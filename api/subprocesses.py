
# sudo tippecanoe -z16 -o ./data/result.mbtiles ./data/processed/overlay_result4.geojson --force

import subprocess
import pathlib

from config import PROJECT_ROOT

# sudo docker run --rm -it -v $(pwd):/data -p 8080:8080 maptiler/tileserver-gl --config /data/tileserver_config.json


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

run_subprocess('parcels_c_ruzinov')