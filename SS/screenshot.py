from PIL import ImageGrab
from pynput import keyboard
import win32gui

# import pyautogui


def screen_shot():
    handle = win32gui.GetForegroundWindow()
    rect = win32gui.GetWindowRect(handle)

    screenshot = ImageGrab.grab()
    croped_ss = screenshot.crop(rect)
    croped_ss.save("originalapp/SS/ss.png")


def press(key):
    try:
        if key == keyboard.Key.print_screen:
            print("アルファベット{0}が押されました".format(key.char))
    except AttributeError:
        if key == keyboard.Key.print_screen:
            screen_shot()


def release(key):
    if key == keyboard.Key.esc:
        return False


listener = keyboard.Listener(on_press=press, on_release=release)
listener.start()
