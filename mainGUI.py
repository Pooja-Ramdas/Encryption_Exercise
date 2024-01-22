import tkinter as tk
from tkinter import messagebox
import hashlib
import main_init

main_init.__init()



def hash_text(text):
    sha256_hash = hashlib.sha256(text.encode()).hexdigest()
    return sha256_hash

def find_key_of_hash(input_hash, dictionary):
    for tool, hashed_value in dictionary.items():
        if input_hash == hashed_value:
            return tool
    return None

def check_hash():
    user_input_hash = entry.get()
    found_tool = find_key_of_hash(user_input_hash, cipher_dictionary)

    if found_tool:
        result_label.config(text=f"The hash corresponds to: {found_tool}")
    else:
        result_label.config(text="No matching hash found.")

#Replace dictionary later
cipher_dictionary = {
    "apache": hash_text("apache"),
    "firefox": hash_text("firefox"),
    "linux": hash_text("linux"),
}

window = tk.Tk()
window.title("Hash Finder")
window.geometry("500x300")
font=("Times New Roman", 17)

entry_label = tk.Label(window, text="Enter a SHA-256 hash:", font=font)
entry_label.pack(pady=20)

entry = tk.Entry(window, width=60)
entry.pack(pady=5)

search_button = tk.Button(window, text="Search", command=check_hash, font=font)
search_button.pack(pady=10)

result_label = tk.Label(window, text="")
result_label.pack(pady=10)


window.mainloop()
