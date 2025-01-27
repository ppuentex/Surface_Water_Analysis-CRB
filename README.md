# Inundated Area Trend Analysis in the Colorado River Basin

## Citation 
By using this code or dataset in your research or projects, please cite the following publication: 

> *Citation Coming Soon*

## Overview 
This repository contains the code, regional data, and additional resources supporting the research described in the citation above. It provides the tools for analyzing and processing the [Global Surface Water Dataset](https://global-surface-water.appspot.com/) focusing on the Colorado River Basin (CRB) and surface water area changes over time. 

## Getting Started

### Prerequisites
**Install Poetry** \
Poetry is required to manage dependencies in this project. If you don't have Poetry installed already, follow the instructions at [Poetry Installation](https://python-poetry.org/docs/#installing-with-the-official-installer). 

### Instructions

1. Clone this repository to your local machine in the terminal: 
```
git clone git@github.com:ppuentex/Surface_Water_Analysis-CRB.git 
```

2. Navigate to the repository directory: 
```
cd <your_local_folder>/Surface_Water_Analysis-CRB
```

3. Create and activate virtual environment: 
    ```
    conda create -n <env_name>
    conda activate <env_name>
    ```

4. Install dependencies with Poetry: 
    Run the following command to populate your environment with all the necessary packages: 
   ```
   poetry install
   ```
   This will download all dependencies specified in `pyproject.toml` file.  


> **Note:** 
> To add more packages to the environment, use Poetry's `add` command. For example: 
> ```poetry add numpy ``` 


## Repository Overview
This repository includes the following structure. 
``` 
Surface_Water_Analysis-CRB/
├── README.md                   
├── LICENSE 
├── pyproject.toml 
├── poetry.lock
├── .gitignore
├── data/
│   ├── README.md
│   ├── analysis-data/
│   │   ├── water_type_transitions_92_19.csv  
│   │   ├── water_type_transitions_02_19.csv  
│   │   └── zonal_statistics.csv
│   ├── processed-data/
│   │	├── Yearly_Water_History_CRB/
│   │   │   ├── 1984_CRB.tif...
│   │   │   ├── ...2002_CRB.tif...
│   │   │   └── ...2021_CRB.tif
│   │   ├── Shapefiles/
│   │   │   ├── CRB_huc4.shp
│   │   │   ├── CRB_states.shp
│   │   │   ├── CRB_major_rivers.shp
│   │   │   └── CRB_urban_cities.shp
│   │   ├── output_mode_1992_1994.tif
│   │   ├── output_mode_2002_2004.tif
│   │   ├── output_mode_2019_2021.tif
│   │   ├── CRB_urban_buildup.tif
│   │   └── CRB_PDSI_84-21.csv
│   └── data_previews.ipynb
├── codes/
│   ├── pre-processing.ipynb
│   ├── analysis.ipynb
│   └── utils/
│       ├── __init__.py
│       └── helper-functions.py
└── results/
    ├── README.md
    ├── figures/
    │   ├── trend-analysis-figure1.png
    │   └── summary-statistics-figure2.png
    └── generate-figures.ipynb 