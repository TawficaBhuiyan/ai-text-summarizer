from typing import List


def chunk_text(text: str, max_chars: int = 3000) -> List[str]:
 """A simple chunker splitting by paragraph while keeping chunks under max_chars."""


def chunk_text(text, max_chars=4000):
    paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
    chunks = []
    current_chunk = ""


    for p in paragraphs:
        if len(current_chunk) + len(p) + 2 <= max_chars:
            current_chunk += ("\n\n" + p if current_chunk else p)
        else:
            chunks.append(current_chunk)
            current_chunk = p


    if current_chunk:
        chunks.append(current_chunk)


    return chunks
