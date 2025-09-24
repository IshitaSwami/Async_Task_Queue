from fastapi import FastAPI, BackgroundTasks
from app.queue import task_queue, redis_conn
from app.tasks import send_email
from rq.job import Job

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Async Task API is running"}

@app.post("/send-email/")
async def trigger_email(background_tasks: BackgroundTasks, recipient: str):
    job = task_queue.enqueue(send_email, recipient)
    return {"job_id": job.get_id(), "status": "Email task queued", "recipient": recipient}

@app.get("/status/{job_id}")
async def get_status(job_id: str):
    try:
        job = Job.fetch(job_id, connection=redis_conn)
        return {"job_id": job_id, "status": job.get_status()}
    except Exception as e:
        return {"error": str(e)}

