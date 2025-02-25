# Inundated Area Trend Analysis in the Colorado River Basin

## Citation 
By using this code or dataset in your research or projects, please cite the following publication: 

> *Puente, P., Condon, L. E., Long-term losses in surface water area in the Colorado River Basin, Environmental Research Letters (in consideration)*

## Overview 
This repository contains the code, regional data, and additional resources supporting the research described in the citation above. It provides the tools for analyzing and processing the [Global Surface Water Dataset](https://global-surface-water.appspot.com/) focusing on the Colorado River Basin (CRB) and surface water area changes over time. 

## Getting Started

### Instructions

1. Clone this repository to your local machine in the terminal: 
```
git clone git@github.com:ppuentex/Surface_Water_Analysis-CRB.git 
```

2. Navigate to the repository directory: 
```
cd <your_local_folder>/Surface_Water_Analysis-CRB
```

3. Create new virtual environment: 
```
python3 -m venv surface-water-env
```
This will create a new folder within the `Surface_Water_Analysis-CRB` directory.

4. Set up a virtual environment: 
```
source surface-water-env/bin/activate #for macOS/Linex \
venv\Scripts\activate  #For Windows
```
Make sure to add `/surface-water-env` to `.gitignore`. 

5. Install dependencies:
```
pip install -r requirements.txt
``` 
This will download all dependencies and populate the virtual environment. 


## Repository Overview
This repository includes the following structure. 
``` 
Surface_Water_Analysis-CRB/
├── README.md                   
├── LICENSE 
├── requirements.txt
├── .gitignore
├── data/
│   ├── README.md
│   ├── analysis-data/
│   │   ├── water_type_transitions_92_19.csv  
│   │   ├── water_type_transitions_02_19.csv  
│   │   ├── transitions_urbanization_92_19.csv  
│   │   └── huc4_zonal_stats.csv
│   ├── processed-data/
│   │	├── Yearly_Water_History_CRB/
│   │   │   ├── 1984_CRB.tif...
│   │   │   ├── ...2002_CRB.tif...
│   │   │   └── ...2021_CRB.tif
│   │   ├── Shapefiles/
│   │   │   ├── CRB_HUC4.shp
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
    │   ├── Basin-figure1a.jpg
    │   ├── ...
    │   └── transition_urban_areas-figure6.jpg
    └── generate-figures.ipynb 