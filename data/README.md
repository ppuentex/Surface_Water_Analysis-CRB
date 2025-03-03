
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
    1. `huc4_zonal_stats.csv` &rarr; this file contains the statistics of for each year, and each HUC 
        Columns: 
        - year, huc4, huc_name
        - count_total = number of pixels that are both permanent and seasonal 
        - count_permaent = number of pixels that are permanent 
        - count_seasonal = number of pixel that are seasonal
        - count_nowater = number of pixels that are no water 
        - count_no_obs = number of pixels that are no observation
        - count_huc = number of pixels total in the HUC regardless of classification 
        - area_total_water = total water area in km 
        - area_permanent = permanent water area in km 
        - area_seasonal = seasonal water area in km
        - area_nowater = no water area in km 
    2. `transitions_urbanization_92_19.csv` &rarr; this file contains the statistics for each HUC on the wet and dry transitions that occurred in urban areas 
        Columns: 
        - huc4 = huc4 id number 
        - HUC_count = number of pixels total in the HUC regardless of classification 
        - gained_urban_area = total urban area that was gained in km 
        - stable_urban_area = total urban area that was stable in km 
        - dry_transition_area = total dry transition area in km (seasonal &rarr; no water, permanent &rarr; no water, permanent &rarr; seasonal)
        - wet_transition_area = total wet transition area in km (seasonal &rarr; permanent, no water &rarr; seasonal, no water &rarr; permanent)
        - stable_urban_dry_area = dry transition that occurred in stable urban area (km)
        - gained_urban_dry_area = dry transition that occurred in gained urban area (km)
        - stable_urban_wet_area = wet transition that occurred in stable urban area (km)
        - gained_urban_wet_area = wet transition that occurred in gained urban area (km)
    
    3. `water_type_transitions_02_19.csv` & `water_type_transitions_92_19.csv` these files contains the statistics for each HUC on the individual wet and dry transitions. The period 1 is 2002-04 or 1992-94 and period 2 is 2019-21 for both files. 
        Columns: 
        - huc4 = huc4 id number 
        - permanent_area_period1 & permanent_area_period2 = permanent water area in period 1 and period 2 respectively
        - seasonal_area_period1 & seasonal_area_period2 = seasonal water area in period 1 and period 2 respectively
        - nowater_area_period1 & nowater_area_period2 = no water area in period 1 and period 2 respectively
        - perm_nowater_trans_area = area that was permanent in period 1 and changed to no water in period 2 
        - perm_seasonal_trans_area = area that was permanent in period 1 and changed to seasonal in period 2 
        - seasonal_nowater_trans_area = area that was seasonal in period 1 and changed to no water in period 2 
        - seaonal_perm_trans_area = area that was seasonal in period 1 and changed to permanent in period 2 
        - nowater_seasonal_trans_area = area that was no water in period 1 and changed to seasonal in period 2 
        - nowater_perm_trans_area = area that was no water in period 1 and changed to permanent in period 2 
        - dry_transition_area = sum of perm_nowater_trans_area, perm_seasonal_trans_area, and seasonal_nowater_trans_area
        - wet_transition_area = sum of seaonal_perm_trans_area, nowater_seasonal_trans_area, and nowater_perm_trans_area
        - total_area_period1 & total_area_period2 = sum of seasonal and permanent water in period 1 and period 2 respectively