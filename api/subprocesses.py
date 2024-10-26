
# sudo tippecanoe -z16 -o ./data/result.mbtiles ./data/processed/overlay_result4.geojson --force

import subprocess
import pathlib

# Run a command, for example, 'ls' to list directory contents (on Unix)
# result = subprocess.run(["ls", "-l"], capture_output=True, text=True)

# # Check if the command was successful
# if result.returncode == 0:
#     print("Command Output:")
#     print(result.stdout)
# else:
#     print("Error:")
#     print(result.stderr)

# TODO: put this into config
PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent

def run_subprocess(filename: str):
    input_path = PROJECT_ROOT / 'data' / 'geojsons' / f'{filename}.geojson'

    if not input_path.exists():
        raise FileNotFoundError(f'Geojson on path {input_path} does not exist.')

    output_path = PROJECT_ROOT / 'data' / 'tiles' / f'{filename}.mbtiles'

    command = [
        "sudo",
        "tippecanoe",
        "-z16",
        "-o",
        output_path,
        input_path,
        "--force"
    ]

    subprocess_result = subprocess.run(command, capture_output=True, text=True)


    if subprocess_result.returncode == 0:
        print("Command Output:")
        print(subprocess_result.stdout)
    else:
        print("Error:")
        print(subprocess_result.stderr)

    # return input_path


# print(.exists())
# print()
run_subprocess('parcels_c_ruzinov')