import ctypes
import time
import tkinter as tk
from tkinter import filedialog, messagebox
import threading
import os
import random
import psutil

KEYEVENTF_KEYUP = 0x0002

def send_input(char):
    if len(char) == 1:
        vk = ctypes.windll.user32.VkKeyScanW(ord(char))
        shift = vk >> 8
        key = vk & 0xff
        if shift & 1:
            keybd_event(0x10, 0, 0, 0)
        keybd_event(key, 0, 0, 0)
        keybd_event(key, 0, KEYEVENTF_KEYUP, 0)
        if shift & 1:
            keybd_event(0x10, 0, KEYEVENTF_KEYUP, 0)

def keybd_event(bVk, bScan, dwFlags, dwExtraInfo):
    ctypes.windll.user32.keybd_event(bVk, bScan, dwFlags, dwExtraInfo)

def press_enter():
    keybd_event(0x0D, 0, 0, 0)
    keybd_event(0x0D, 0, KEYEVENTF_KEYUP, 0)

def press_backspace(times=1, delay=True):
    for _ in range(times):
        keybd_event(0x08, 0, 0, 0)
        keybd_event(0x08, 0, KEYEVENTF_KEYUP, 0)
        if delay:
            time.sleep(random.uniform(0.1, 0.25))

class StealthGUIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stealth Auto Typer - No Repeats")
        self.root.geometry("580x440")
        self.root.configure(bg="#121212")

        self.file_path = ""
        self.lines = []
        self.typing_active = False
        self.pause_typing = False
        self.typed_chars = 0
        self.status = tk.StringVar(value="Status: Idle")

        self.setup_gui()

    def setup_gui(self):
        tk.Label(self.root, text="Stealth Auto Typer (Human Mode - No Repeats)", font=("Helvetica", 16, "bold"), bg="#121212", fg="#76FF03").pack(pady=10)
        tk.Button(self.root, text="Select File", command=self.select_file, bg="#76FF03", fg="black").pack(pady=5)
        self.file_label = tk.Label(self.root, text="No file selected", bg="#121212", fg="white")
        self.file_label.pack()

        tk.Label(self.root, text="Start Delay (sec):", bg="#121212", fg="white").pack()
        self.delay_entry = tk.Entry(self.root, width=5, justify='center')
        self.delay_entry.insert(0, "5")
        self.delay_entry.pack(pady=5)

        self.countdown_label = tk.Label(self.root, text="", bg="#121212", fg="#FFD700", font=("Courier", 12, "bold"))
        self.countdown_label.pack()

        self.status_label = tk.Label(self.root, textvariable=self.status, bg="#121212", fg="#00FFAA")
        self.status_label.pack()

        tk.Button(self.root, text="Start Typing", command=self.start_typing_thread, bg="#2979FF", fg="white").pack(pady=10)
        tk.Button(self.root, text="Stop", command=self.stop_typing, bg="#FF1744", fg="white").pack(pady=5)

        self.char_timer_label = tk.Label(self.root, text="Characters typed: 0 | Time: 00:00", bg="#121212", fg="white")
        self.char_timer_label.pack(pady=10)

    def select_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if self.file_path:
            with open(self.file_path, "r", encoding="utf-8") as file:
                self.lines = file.readlines()
            self.file_label.config(text=f"Loaded {len(self.lines)} lines")

    def start_typing_thread(self):
        try:
            delay = int(self.delay_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid delay.")
            return
        if not self.file_path or not self.lines:
            messagebox.showerror("Error", "Please select a valid text file.")
            return
        threading.Thread(target=self.start_typing, args=(delay,)).start()

    def start_typing(self, delay):
        self.typing_active = True
        self.typed_chars = 0
        start_time = time.time()
        self.status.set("Starting in a moment...")

        for i in range(delay, 0, -1):
            self.countdown_label.config(text=f"Typing starts in {i} second(s)...")
            time.sleep(1)

        self.countdown_label.config(text="Typing...")
        for line in self.lines:
            if not self.typing_active:
                break
            char_buffer = list(line.strip())
            i = 0
            while i < len(char_buffer):
                if not self.typing_active:
                    break
                char = char_buffer[i]

                if psutil.cpu_percent() > 85:
                    self.status.set("Waiting for CPU to relax...")
                    time.sleep(random.uniform(2.5, 4.5))
                    self.status.set("Typing...")

                if random.random() < 0.015:
                    self.status.set("Thinking...")
                    time.sleep(random.uniform(2.5, 4.0))
                    self.status.set("Typing...")

                if random.random() < 0.01:
                    self.status.set("Distraction...")
                    time.sleep(random.uniform(3.0, 5.0))
                    self.status.set("Typing...")

                if random.random() < 0.025:
                    typo_char = random.choice("abcdefghijklmnopqrstuvwxyz")
                    send_input(typo_char)
                    time.sleep(random.uniform(0.05, 0.12))
                    press_backspace(times=1, delay=True)

                send_input(char)
                self.typed_chars += 1

                if char == ' ':
                    time.sleep(random.uniform(0.14, 0.30))
                elif char in ['.', ',', '?', '!']:
                    time.sleep(random.uniform(0.35, 0.70))
                else:
                    time.sleep(random.uniform(0.22, 0.36))

                elapsed = time.time() - start_time
                mins, secs = divmod(int(elapsed), 60)
                self.char_timer_label.config(text=f"Characters typed: {self.typed_chars} | Time: {mins:02}:{secs:02}")
                i += 1

            press_enter()
            time.sleep(random.uniform(0.6, 1.7))

        self.status.set("Completed")

    def stop_typing(self):
        self.typing_active = False
        self.status.set("Stopped")

if __name__ == "__main__":
    root = tk.Tk()
    app = StealthGUIApp(root)
    root.mainloop()
