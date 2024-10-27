import contextlib
import uuid
import asyncio

from fastapi import FastAPI, Request, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware

from .subprocesses import run_tc_subprocess
from .config import Status
from .utils.overlay import overlay_layers

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins; for production, restrict this to specific origins
    allow_credentials=True,
    allow_methods=["POST", "GET"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

process_status = {}

@app.post("/compute-layers/")
async def create_item(request: Request, background_tasks: BackgroundTasks):
    pad_config = await request.json()  # Get raw JSON data
    # Process the data as needed
    task_id = str(uuid.uuid4())

    background_tasks.add_task(overlay_layers, pad_config, task_id, process_status)
    # background_tasks.add_task(run_tc_subprocess, 'parcels_c_ruzinov', process_status)
    
    return {"computation_task_id": task_id, "status": "Computation task started."}

@app.get("/task-status/{task_id}")
async def get_task_status(task_id: str):
    # Return the current status of the task
    status, message = process_status.get(task_id, (Status.FAILED, f"Task {task_id} not found"))

    return {"task_id": task_id, "status": status, 'message': message}

