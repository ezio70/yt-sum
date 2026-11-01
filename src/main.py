from src.services.transcript_service import transcribe_video
from src.services.summary_service import summarize_transcript
import asyncio
def main(url: str) -> str:
    video_id = url.split("v=")[1]
    transcript = transcribe_video(video_id)
    if transcript:
        summary = asyncio.run(summarize_transcript(transcript))
        return(summary)
    else:
        return None







