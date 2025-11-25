from scrapers.greenhouse import fetch_greenhouse_jobs
from core.database import get_conn, init_db
from core.dedupe import hash_job
from whatsapp.sender import send_whatsapp_message

def run():
    init_db()

    all_jobs = fetch_greenhouse_jobs()

    conn = get_conn()
    new_jobs = []

    for job in all_jobs:
        job_hash = hash_job(job)

        q = conn.execute("SELECT 1 FROM jobs WHERE id=?", (job_hash,))
        if q.fetchone() is None:
            conn.execute("INSERT INTO jobs VALUES (?, ?, ?, ?, ?)", (
                job_hash, job['title'], job['company'], job['url'], str(job['posted_at'])
            ))
            conn.commit()
            new_jobs.append(job)

    for job in new_jobs[:20]:
        msg = f"{job['title']} at {job['company']}\nApply: {job['url']}"
        send_whatsapp_message(msg)

if __name__ == "__main__":
    run()
