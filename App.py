import os
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube
from tkinter import messagebox
from tkinter import PhotoImage

class YouTubeDownloader:
    def __init__(self, master):
        self.master = master
        master.title("YT Droid YouTube Downloader")

        style=ttk.Style()
        style.theme_use("clam")

        # Create a label Header 
        header = ttk.Label( text=" Ӝ YT DROID    ", foreground="red", background="white", font=("Inter bold", 72))
        header.pack()

        # Create a label Header
        header = ttk.Label( text=" YouTube Video Downloader  ", foreground="White", background="red", font=("Inter bold", 36))
        header.pack()

        # Create a label and entry widget for the video URL
        url_label = ttk.Label(master, text="Enter Video URL:", font=("Inter regular", 15))
        url_label.pack()
        self.url_entry = ttk.Entry(master, width=50)
        self.url_entry.pack()

        # Create a label and combobox for the video quality
        quality_label = ttk.Label(master, text="Select Video Quality:", font=("Inter regular", 15))
        quality_label.pack()
        self.quality_combobox = ttk.Combobox(master, values=["1080p","720p", "480p", "360p", "240p", "144p"])
        self.quality_combobox.current(0)
        self.quality_combobox.pack()

        # Create a button to select the save directory
        save_dir_button = ttk.Button(master, text="Select Save Directory", command=self.select_save_dir)
        save_dir_button.pack()

        # ttk Button style for dowload Button
        style.configure('dowloadbtn.TButton', font=("Inter bold", 16),width=20,bordercolor="red")
        style.map('dowloadbtn.TButton',background=[('active','white'),('!disabled',"red")],foreground=[('active','red'),('!disabled',"white")])

        # Create a button to start the download
        download_button = ttk.Button(master, text="Download", command=self.download_video,style='dowloadbtn.TButton')
        download_button.pack(ipady=10, ipadx=200,)

        # Create a progress bar to show the download progress
        self.progress_bar = ttk.Progressbar(master, orient="horizontal", length=300, mode="determinate")
        self.progress_bar.pack()

        # Initialize the save directory to the current directory
        self.save_dir = os.getcwd()

        # Create a label Header
        header = ttk.Label( text="Made by Viraj Ray 2023©", font=("Inter medium", 10), )
        header.pack()

    # Define a function to select the save directory
    def select_save_dir(self):
        self.save_dir = filedialog.askdirectory(title="Select Save Directory")

    # Define a function to download the video
    def download_video(self):
        # Get the URL of the video from the entry widget
        video_url = self.url_entry.get()

        # Create a YouTube object
        video = YouTube(video_url)

        # Get the video stream with the selected quality
        video_stream = video.streams.filter(res=self.quality_combobox.get(), only_audio=False).first()

        # Download the video to the selected directory
        video_stream.download(output_path=self.save_dir, filename_prefix="YouTube Downloader")

        # Show a message box when the video has been downloaded
        tk.messagebox.showinfo(title="Download Complete", message="The video has been downloaded.")

    # Define a function to update the progress bar
    def update_progress_bar(self, stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        progress = (bytes_downloaded / total_size) * 100
        self.progress_bar["value"] = progress

# Create the main window
root = tk.Tk()
my_downloader = YouTubeDownloader(root)

#Set the geometry of tkinter window
root.geometry("690x450")

#Set the icon of tkinter window
root.iconbitmap(r"C:\Users\Viraj Ray\Downloads\104447_apple_logo_icon.ico")

# Start the mainloop.
root.mainloop()

#The method select_save_dir uses filedialog.askdirectory, 
# which is a blocking operation. It is recommended to run it in a separate 
# thread or use an asynchronous approach to prevent the GUI from freezing.