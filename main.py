import os
from dotenv import load_dotenv

import googleapiclient.discovery

import isodate

load_dotenv(dotenv_path = "keys.env")

youtube_api_key = os.getenv("YouTube_API_KEY")

youtube = googleapiclient.discovery.build("youtube", "v3", developerKey = youtube_api_key)

# Given a video ID, return the length of the video in seconds
def get_video_length(video_id: str) -> float:
    request = youtube.videos().list(
        part = "contentDetails", id = video_id
    )

    response = request.execute()

    # This is in ISO 8601 format, so we need to convert it to seconds
    try:
        duration = response["items"][0]["contentDetails"]["duration"]

    # This can occur if the video is private or deleted, so we will just return 0 in that case
    except (KeyError, IndexError):
        print(f"Error occurred while fetching duration for video ID: {video_id}")
        print(f"response: {response}")
        return 0

    parsed_duration = isodate.parse_duration(duration)
    total_seconds = parsed_duration.total_seconds()

    return total_seconds

# Given a playlist ID, return a list of all video IDs and titles in the playlist
def get_all_videos_from_playlist(playlist_id: str) -> list:
    all_videos = []  # Initialize a single list to hold all video IDs

    next_page_token = None

    # Fetch videos from the current playlist
    while True:
        playlist_request = youtube.playlistItems().list(
            part = "snippet,contentDetails",
            playlistId = playlist_id,
            maxResults = 50,
            pageToken = next_page_token)
        playlist_response = playlist_request.execute()

        for pl_item in playlist_response["items"]:
            all_videos.append({"Video_ID": pl_item["contentDetails"]["videoId"], "Title" : pl_item["snippet"]["title"]})

        next_page_token = playlist_response.get("nextPageToken")

        if next_page_token is None:
            break

    return all_videos

#playlist_id = PLYNWcRHKhTsuNvqQY279DU4SYDswHemzQ
#lit hq id = PLs1Uc0mySIqtTr80fTKcTnFBXjvt9_Fl0

while True:
    playlist_id = input("Enter a YouTube playlist ID (or 'exit' to quit): ")
    if playlist_id.lower() == "exit":
        break

    videos = get_all_videos_from_playlist(playlist_id)

    total_length = 0

    for video in videos:
        title = video["Title"]
        video_id = video["Video_ID"]

        # This will be in seconds
        length = get_video_length(video_id)

        total_length += length

        print(f"{title} - {length}s")

    hours = total_length // 3600
    minutes = (total_length % 3600) // 60
    seconds = total_length % 60

    print(f"Total length: {hours} hours, {minutes} minutes, {seconds} seconds")