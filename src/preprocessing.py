import re
import base64

mots_suspects = ["ignore", "bypass", "jailbreak", "override",
                 "forget", "pretend", "disregard", "reveal",
                 "system", "instruction", "prompt"]

def clean_text(text):
    text = str(text)
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-z0-9\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def has_base64(text):
    try:
        pattern = r'[A-Za-z0-9+/]{20,}={0,2}'
        matches = re.findall(pattern, str(text))
        for m in matches:
            base64.b64decode(m)
            return 1
    except:
        pass
    return 0

def count_suspicious(text):
    text = str(text).lower()
    return sum(1 for mot in mots_suspects if mot in text)