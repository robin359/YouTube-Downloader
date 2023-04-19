from pytube import YouTube, Playlist
import os

# Download Function
def download():
    
    # Input URL from User
    url = input("Enter URL: ")
    
    # Check if input URL is a playlist
    if 'playlist' in url.lower():
        playlist = Playlist(url)
        # Ask if User wants mp3 or mp4
        format = input("Download mp3 or mp4? ")
        # Enter destination directory
        destination = str(input("Enter the destination (leave blank for current directory)\n >> ")) or '.'
        
        for video in playlist.videos:
            # Logic for downloading mp3 or mp4
            if format == "mp3":
                ys = video.streams.filter(only_audio=True).first()
            elif format == "mp4":
                ys = video.streams.get_highest_resolution()
            else:
                return 0
            
            # Downloading file
            print("Downloading...")
            out_file = ys.download(output_path=destination)
            
            # Changing file extension if user chose mp3
            if format == "mp3":
                base, ext = os.path.splitext(out_file)
                new_file = base + '.mp3'
                os.rename(out_file, new_file)
            
            print("Download completed.")
        
    else:
        # If input URL is not a playlist, download the single video
        yt = YouTube(url)
        # Ask if User wants mp3 or mp4
        format = input("Download mp3 or mp4? ")
        # Enter destination directory
        destination = str(input("Enter the destination (leave blank for current directory)\n >> ")) or '.'
        
        # Logic for downloading mp3 or mp4
        if format == "mp3":
            ys = yt.streams.filter(only_audio=True).first()
        elif format == "mp4":
            ys = yt.streams.get_highest_resolution()
        else:
            return 0
        
        # Downloading file
        print("Downloading...")
        out_file = ys.download(output_path=destination)
        
        # Changing file extension if user chose mp3
        if format == "mp3":
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
        
        print("Download completed.")
    
    # Continuing
    download()

download()
