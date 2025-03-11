import tkinter as tk
from tkinter import ttk

class SearchScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.search_label = ttk.Label(self, text="Search:")
        self.search_label.pack(pady=10)

        self.search_entry = ttk.Entry(self)
        self.search_entry.pack(pady=10)

        self.search_button = ttk.Button(self, text="Search", command=self.perform_search)
        self.search_button.pack(pady=10)

        self.results_label = ttk.Label(self, text="")
        self.results_label.pack(pady=10)

    def perform_search(self):
        search_string = self.search_entry.get()
        self.results_label.config(text=f"Searching for: {search_string}")


