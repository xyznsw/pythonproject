import os
import tkinter as tk
from tkinter import ttk

def get_folder_sizes(root_folder):
    folder_sizes = {}

    for folder_name in os.listdir(root_folder):
        folder_path = os.path.join(root_folder, folder_name)
        if os.path.isdir(folder_path):
            folder_size = get_folder_size(folder_path)
            folder_sizes[folder_name] = folder_size / (1024 * 1024)  # Convert to MB

    root_folder_size = get_folder_size(root_folder) / (1024 * 1024)  # Convert to MB
    folder_sizes[root_folder] = root_folder_size  # Add root folder size to the dictionary with custom key

    return folder_sizes

def get_folder_size(folder_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            total_size += os.path.getsize(file_path)
    return total_size

def show_folder_sizes():
    root_folder = folder_entry.get()
    folder_sizes = get_folder_sizes(root_folder)

    for child in result_frame.winfo_children():
        child.destroy()  # Clear the previous results

    tree = ttk.Treeview(result_frame, columns=("Folder", "Size (MB)"), show="headings")
    tree.column("Folder", anchor='e')
    tree.column("Size (MB)", anchor='e')
    tree.heading("Folder", text="Folder")
    tree.heading("Size (MB)", text="Size (MB)")

    sorted_folders = sorted(folder_sizes.items(), key=lambda x: x[0] != root_folder)  # Sort by root folder
    for folder_name, folder_size_mb in sorted_folders:
        tree.insert("", "end", values=(folder_name, "{:,}".format(round(folder_size_mb,2))))

    tree.pack(expand=True, fill=tk.BOTH)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Folder Size Viewer")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_width = 400
    window_height = 300

    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2

    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    folder_label = tk.Label(root, text="Enter folder path:")
    folder_label.pack()

    folder_entry = tk.Entry(root, width=60)
    folder_entry.insert(0, "c:\\coding\\pythonproject")  # Set the default text in the entry widget
    folder_entry.pack()

    show_button = tk.Button(root, text="Show Folder Sizes", command=show_folder_sizes)
    show_button.pack()

    result_frame = tk.Frame(root)
    result_frame.pack(fill=tk.BOTH, expand=True)

    root.mainloop()
