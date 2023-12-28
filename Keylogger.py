import tkinter as tk
from tkinter import *
from pynput import keyboard

target_word = ""

def on_press(key):
    global target_word
    try:
        current_key = key.char
    except AttributeError:
        # Handle special keys like 'space', 'enter', etc.
        current_key = str(key)

    if current_key == target_word:
        print(f"Target word '{target_word}' typed!")

def start_keylogger():
    global listener
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    label.config(text=f"[+] Keylogger is running!\n[!] Monitoring for word: '{target_word}'")
    start_button.config(state='disabled')
    stop_button.config(state='normal')

def stop_keylogger():
    global listener
    listener.stop()
    label.config(text="Keylogger stopped.")
    start_button.config(state='normal')
    stop_button.config(state='disabled')

def set_target_word():
    global target_word
    target_word = entry.get()
    label.config(text=f"[!] Monitoring for word: '{target_word}'")

# GUI
root = Tk()
root.title("College Keylogger")

label = Label(root, text='Enter the word to monitor:')
label.config(anchor=CENTER)
label.pack()

entry = Entry(root)
entry.pack()

set_word_button = Button(root, text="Set Word", command=set_target_word)
set_word_button.pack()

start_button = Button(root, text="Start", command=start_keylogger)
start_button.pack(side=LEFT)

stop_button = Button(root, text="Stop", command=stop_keylogger, state='disabled')
stop_button.pack(side=RIGHT)

root.mainloop()

    

     
