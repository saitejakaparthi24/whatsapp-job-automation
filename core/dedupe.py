import hashlib

def hash_job(job):
    key = job["company"] + job["title"] + job["url"]
    return hashlib.sha256(key.encode()).hexdigest()
