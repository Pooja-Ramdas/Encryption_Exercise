import tkinter as tk
from tkinter import messagebox
import hashlib
#import main_init

#main_init.__init()



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

def display_tool_info(tool):
    tool_info = get_tool_info(tool)

    result_label.config(text=f"1. What is this tool?\n\n"
                             f"2. Proprietary alternatives of this tool?\n\n"
                             f"3. What languages is this tool written in?")
    
cipher_dictionary = {
    "Linux": hash_text("Linux"),  # [FOSS Open Source]
	"Syncthing": hash_text("Syncthing"),  # [File Synchronization Application]
	"OBS": hash_text("OBS"),  # [Screencasting and Streaming Application]
	"Llama": hash_text("Llama"),  # [Autoregressive large language model]
	"Ghidra": hash_text("Ghidra"),  # [FOSS Reverse Engineering tool]
	"Blender": hash_text("Blender"),  # [3D computer graphics software tool]
	"VLCMediaPlayer": hash_text("VLCMediaPlayer"),  # [FOSS Media Player]
	"Audacity": hash_text("Audacity"),  # [FOSS Audio editor]
	"RobotOperatingSystem": hash_text("RobotOperatingSystem"),  # [FOSS robotics middleware suite]
	"MozillaFirefox": hash_text("MozillaFirefox"),  # [FOSS Browser]
	"LibreOffice": hash_text("LibreOffice"),  # [FOSS alternative of Office]
	"MYSQL": hash_text("MYSQL"),  # [FOSS alternative of Oracle]
	"Python": hash_text("Python"),  # [Programming Language]
	"Ruby": hash_text("Ruby"),  # [Programming Language]
	"PHP": hash_text("PHP"),  # [Programming Language]
	"GIT": hash_text("GIT"),  # [Version Control System]
	"Mercurial": hash_text("Mercurial"),  # [Version Control System]
	"VisualStudioCode": hash_text("VisualStudioCode"),  # [FOSS code editor]
	"WordPress": hash_text("WordPress"),  # [Content Management System]
	"Chromium": hash_text("Chromium"),  # [Web browser engine]
	"RPCS3": hash_text("RPCS3"),  # [PS3 emulator]
	"VirtualBox": hash_text("VirtualBox"),  # [Open Source Virtualization]
	"GIMP": hash_text("GIMP"),  # [GNU Image Manipulation Program]
	"Inkscape": hash_text("Inkscape"),  # [Vector Graphics Editor]
	"Nginx": hash_text("Nginx"),  # [Web Servers]
	"ApacheHTTPServer": hash_text("ApacheHTTPServer"),  # [Web Servers]
	"Wireshark": hash_text("Wireshark"),  # [network protocol analyzer]
	"Docker": hash_text("Docker"),  # [Containers and Orchestration]
	"Vim": hash_text("Vim"),  # [Text Editors]
	"SevenZip": hash_text("7zip"),  # [FOSS Archiver]
	"Nodejs": hash_text("Nodejs"),  # [Development Frameworks]
	"RubyonRails": hash_text("RubyonRails"),  # [Development Frameworks]
	"TensorFlow": hash_text("TensorFlow"),  # [Machine Learning and Data Science]
	"Signal": hash_text("Signal"),  # [WhatsApp alternative]
	"Darktable": hash_text("Darktable"),  # [Lightroom alternative]
	"AOSP": hash_text("AOSP"),  # [Android]
	"React": hash_text("React"),  # [Library for web and native user interface]
	"Flutter": hash_text("Flutter"),  # [UI Software development kit]
	"VisualBoyAdvance": hash_text("VisualBoyAdvance"),  # [FOSS Emulator of Gameboy]
	"StableDiffusion": hash_text("StableDiffusion"),  # [Deep Learning text-to-image model]
	"Electron": hash_text("Electron"),  # [FOSS framework developed and maintained by OpenJS Foundation]
	"Rust": hash_text("Rust"),  # [Multi-paradigm, general-purpose programming language]
	"Godot": hash_text("Godot"),  # [FOSS Game Engine]
	"Django": hash_text("Django"),  # [FOSS Python-based web framework]
	"Pytorch": hash_text("Pytorch"),  # [ML Framework]
	"OpenCV": hash_text("OpenCV"),  # [Real-time computer vision]
	"Qbittorrent": hash_text("Qbittorrent"),  # [FOSS torrent client]
	"Krita": hash_text("Krita"),  # [FOSS digital art and 2D animation]
	"TorBrowser": hash_text("TorBrowser"),  # [FOSS that enables anonymous connection]
	"Magisk": hash_text("Magisk"),  # [FOSS tool to root Android devices]
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
