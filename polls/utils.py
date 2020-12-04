import hashlib


def gen_md5_digest(content):
    return hashlib.md5(content.encode()).hexdigest()
