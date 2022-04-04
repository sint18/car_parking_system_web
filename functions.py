import hashlib


def get_hash(text):
    if text:
        res = hashlib.sha256(text.encode()).hexdigest()
        return res
