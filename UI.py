import tkinter as tk


class App:
    def __init__(self, root, clicker):
        self.clicker = clicker
        self.clicker_running = False

        self.root = root
        self.root.title("AutoClicker")
        self.root.geometry("300x150")
        self.root.resizable(False, False)

        self.start_button = tk.Button(root, text="Start", width=20, height=2, command=self.toggle_clicker)
        self.start_button.pack(side=tk.TOP, pady=20)

        self.settings_button = tk.Button(root, text="Settings", width=10, command=self.open_settings_window)
        self.settings_button.pack(side=tk.TOP, pady=10)

    def toggle_clicker(self):
        if not self.clicker_running:
            self.clicker_running = True
            self.clicker.run()
            self.start_button["text"] = "Stop"
        else:
            self.clicker_running = False
            self.clicker.stop()
            self.start_button["text"] = "Start"

    def open_settings_window(self):
        settings_window = tk.Toplevel(self.root)
        settings_window.title("Settings")
        settings_window.geometry("300x150")

        frame = tk.Frame(settings_window)
        frame.pack(pady=10, padx=10)

        tk.Label(frame, text="Click interval (sec):").grid(row=0, column=0, padx=5)

        interval_entry = tk.Entry(frame, width=10)
        interval_entry.grid(row=0, column=1, padx=5)
        interval_entry.insert(0, str(self.clicker.interval))

        def save_settings():
            try:
                new_interval = float(interval_entry.get())
                self.clicker.change_interval(new_interval)
            except ValueError:
                pass
            settings_window.destroy()

        save_button = tk.Button(settings_window, text="Save", command=save_settings)
        save_button.pack(pady=10)
