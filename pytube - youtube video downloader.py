from pytube import YouTube
import logging

# Configure logging to display informational messages
logging.basicConfig(level=logging.INFO)

def download_video(url, path):
    """
    Downloads the highest resolution of a YouTube video to the specified path.

    :param url: The URL of the YouTube video
    :param path: The path where the video will be saved
    """
    try:
        yt = YouTube(url, on_progress_callback=progress_callback)
        stream = yt.streams.get_highest_resolution()  # Always get the highest resolution
        stream.download(output_path=path)
        logging.info(f"Downloaded '{yt.title}' successfully.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

def progress_callback(stream, chunk, bytes_remaining):
    """
    Callback function to monitor the download progress.

    :param stream: Stream object of the video being downloaded
    :param chunk: Chunk of data that was downloaded
    :param bytes_remaining: Number of bytes remaining to download
    """
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    print(f'Downloading: {percentage_of_completion:.2f}%', end='\r')

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    download_path = input("Enter the download path (leave blank for current directory): ")
    download_video(video_url, download_path)
