"""Simple code formatter helper used by the code-reviewer skill."""


def normalize_whitespace(text: str) -> str:
    """Collapse multiple blank lines into one."""
    lines = text.splitlines()
    result = []
    prev_blank = False
    for line in lines:
        is_blank = not line.strip()
        if is_blank and prev_blank:
            continue
        result.append(line)
        prev_blank = is_blank
    return "\n".join(result)
