from youtube_transcript_api import (
    YouTubeTranscriptApi,
    NoTranscriptFound,
    TranscriptsDisabled,
    VideoUnavailable
)

def transcribe_video(video_id):
    try:
        transcript = YouTubeTranscriptApi().fetch(video_id)
        return " ".join(snippet.text for snippet in transcript)

    except (NoTranscriptFound, TranscriptsDisabled):
        return None

    except VideoUnavailable:
        return None

    except Exception as e:
        print(f"Unexpected error: {e}")
        return None