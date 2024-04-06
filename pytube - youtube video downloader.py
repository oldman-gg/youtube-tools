#pip install pytube
from pytube import YouTube

def download_video(url, path):
    """
    Downloads a YouTube video to the specified path.

    :param url: The URL of the YouTube video
    :param path: The path where the video will be saved
    """
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path=path)
        print(f"Downloaded '{yt.title}' successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    download_path = input("Enter the download path (leave blank for current directory): ")
    download_video(video_url, download_path)
