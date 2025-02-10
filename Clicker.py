from pynput import mouse, keyboard
import threading
import time


class AutoClicker:
    def __init__(self):
        self.started = False
        self.clicking = False
        self.interval = 0.01
        self.mouse_controller = mouse.Controller()
        self.keyboard_listener = None

    def change_interval(self, interval: float):
        self.interval = interval

    def run(self):
        self.keyboard_listener = keyboard.Listener(on_press=self.__on_press, on_release=self.__on_release)
        threading.Thread(target=self.__run, daemon=True).start()

    def stop(self):
        if self.keyboard_listener and self.keyboard_listener.running:
            self.keyboard_listener.stop()

    def __run(self):
        with self.keyboard_listener:
            self.keyboard_listener.join()

    def __on_press(self, key):
        if key == keyboard.Key.space and not self.clicking:
            self.clicking = True
            threading.Thread(target=self.__click_loop, daemon=True).start()

    def __on_release(self, key):
        if key == keyboard.Key.space:
            self.clicking = False

    def __click_loop(self):
        while self.clicking:
            self.mouse_controller.click(mouse.Button.left)
            time.sleep(self.interval)
