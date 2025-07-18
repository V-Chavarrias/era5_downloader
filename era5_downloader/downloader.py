import cdsapi
from datetime import datetime
import os
import subprocess

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
    # Print the version of this file
    print(f"Running {os.path.basename(__file__)} (last modified: {datetime.fromtimestamp(os.path.getmtime(__file__))})")
    
    # Print Git commit hash if available
    try:
        repo_dir = os.path.dirname(os.path.abspath(__file__))
        git_hash = subprocess.check_output(
            ["git", "-C", repo_dir, "rev-parse", "--short", "HEAD"],
            stderr=subprocess.DEVNULL
        ).decode().strip()
        print(f"Git commit hash: {git_hash}")
    except Exception:
        print("Git commit hash: unavailable")

    c = cdsapi.Client()
    os.makedirs(output_root, exist_ok=True)

    for variable in variables:
        
        variable_folder = os.path.join(output_root, variable)
        os.makedirs(variable_folder, exist_ok=True)

        for year in years:

            bdate = str(year)
            # Ensure the date is in the correct format
            if len(bdate) != 4:
                raise ValueError(f"Year {year} is not in the correct format (YYYY).")
            
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]: get variable {variable} from {bdate}")
            output_file = os.path.join(variable_folder, f"{bdate}_{variable}.nc")

            #if the file already exists, skip downloading
            if os.path.exists(output_file):
                print(f"File {output_file} already exists, skipping download.")
                continue

            # Download data from CDS API
            print(f"Downloading {variable} data for {bdate} to {output_file}")
            
            c.retrieve(
                'reanalysis-era5-single-levels',
                {
                    "product_type": "reanalysis",
                    "variable": variable,
                    "year": bdate,
                    "month": [f"{m:02d}" for m in range(1, 13)],
                    "day": [f"{d:02d}" for d in range(1, 32)],
                    "time": [f"{h:02d}:00" for h in range(24)],
                    "format": "netcdf",
                    "area": area,
                },
                output_file,
            )
