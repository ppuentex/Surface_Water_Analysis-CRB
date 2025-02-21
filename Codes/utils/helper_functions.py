import rasterio 
import numpy as np 
from scipy import stats 
import pandas as pd 
from rasterio.features import geometry_mask
from shapely.geometry import mapping 

class RasterCalculator: 
    def __init__(self, input_files, output_file):
        ''' 
        Initialize the calculator with input and output file paths. 

        Parameters: 
            input_files (list of str): Paths to input .tif files. 
            output_file (str): Path to the output .tif file.
        '''
        self.input_files = input_files 
        self.output_file = output_file

    def calculate_mode(self): 
        '''
        Calculate the mode across input .tif files and save the result.
        '''
        # Open and read all raster files 
        arrays = []
        for file in self.input_files:
            with rasterio.open(file) as src:
                arrays.append(src.read(1)) #read the first band (specific to .tif file)
        
        #stack arrays along a new axis to calculate the mode for each pixel 
        stacked_arrays = np.stack(arrays, axis = -1)
        result = stats.mode(stacked_arrays, axis=2, keepdims=True)
        mode_array = result.mode.reshape(result.mode.shape[0], result.mode.shape[1])

        #save the mode array as a new GeoTiff file 
        self._save_output(mode_array)
    
    def _save_output(self, mode_array):
        '''
        Save the mode array to the output GeoTiff file. 

        Parameters: 
            mode_array (numpy.ndarray): array of mode values
        '''

        #Use the first input file to copy the metadata 
        with rasterio.open(self.input_files[0]) as src:
            profile = src.meta.copy()
        
        #update metadata 
        profile.update({'count': 1}) #specify the number of bands
        profile.update({"compress": "lzw"}) 

        #write 
        with rasterio.open(self.output_file, 'w', **profile) as dst:
            dst.write(mode_array, 1) #write data into first band

        print(f"Mode calculation complete. Output saved to {self.output_file}")

class WaterTransitionAnalyzer: 
    def __init__(self, pixel_size = 30):
        '''Initialize with pixel size (default is 30m for Landsat).'''
        self.pixel_area = pixel_size**2  # Convert to square meters
        self.km_scale = 1e6  # Convert m² to km²
    
    def load_raster(self, path):
        '''Loads a raster and returns the data array and transform.'''
        with rasterio.open(path) as src:
            return src.read(1), src.transform
        
    def raster_shapes(self, shapes, out_shape, transform):
        '''Rasterize geometries into an array using given transform.'''
        raster = np.zeros(out_shape, dtype=np.uint16)
        for geom, value in shapes: 
            mask = geometry_mask([geom], transform=transform, invert=True, out_shape=out_shape)
            raster[mask] = value
        return raster
    
    def calculate_transitions(self, mode_path1, mode_path2, huc_raster): 
        '''Calculate water transitions between two mode rasters for each huc4'''
        period1, _ = self.load_raster(mode_path1)
        period2, _ = self.load_raster(mode_path2)

        #define water pixel labels 
        nowater_label = 1 
        seasonal_label = 2
        permanent_label = 3 
        
        #create mask for water types
        masks_period1 = {label: (period1 == label) for label in [permanent_label, seasonal_label, nowater_label]}
        masks_period2 = {label: (period2 == label) for label in [permanent_label, seasonal_label, nowater_label]}

        # Define transitions
        transitions = {
            'perm_nowater': masks_period1[permanent_label] & (period2 == nowater_label),
            'perm_seasonal': masks_period1[permanent_label] & (period2 == seasonal_label),
            'seasonal_nowater': masks_period1[seasonal_label] & (period2 == nowater_label),
            'seasonal_perm': masks_period1[seasonal_label] & (period2 == permanent_label),
            'nowater_seasonal': masks_period1[nowater_label] & (period2 == seasonal_label),
            'nowater_perm': masks_period1[nowater_label] & (period2 == permanent_label),
        }

        # Get unique HUC labels
        unique_labels = np.unique(huc_raster)
        unique_labels = unique_labels[unique_labels != 0]  # Exclude background (0)

        # Collect transition results
        trans_results = []
        for huc_id in unique_labels:
            huc_mask = (huc_raster == huc_id)

            # Calculate area of each water type in both periods
            area_period1 = {key: np.sum(huc_mask & masks_period1[key]) * self.pixel_area / self.km_scale for key in masks_period1}
            area_period2 = {key: np.sum(huc_mask & masks_period2[key]) * self.pixel_area / self.km_scale for key in masks_period2}

            # Calculate transition areas
            transition_areas = {key: np.sum(huc_mask & transitions[key]) * self.pixel_area / self.km_scale for key in transitions}

            trans_results.append({
                'huc4': str(huc_id),
                **{f"{key}_area_period1": val for key, val in area_period1.items()},
                **{f"{key}_area_period2": val for key, val in area_period2.items()},
                **{f"{key}_trans_area": val for key, val in transition_areas.items()},
                'dry_transition_area': transition_areas['perm_nowater'] + transition_areas['perm_seasonal'] + transition_areas['seasonal_nowater'],
                'wet_transition_area': transition_areas['seasonal_perm'] + transition_areas['nowater_seasonal'] + transition_areas['nowater_perm']
            })

            print(f"Processed HUC {huc_id}")

        return pd.DataFrame(trans_results)
    
    def calculate_transition_urban(self, mode_path1, mode_path2, urban_path, huc_raster):
        '''Analyzes water transitions in urban and non-urban areas within each huc4 subbasin'''
        water_period1,_ = self.load_raster(mode_path1)
        water_period2,_ = self.load_raster(mode_path2)
        land_class,_ = self.load_raster(urban_path)

        #define water pixel labels 
        nowater_label = 1 
        seasonal_label = 2
        permanent_label = 3 

        # Create urban masks
        stable_urban_mask = (land_class == 2)
        gain_urban_mask = (land_class == 1)

        # Create transition masks
        trans_masks = {
            "perm_nowater": (water_period1 == permanent_label) & (water_period2 == nowater_label),
            "perm_seasonal": (water_period1 == permanent_label) & (water_period2 == seasonal_label),
            "seasonal_nowater": (water_period1 == seasonal_label) & (water_period2 == nowater_label),
            "seasonal_perm": (water_period1 == seasonal_label) & (water_period2 == permanent_label),
            "nowater_seasonal": (water_period1 == nowater_label) & (water_period2 == seasonal_label),
            "nowater_perm": (water_period1 == nowater_label) & (water_period2 == permanent_label),
        }

        # Get unique HUC labels
        unique_labels = np.unique(huc_raster)
        unique_labels = unique_labels[unique_labels != 0]  # Exclude background (0)
        trans_results = []
        for huc_id in unique_labels:
            huc_mask = (huc_raster == huc_id)
            huc_count = np.sum(huc_mask)

            gained_urban = np.sum(huc_mask & gain_urban_mask)
            stable_urban = np.sum(huc_mask & stable_urban_mask)

            percent_urbanization = ((gained_urban + stable_urban) / huc_count) * 100

            # Calculate transition areas
            dry_area = sum(np.sum(huc_mask & trans_masks[key]) for key in ["perm_nowater", "perm_seasonal", "seasonal_nowater"])
            wet_area = sum(np.sum(huc_mask & trans_masks[key]) for key in ["seasonal_perm", "nowater_seasonal", "nowater_perm"])

            total_dry_transition_area = (dry_area * self.pixel_area) / self.km_scale
            total_wet_transition_area = (wet_area * self.pixel_area) / self.km_scale

            #urban specific water transitions 
            stable_dry_area = sum(np.sum(huc_mask & stable_urban_mask & trans_masks[key]) for key in ["perm_seasonal", "perm_nowater", "seasonal_nowater"])
            gained_dry_area = sum(np.sum(huc_mask & gain_urban_mask & trans_masks[key]) for key in ["perm_seasonal", "perm_nowater", "seasonal_nowater"])

            stable_wet_area = sum(np.sum(huc_mask & stable_urban_mask & trans_masks[key]) for key in ["seasonal_perm", "nowater_perm", "nowater_seasonal"])
            gained_wet_area = sum(np.sum(huc_mask & gain_urban_mask & trans_masks[key]) for key in ["seasonal_perm", "nowater_perm", "nowater_seasonal"])

            # Store results
            trans_results.append({
                'huc4': huc_id,
                'HUC_count': huc_count,
                'gained_urban_area': (gained_urban * self.pixel_area) / self.km_scale,
                'stable_urban_area': (stable_urban * self.pixel_area) / self.km_scale,
                'dry_transition_area': total_dry_transition_area,
                'wet_transition_area': total_wet_transition_area,
                'stable_urban_dry_area': (stable_dry_area * self.pixel_area) / self.km_scale,
                'gained_urban_dry_area': (gained_dry_area * self.pixel_area) / self.km_scale,
                'stable_urban_wet_area': (stable_wet_area * self.pixel_area) / self.km_scale,
                'gained_urban_wet_area': (gained_wet_area * self.pixel_area) / self.km_scale,
                'urbanization_percent': percent_urbanization
            })
            print(f"Processed HUC {huc_id}")
        
        return pd.DataFrame(trans_results)