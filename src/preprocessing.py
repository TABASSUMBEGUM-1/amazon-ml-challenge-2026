import re
import unicodedata


def normalize_text(text):
    """Basic text normalization."""
    if text is None:
        return ""

    text = str(text).lower().strip()

    # Normalize unicode characters
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))

    # Replace punctuation with spaces
    text = re.sub(r"[^a-z0-9\s]", " ", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text


def normalize_name(name):
    """Normalize business names."""
    return normalize_text(name)


def normalize_address(address):
    """Normalize business addresses."""
    return normalize_text(address)