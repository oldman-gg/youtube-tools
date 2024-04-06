# Video Modification Toolkit

## Overview
This repository hosts a Python-based toolkit for downloading and modifying video files, particularly from YouTube. The primary functionality at present is the ability to download videos in their highest resolution.

## Features
- **Download High-Resolution Videos:** Downloads the highest available resolution of a YouTube video.

## How to Use
1. **Set Up Your Environment:** Ensure you have Python installed on your machine.
2. **Install Dependencies:** You need to install `pytube`, which is a library used for interacting with YouTube content. Install it via pip:
 pip install pytube
3. **Run the Script:** Execute the script and follow the prompts to download your desired YouTube video.

## Tools and Libraries Used
- **Python:** The core programming language used for the script.
- **Pytube:** A lightweight, dependency-free Python library for downloading YouTube Videos.

## Getting Started
To use this toolkit, clone the repository and navigate to the cloned directory. Make sure you have Python and the necessary libraries installed. Run the script using:
python "pytube - YouTube Video Downloader.py"

Replace "pytube - YouTube Video Downloader.py" with the actual path to the script if it is located in a different directory.

## How it Works
The script `download_video` function takes a YouTube URL and a download path as arguments. It then uses `pytube` to fetch and download the highest resolution stream available for that video. During the download process, the script outputs the download progress in percentage to the console.

## Error Handling
Logging is implemented to handle and report errors during the download process. If an error occurs, it will be logged with an appropriate error message.
