from pymongo import MongoClient

# connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["libraryDB"]
collection = db["books"]

print("Connected to MongoDB!")
import tkinter as tk
from tkinter import messagebox
from pymongo import MongoClient

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")
db = client["libraryDB"]
collection = db["books"]

# GUI window
root = tk.Tk()
root.title("Library - CRUD App")
root.geometry("500x450")

# Labels & Entry boxes
tk.Label(root, text="Book Title").pack()
title_entry = tk.Entry(root)
title_entry.pack()

tk.Label(root, text="Author").pack()
author_entry = tk.Entry(root)
author_entry.pack()

tk.Label(root, text="Year").pack()
year_entry = tk.Entry(root)
year_entry.pack()

tk.Label(root, text="Copies").pack()
copies_entry = tk.Entry(root)
copies_entry.pack()
# CREATE
def add_book():
    title = title_entry.get()
    author = author_entry.get()
    year = int(year_entry.get())
    copies = int(copies_entry.get())

    collection.insert_one({"title": title, "author": author, "year": year, "copies": copies})
    messagebox.showinfo("Success", "Book Added!")

# READ
def view_books():
    books = collection.find()
    data = ""
    for book in books:
        data += f"{book['title']} - {book['author']} - {book['year']} - Copies: {book['copies']}\n"
    messagebox.showinfo("Library Books", data)

# UPDATE
def update_book():
    title = title_entry.get()
    new_copies = int(copies_entry.get())
    collection.update_one({"title": title}, {"$set": {"copies": new_copies}})
    messagebox.showinfo("Updated", "Copies Updated!")

# DELETE
def delete_book():
    title = title_entry.get()
    collection.delete_one({"title": title})
    messagebox.showinfo("Deleted", "Book Deleted!")
tk.Button(root, text="Add", command=add_book).pack(pady=5)
tk.Button(root, text="View", command=view_books).pack(pady=5)
tk.Button(root, text="Update", command=update_book).pack(pady=5)
tk.Button(root, text="Delete", command=delete_book).pack(pady=5)

root.mainloop()

