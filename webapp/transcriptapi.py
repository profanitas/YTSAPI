from youtube_transcript_api import YouTubeTranscriptApi

def get_subtitles(video_url):
    video_id = video_url.split('?v=')[1]
    try:
        subtitles = YouTubeTranscriptApi.get_transcript(video_id)
        return subtitles
    except Exception:
        return {"message":"Error retrieving subtitles"}
