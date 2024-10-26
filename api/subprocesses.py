import asyncio

from .config import PROJECT_ROOT, Status

# sudo tippecanoe -z16 -o ./data/result.mbtiles ./data/processed/overlay_result4.geojson --force
# sudo docker run --rm -it -v $(pwd):/data -p 8080:8080 maptiler/tileserver-gl --config /data/tileserver_config.json

async def run_tc_subprocess(filename: str, process_status: dict[tuple[Status | str]]):
    process_status[filename] = (Status.STARTED, '')

    input_path = PROJECT_ROOT / 'data' / 'geojsons' / f'{filename}.geojson'

    if not input_path.exists():
        process_status[filename] = (Status.FAILED, f'Geojson on path {input_path} does not exist.')
        return 
    
    output_path = PROJECT_ROOT / 'data' / 'tiles' / f'{filename}.mbtiles'

    command = [
        # "sudo",
        "tippecanoe",
        "-z16",
        "-o",
        output_path,
        input_path,
        "--force"
    ]

    process = await asyncio.create_subprocess_exec(
        *command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    while process.returncode is None:
        process_status[filename] = (Status.RUNNING, '')
        await asyncio.sleep(2)

    _, stderr = await process.communicate()
    if process.returncode == 0:
        process_status[filename] = (Status.COMPLETED, f'Tiles for task {filename} calculated.')
    else:
        process_status[filename] = (Status.FAILED, stderr.decode())

    return output_path
# asyncio.cre
# print(asyncio.run(run_tc_subprocess('parcels_c_ruzinov', {})))
# await run_subprocess('parcels_c_ruzinov')