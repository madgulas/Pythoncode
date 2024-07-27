import tkinter as tk
from tkinter import Entry, Label, Button
import webbrowser

#Define the main window
root=tk.Tk()
root.title("Your AI Assistant")

#Adding a bg color
root.configure(bg='steelblue')

#Define the function to atumate youtube search

def search_youtube():
    query =entry.get()
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)


def search_instagram():
    username =entry.get().replace('@', "")
    url = f"https://www.instagram.com/{username}/"
    webbrowser.open(url)


def search_google():
    query =entry.get()
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

#create input field, labels and buttons
Label(root, text= "Enter your username:").pack(pady=10)
entry=Entry(root, width=50)
entry.pack(pady=10)
Button(root, text= "Search on Youtube", command = search_youtube).pack(pady=5)
Button(root, text= "Search on instagram", command = search_instagram).pack(pady=5)
Button(root, text= "Search on google", command = search_google).pack(pady=15)

#Run the GUI event loop
root.mainloop()