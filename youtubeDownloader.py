from pytube import YouTube, Playlist
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk


def download_video(video, format, destination, progress_bar):
    if format == "mp3":
        ys = video.streams.filter(only_audio=True).first()
    elif format == "mp4":
        ys = video.streams.get_highest_resolution()
    else:
        return 0

    # Downloading file
    print("Downloading...")
    out_file = ys.download(output_path=destination, filename_prefix="downloading_")

    # Changing file extension if user chose mp3
    if format == "mp3":
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

    print("Download completed.")
    progress_bar.stop()


def download():
    # Create GUI window
    root = tk.Tk()
    root.title("YouTube Downloader")

    # Create input URL entry
    url_label = tk.Label(root, text="Enter URL:")
    url_label.grid(row=0, column=0)
    url_entry = tk.Entry(root, width=50)
    url_entry.grid(row=0, column=1)

    # Create format dropdown
    format_label = tk.Label(root, text="Download format:")
    format_label.grid(row=1, column=0)
    format_var = tk.StringVar(value="mp4")
    format_dropdown = tk.OptionMenu(root, format_var, "mp3", "mp4")
    format_dropdown.grid(row=1, column=1)

    # Create destination directory entry
    destination_label = tk.Label(root, text="Destination directory:")
    destination_label.grid(row=2, column=0)
    destination_var = tk.StringVar(value=os.getcwd())
    destination_entry = tk.Entry(root, textvariable=destination_var, width=50)
    destination_entry.grid(row=2, column=1)
    def choose_destination():
        chosen_directory = filedialog.askdirectory()
        if chosen_directory:
            destination_var.set(chosen_directory)
    choose_destination_button = tk.Button(root, text="Choose directory", command=choose_destination)
    choose_destination_button.grid(row=2, column=2)

    # Create progress bar
    progress_bar = ttk.Progressbar(root, orient="horizontal", length=200, mode="indeterminate")
    progress_bar.grid(row=3, column=1)

    def start_download():
        url = url_entry.get()
        # Check if input URL is a playlist
        if 'playlist' in url.lower():
            playlist = Playlist(url)
            # Ask if User wants mp3 or mp4
            format = format_var.get()
            # Enter destination directory
            destination = destination_var.get()

            progress_bar.start()

            for video in playlist.videos:
                download_video(video, format, destination, progress_bar)

        else:
            # If input URL is not a playlist, download the single video
            yt = YouTube(url)
            # Ask if User wants mp3 or mp4
            format = format_var.get()
            # Enter destination directory
            destination = destination_var.get()

            progress_bar.start()

            download_video(yt, format, destination, progress_bar)

    # Create download button
    download_button = tk.Button(root, text="Download", command=start_download)
    download_button.grid(row=4, column=1)

    # Create quit button
    quit_button = tk.Button(root, text="Quit", command=root.destroy)
    quit_button.grid(row=4, column=0)

    root.mainloop()

if __name__ == "__main__":
    download()