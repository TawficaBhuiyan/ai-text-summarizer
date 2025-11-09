from src.summarizer import summarize_text


def test_short_summary():
    text = (
        "Python is an interpreted, high-level programming language. It emphasizes code readability and has a large standard library.\n\n"
        "Many developers use Python for web development, data analysis, scripting, and automation."
    )
    s = summarize_text(text)
    assert isinstance(s, str)
    assert len(s) > 0
