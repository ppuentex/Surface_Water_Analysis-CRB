import rasterio 
import numpy as np 
from scipy import stats 

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