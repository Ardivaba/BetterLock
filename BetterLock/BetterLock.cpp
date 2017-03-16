// Writing C++ in Python style must be sacrilege. But meh, consistency wins.

/*
	So the way it works is that when you're holding capslock all keypresses are blocked and stored in a limited queue.
	That limited queue is then queried by python app.
	Python app is also responsible for clearing the queue.

	Methods exposed to python:
		queue_array		get_queue()
		void			clear_queue()
*/

#include "stdafx.h"
#include <Windows.h>
#include <queue>
#include <tuple>
#include <map>
#include <vector>

// Define to make writing extenr C declspec export easier and more comprehensible
#define DLLEXPORT extern "C" __declspec(dllexport)
using namespace std;

bool debug = false;
HHOOK keyboard_hook;

struct keyboard_key_event {
	int key_code = -1;
	bool just_pressed = true;
};

vector<keyboard_key_event> keyboard_event_queue;
keyboard_key_event current_event;

int layer = 0;
vector<vector<int>> key_maps;

DLLEXPORT void set_layer(int new_layer)
{
	layer = new_layer;
}

DLLEXPORT void map_key(int original_key, int mapped_key, int layer)
{
	key_maps[layer][original_key] = mapped_key;
}

DLLEXPORT void press_key(int key_code)
{
	keybd_event(key_code, 0, 0, 0);
}

DLLEXPORT void release_key(int key_code)
{
	keybd_event(key_code, 0, KEYEVENTF_KEYUP, 0);
}

DLLEXPORT bool event_selected()
{
	if (current_event.key_code != -1)
		return true;
	else
		return false;
}

DLLEXPORT void set_debug(bool value)
{
	debug = value;
}

DLLEXPORT int get_key()
{
	return current_event.key_code;
}

DLLEXPORT bool just_pressed()
{
	return current_event.just_pressed;
}

DLLEXPORT bool has_events()
{
	return keyboard_event_queue.size() > 0;
}

DLLEXPORT bool pop()
{
	if (keyboard_event_queue.size() < 1)
		return false;

	current_event = keyboard_event_queue.back();
	keyboard_event_queue.pop_back();

	return has_events();
}

// Gets called when any of the keyboard keys are pressed
DLLEXPORT LRESULT keyboard_event(int code, WPARAM w_param, LPARAM l_param)
{
	char pressed_key;
	KBDLLHOOKSTRUCT *p_keyboard = (KBDLLHOOKSTRUCT *)l_param;

	if ((code == HC_ACTION) && ((code == WM_SYSKEYDOWN) || (w_param == WM_KEYDOWN)))
	{
		pressed_key = (char)p_keyboard->vkCode;

		bool capslock_toggled = GetKeyState(VK_CAPITAL);
		bool capslock_held = GetKeyState(VK_CAPITAL) & 0x80;

		if (capslock_held)
		{
			keyboard_key_event key_event;
			key_event.key_code = pressed_key;
			bool event_found = false;

			for (int i = 0; i < keyboard_event_queue.size(); i++)
			{
				keyboard_key_event loop_key_event = keyboard_event_queue[i];
				if (loop_key_event.key_code == key_event.key_code)
				{
					event_found = true;
					keyboard_event_queue[i].just_pressed = false;
				}
			}

			if (!event_found)
			{
				keyboard_event_queue.push_back(key_event);

				if(debug)
					printf("Added key: %i to queue.\n", key_event.key_code);
			}

			return 1;
		}
	}

	return CallNextHookEx(keyboard_hook, code, w_param, l_param);
}

// Message loop
void message_loop()
{
	MSG message;
	while (GetMessage(&message, NULL, 0, 0))
	{
		TranslateMessage(&message);
		DispatchMessage(&message);
	}
}

// Set hotkey hooks
DWORD WINAPI hotkey(LPCWSTR lp_param)
{
	HINSTANCE h_instance = GetModuleHandle(NULL);
	if (!h_instance) h_instance = LoadLibrary(lp_param);
	if (!h_instance) return 1;

	keyboard_hook = SetWindowsHookEx(WH_KEYBOARD_LL, (HOOKPROC)keyboard_event, h_instance, NULL);
	message_loop();
	UnhookWindowsHookEx(keyboard_hook);
	return 0;
}

// Start blocking keys when capslock is held
DLLEXPORT void start()
{
	HANDLE h_thread;
	DWORD dw_thread;

	if(debug)
		printf("Capslock memes activated...\n");
	h_thread = CreateThread(NULL, NULL, (LPTHREAD_START_ROUTINE)hotkey, NULL, NULL, &dw_thread);
}

int main()
{
	start();
	while (true) {

	}
    return 0;
}