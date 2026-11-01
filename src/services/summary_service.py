import asyncio
import os

from langchain_openai import ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter


llm = ChatOpenAI(
    model="deepseek-flash",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",
    temperature=0
)


async def summarize_chunk(chunk: str) -> str:
    response = await llm.ainvoke(
        f"""
        Summarize this transcript chunk.

        Requirements:
        - Keep all important information.
        - Preserve names, dates, numbers, and facts.
        - Use concise bullet points.
        - Do not add information not present in the transcript.

        Transcript:
        {chunk}
        """
    )

    return response.content


async def summarize_transcript(transcript: str) -> str:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=10000,
        chunk_overlap=500
    )

    chunks = splitter.split_text(transcript)

    chunk_summaries = await asyncio.gather(
        *(summarize_chunk(chunk) for chunk in chunks)
    )

    merged_summaries = "\n\n".join(chunk_summaries)

    final_response = await llm.ainvoke(
        f"""
        Below are summaries of different parts of a video.

        Generate a final comprehensive summary.

        Include:
        - Overview
        - Key takeaways
        - Important details
        - Actionable insights

        Summaries:

        {merged_summaries}
        """
    )

    return final_response.content


# Usage
# final_summary = asyncio.run(
#     summarize_transcript(transcript_text)
# )
# print(final_summary)