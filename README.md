# era5_downloader

A simple Python package to download ERA5 reanalysis data using the CDS API.

## Installation

```bash
pip install git+https://github.com/yourusername/era5_downloader.git
```

Or clone and install locally:

```bash
git clone https://github.com/yourusername/era5_downloader.git
cd era5_downloader
pip install -e .
```

## Usage

```python
from era5_downloader import download_era5_data

download_era5_data(
    variables=[
        "10m_u_component_of_wind",
        "10m_v_component_of_wind",
        "significant_height_of_total_swell",
        "mean_direction_of_total_swell",
    ],
    years=range(1975, 1976),
    area=[13.5, -81.5, 13.2, -81.2],  # North, West, South, East
    output_root=r'P:\01\05_data\05_ERA5'
)
```
