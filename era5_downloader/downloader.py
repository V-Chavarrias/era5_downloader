import cdsapi
from datetime import datetime
import os

def download_era5_data(
    variables,
    years,
    area,
    output_root,
):
    """
    Download ERA5 single-level reanalysis data from CDS API.

    Args:
        variables (list of str): List of variable names to download.
        years (iterable): Years to include (e.g. range(1975, 1976)).
        area (list): Geographic area in [N, W, S, E] format.
        output_root (str): Root directory to save downloaded files.
    """
    c = cdsapi.Client()
    os.makedirs(output_root, exist_ok=True)

    for year in years:
        bdate = str(year)
        year_folder = os.path.join(output_root, bdate)
        os.makedirs(year_folder, exist_ok=True)

        for variable in variables:
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]: get variable {variable} from {bdate}")
            variable_folder = os.path.join(year_folder, variable)
            os.makedirs(variable_folder, exist_ok=True)
            output_file = os.path.join(variable_folder, f"{bdate}_{variable}.nc")

            c.retrieve(
                'reanalysis-era5-single-levels',
                {
                    "product_type": ["reanalysis"],
                    'variable': [variable],
                    'year': [bdate],
                    'month': [f'{m:02d}' for m in range(1, 13)],
                    'day': [f'{d:02d}' for d in range(1, 32)],
                    "data_format": "netcdf",
                    "download_format": "unarchived",
                    "area": area,
                },
                output_file,
            )
