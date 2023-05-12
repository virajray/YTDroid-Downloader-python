import os
import tkinter as tk
from tkinter import filedialog
from pytube import YouTube


# Define a function to download the video
def download_video():
    # Get the URL of the video from the entry widget
    video_url = url_entry.get()

    # Create a YouTube object
    video = YouTube(video_url)

    # Get the video stream
    video_stream = video.streams.filter(only_audio=False).first()

    # Ask the user to select a directory to save the video in
    save_dir = filedialog.askdirectory(title="Select Directory")

    # Download the video to the selected directory
    video_stream.download(output_path=os.path.join(save_dir, video.title))

    # Show a message box when the video has been downloaded
    tk.messagebox.showinfo(title="Download Complete", message="The video has been downloaded.")


# Create the main window
root = tk.Tk()
root.title("YouTube Video Downloader")

# Create a label and entry widget for the video URL
url_label = tk.Label(root, text="Enter Video URL:")
url_label.pack()
url_entry = tk.Entry(root, width=50)
url_entry.pack()

# Create a button to start the download
download_button = tk.Button(root, text="Download Video", command=download_video)
download_button.pack()

# Start the main event loop
root.mainloop()