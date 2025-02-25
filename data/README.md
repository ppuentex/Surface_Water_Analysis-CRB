## Processed and Analysis Data

All datasets are descibed below, see `link to notebook (of showcasing datasets)`:

Instructions on how the data was processed or analyzed is in the  `Codes/` folder. See `pre-processing.ipynb` for  `processed-data/` and `analysis.ipynb` for `analysis-data/`. 

This folder contains all datasets for this study: 
### Processed 
1. CRB-Surface-Water
    - This folder contains the Global Surface Water, yearly water history tif files ONLY for the Coloraod River Basin from 1984 to 2021 
    - Each file contains classifications for surface water; 1: , 2: , 3: , 4: 
2. CRB-Urban-Buildup.tif 
    - This file is the build-up urban land changes in 2000 - 2021
    - This file contains classifications for built-up; 225: ,226: 
3. CRB-PDSI 
    - upper PDSI, lower PDSI, aggregated PDSI
4. Shapefiles
    - Watershed boundaries - CRB statelines only (HUCs), Western States, Main Cities, Main Rivers

### Analysis  
1. Zonal_statistics.csv
    - this file contains the statistics of for each year, and each HUC (i.e. year, huc4, inundated_permanent_area, etc.)
2. HUC4_transition-92_21.csv 
    - this file contains the statistics for each HUC on the transitions from permanent to seasonal inundated water, etc