# Surface_Water_Analysis-CRB
GitHub repository for "paper title": inundated area trend analysis in the Colorado River Basin. 

## Getting Started
- Using Poetry to create virtual environment. 

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
│   │   │   ├── 1984.tif...
│   │   │   ├── ...2002.tif...
│   │   │   └── ...2021.tif
│   │   ├── Shapefiles/
│   │   │   ├── CRB_huc4.shp
│   │   │   ├── CRB_states.shp
│   │   │   ├── CRB_major_rivers.shp
│   │   │   └── CRB_urban_cities.shp
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