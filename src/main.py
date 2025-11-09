import argparse
from src.utils import chunk_text
from src.summarizer import summarize_text


def summarize_input(text: str):
    chunks = chunk_text(text, max_chars=3000)
    if len(chunks) == 1:
        return summarize_text(chunks[0])
    partial_summaries = [summarize_text(c) for c in chunks]
    combined = "\n\n".join(partial_summaries)


    return summarize_text(combined)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Summarize a text file or raw text')
    parser.add_argument('--file', '-f', help='Path to a text file to summarize')
    parser.add_argument('--text', '-t', help='Raw text to summarize (wrap in quotes)')
    args = parser.parse_args()


    if args.file:
        with open(args.file, 'r', encoding='utf-8') as fh:
            txt = fh.read()
    elif args.text:
        txt = args.text
    else:
        print('Provide --file path or --text \"your text\"')
        exit(1)


    summary = summarize_input(txt)
    print('\\n=== Summary ===\\n')
    print(summary)
