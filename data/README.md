
This folder contains all datasets used in the study. 

Instructions on how the data was processed or analyzed is in the  `Codes/` folder. See `pre-processing.ipynb` for  `processed-data/` and `analysis.ipynb` for `analysis-data/`. 

1. Contents
- `/processed-data` &rarr; this folder contains shapefiles, yearly water history for the Colorado River Basin, PDSI values for the Upper, Lower, and whole Basin, urbanization buildup, and mode raster files for the periods 1992-1994, 2002-2004, and 2019-2021
- `/analysis-data` &rarr; this folder contains the zonal statistics for each HUC for every year, the individual dry and wet transitions per HUC for two periods, and the transitions occurring in urbanziaiton

2. File Descriptions  
    **Processed Data**
    1. `/yearly_water_history-CRB/`
        - Files in this folder contains the water history for the Coloraod River Basin from 1984 to 2021 
        - Each file contains classifications for surface water; 1:not water, 2: seasonal water , 3: permanent water , 4: no observation
    2. `/shapefiles/` &rarr; when working with shapefiles, all associated files are essential (ie. `.cpg`, `.dbf`, `.prj`, and `.shx`) even though the code only references or calls the `.shp`. 
        - `CRB_HUC4.shp` &rarr; file contains the geometry for the all 14 HUC4s in the CRB, within stateline boundary 
        - `CRB_major_rivers.shp` &rarr; file contains the geometry for the Colorado, Gila, Verde, Salt, Little Colorado, San Juan, and Green River 
        - `CRB_states.shp` &rarr; file contains the geometry for the state of Nevada, California, Utah, Arizona, Wyoming, Colorado, and New Mexico
        - `CRB_urban_cities.shp` &rarr; file contains the geometry for the major urban hubs in the CRB -- Tucson, Yuma, Phoenix, Flagstaff, Las Vegas, Gunnison, and Grand Junction 
        - `Lake_Mead.shp` &rarr; file contains the geometry of Lake Mead
        - `Lake_Powell.shp` &rarr; file contains the geometry of Lake Powell
        
        *Note: Make sure all associated files are in the same folder or the .shp file will not open.*
    3. `CRB_urban_buildup.tif` &rarr; this file is the build-up urban land changes in 2000 - 2020, with classifications 2: build-up expansion (new urbanization developement within 2000-2020), 1: build-up stable (urbanization prior to 2000)
    4. `CRB_PDSI_84-21.csv` &rarr; this file contains yearly averages for the upper and lower CRB, and the aggregated averages for the CRB 
    5. `output_mode_[period].tif` where `[period]` is `1992_1994`, `2002_2004`, and `2019_2021` are the raster file outputs on calculating the pixel-wise mode within the time period. 

    **Analysis Data**
    1. Zonal_statistics.csv
        - this file contains the statistics of for each year, and each HUC (i.e. year, huc4, inundated_permanent_area, etc.)
    2. HUC4_transition-92_21.csv 
        - this file contains the statistics for each HUC on the transitions from permanent to seasonal inundated water, etc