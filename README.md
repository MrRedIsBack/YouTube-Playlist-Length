# YouTube Playlist Total Watch Time Calculator

This Python script calculates the total duration (watch time) of all videos in a YouTube playlist using the YouTube Data API v3. Given a playlist ID, it fetches video IDs, retrieves each video's duration, and sums them up into hours, minutes, and seconds.

## Features
- Handles playlists of any size by paginating API results.
- Parses ISO 8601 duration format (e.g., "PT2H30M15S") into total seconds.
- Displays total time in a human-readable format.
- Requires a free YouTube Data API key from Google Cloud Console.
- Deals with private/deleted videos.

## Prerequisites
- Python 3.6+ with `google-api-python-client` and `google-auth-oauthlib` libraries.
- YouTube Data API v3 enabled and API key created (see Setup).

### Installation

Clone the repository:
```bash
git clone https://github.com/MrRedIsBack/YouTube-Playlist-Length.git
```
Install requirements:
```bash
pip install -r requirements.txt
```

## Setup
1. Go to [Google Cloud Console](https://console.cloud.google.com/).
2. Create a project, enable YouTube Data API v3.
3. Create credentials (API key) and copy it.

## Usage
Run the script and use the terminal.

## License
MIT License. See LICENSE file for details.
