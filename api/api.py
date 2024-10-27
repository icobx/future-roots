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

# task_queue = asyncio.Queue()

# processed entire bratislava
process_status = {}

@app.post("/compute-layers/")
async def create_item(request: Request, background_tasks: BackgroundTasks):
    pad_config = await request.json()  # Get raw JSON data
    # Process the data as needed
    task_id = str(uuid.uuid4())

    # overlay_coroutine = asyncio.to_thread(overlay_layers, pad_config, task_id, process_status)
    # await asyncio.create_task(overlay_layers(pad_config, task_id, process_status))
    background_tasks.add_task(overlay_layers, pad_config, task_id, process_status)
    # background_tasks.add_task(run_tc_subprocess, 'parcels_c_ruzinov', process_status)
    
    return {"computation_task_id": task_id, "status": "Computation task started."}

@app.get("/task-status/{task_id}")
async def get_task_status(task_id: str):
    # Return the current status of the task
    status, message = process_status.get(task_id, (Status.FAILED, f"Task {task_id} not found"))

    return {"task_id": task_id, "status": status, 'message': message}

# async def long_running_task(task_id: str, data: dict):
#     try:
#         # Simulate long processing with multiple stages
#         for i in range(3):
#             await asyncio.sleep(5)  # Simulate work
#             process_status[task_id] = f"In progress: stage {i + 1}/3"
        
#         # Mark task as completed
#         process_status[task_id] = "Completed"
    
#     except Exception as e:
#         # In case of error, set task status to failed
#         process_status[task_id] = f"Failed: {str(e)}"



# import src.baseline.baseline_client as bc
# import src.models.models as models
# from src.config import Config

# baseline_client = {}


# @contextlib.asynccontextmanager
# async def baseline_client_init_lifespan(app: fastapi.FastAPI):
#     """Baseline client initialization lifespan context manager.

#     Args:
#         app: API application object.
#     """
#     baseline_client["bc"] = bc.BaselineClient()

#     yield

#     baseline_client["bc"].db.close_connection()
#     baseline_client.clear()


# app = fastapi.FastAPI(
#     title="Baseline API",
#     version="0.0.1",
#     description=Config.api_description,
#     lifespan=baseline_client_init_lifespan,
# )


# @app.post("/baseline/", response_model=models.BaselineResponseBody)
# async def baseline(
#     request_body: models.BaselineRequestBody,
# ) -> models.BaselineResponseBody:
#     """Baseline API POST endopoint.

#     Args:
#         request_body: Request body model.

#     Raises:
#         fastapi.HTTPException: If any exception is raised during the baseline
#             calculation.

#     Returns:
#         Response body model.
#     """
#     try:
#         response = baseline_client["bc"].calculate_baseline(request_body)
#     except Exception as e:
#         raise fastapi.HTTPException(
#             status_code=422,
#             detail={
#                 "type": str(type(e)),
#                 "msg": str(e),
#                 "input": request_body.model_dump(),
#             },
#         )

#     return response
