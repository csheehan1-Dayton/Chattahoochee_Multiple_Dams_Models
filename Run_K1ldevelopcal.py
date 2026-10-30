#%% Run K1ldevelopcal
# **Author**: Chris Sheehan

#%% Import libraries

# Print status
print('Importing libraries...')

# Import
import os
import os.path
from os import path
import sys
if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")
warnings.filterwarnings("ignore")
import inspect
import numpy as np
from numpy import nan
from matplotlib import pyplot as plt
from matplotlib.ticker import ScalarFormatter, FuncFormatter
import matplotlib.colors as mcolors
from matplotlib.patches import Rectangle
from collections import defaultdict, deque
from landlab import imshowhs_grid
from landlab.components import PriorityFloodFlowRouter, SinkFillerBarnes, SpaceLargeScaleEroder
from landlab.io.esri_ascii import read_esri_ascii, write_esri_ascii
import EET

# Section break
print(' ')

#%% Set directories

# Print status
print('Setting directories...')

# Set directories
script_directory = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
project_directory = script_directory.replace('\\5_runs\\run_k1ldevelopcal', '')
export_directory = script_directory + '/'

# Create directories
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal')
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/Overview_Map') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/Overview_Map') 
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/topographic__elevation_Map') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/topographic__elevation_Map')     
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/topographic__elevation_Map/Full') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/topographic__elevation_Map/Full')    
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/topographic__elevation_Map/Zone_1') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/topographic__elevation_Map/Zone_1')  
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/topographic__elevation_Map/Zone_2') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/topographic__elevation_Map/Zone_2')  
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/topographic__elevation_Map/Zone_3') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/topographic__elevation_Map/Zone_3')  
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/topographic__elevation_Map/Zone_4') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/topographic__elevation_Map/Zone_4')  
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/topographic__elevation_Map/Zone_5') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/topographic__elevation_Map/Zone_5')  
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/topographic__elevation_timeseries') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/topographic__elevation_timeseries')  
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/dbedelevdt_Map') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/dbedelevdt_Map')     
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/dbedelevdt_Map/Full') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/dbedelevdt_Map/Full')    
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/dbedelevdt_Map/Zone_1') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/dbedelevdt_Map/Zone_1')  
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/dbedelevdt_Map/Zone_2') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/dbedelevdt_Map/Zone_2')  
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/dbedelevdt_Map/Zone_3') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/dbedelevdt_Map/Zone_3')  
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/dbedelevdt_Map/Zone_4') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/dbedelevdt_Map/Zone_4')  
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/dbedelevdt_Map/Zone_5') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/dbedelevdt_Map/Zone_5')  
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/dbedelevdt_timeseries') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/dbedelevdt_timeseries')  
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/dsoildepthdt_Map') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/dsoildepthdt_Map')     
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/dsoildepthdt_Map/Full') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/dsoildepthdt_Map/Full')    
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/dsoildepthdt_Map/Zone_1') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/dsoildepthdt_Map/Zone_1')  
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/dsoildepthdt_Map/Zone_2') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/dsoildepthdt_Map/Zone_2')  
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/dsoildepthdt_Map/Zone_3') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/dsoildepthdt_Map/Zone_3')  
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/dsoildepthdt_Map/Zone_4') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/dsoildepthdt_Map/Zone_4')  
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/dsoildepthdt_Map/Zone_5') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/dsoildepthdt_Map/Zone_5')  
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/dsoildepthdt_timeseries') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/dsoildepthdt_timeseries')  
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/dzdt_Map') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/dzdt_Map')     
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/dzdt_Map/Full') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/dzdt_Map/Full')    
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/dzdt_Map/Zone_1') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/dzdt_Map/Zone_1')  
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/dzdt_Map/Zone_2') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/dzdt_Map/Zone_2')  
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/dzdt_Map/Zone_3') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/dzdt_Map/Zone_3')  
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/dzdt_Map/Zone_4') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/dzdt_Map/Zone_4')  
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/dzdt_Map/Zone_5') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/dzdt_Map/Zone_5')  
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/dzdt_timeseries') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/dzdt_timeseries') 
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/erosionrate_Map') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/erosionrate_Map')     
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/erosionrate_Map/Full') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/erosionrate_Map/Full')    
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/erosionrate_Map/Zone_1') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/erosionrate_Map/Zone_1')  
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/erosionrate_Map/Zone_2') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/erosionrate_Map/Zone_2')  
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/erosionrate_Map/Zone_3') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/erosionrate_Map/Zone_3')  
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/erosionrate_Map/Zone_4') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/erosionrate_Map/Zone_4')  
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/erosionrate_Map/Zone_5') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/erosionrate_Map/Zone_5')  
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/erosionrate_timeseries') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/erosionrate_timeseries') 
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/netdz_Map') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/netdz_Map')   
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/netdz_Map/Full') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/netdz_Map/Full')    
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/netdz_Map/Zone_1') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/netdz_Map/Zone_1')  
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/netdz_Map/Zone_2') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/netdz_Map/Zone_2')  
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/netdz_Map/Zone_3') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/netdz_Map/Zone_3')  
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/netdz_Map/Zone_4') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/netdz_Map/Zone_4')  
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/netdz_Map/Zone_5') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/netdz_Map/Zone_5')  
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/netdz_timeseries') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/netdz_timeseries') 
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/sediment__flux_Map') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/sediment__flux_Map')   
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/sediment__flux_Map/Full') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/sediment__flux_Map/Full')    
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/sediment__flux_Map/Zone_1') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/sediment__flux_Map/Zone_1')  
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/sediment__flux_Map/Zone_2') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/sediment__flux_Map/Zone_2')  
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/sediment__flux_Map/Zone_3') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/sediment__flux_Map/Zone_3')  
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/sediment__flux_Map/Zone_4') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/sediment__flux_Map/Zone_4')  
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/sediment__flux_Map/Zone_5') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/sediment__flux_Map/Zone_5')  
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/sediment__flux_timeseries') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/sediment__flux_timeseries') 
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/sediment__flux_timeseries_gauge') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/sediment__flux_timeseries_gauge') 
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/Segs') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/Segs')     
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/Segs/Individual') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/Segs/Individual')       
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/Segs/Zones') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/Segs/Zones')      
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/Segs/Combined') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/Segs/Combined')    
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/Segs/Individual/MS') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/Segs/Individual/MS')  
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/Segs/Individual/WPa') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/Segs/Individual/WPa') 
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/Segs/Individual/WPb') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/Segs/Individual/WPb') 
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/Segs/Individual/WPc') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/Segs/Individual/WPc') 
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/Segs/Individual/WPd') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/Segs/Individual/WPd')   
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/Segs/Individual/HDa') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/Segs/Individual/HDa') 
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/Segs/Individual/HDb') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/Segs/Individual/HDb') 
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/Segs/Individual/GRa') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/Segs/Individual/GRa') 
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/Segs/Individual/OVa') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/Segs/Individual/OVa') 
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/Segs/Individual/WGa') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/Segs/Individual/WGa') 
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/Segs/Individual/WGb') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/Segs/Individual/WGb') 
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/Segs/Individual/WGc') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/Segs/Individual/WGc') 
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/Segs/Individual/WGd') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/Segs/Individual/WGd') 
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/Segs/Individual/WGe') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/Segs/Individual/WGe') 
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/Segs/Individual/WGf') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/Segs/Individual/WGf') 
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/Segs/Individual/SMa') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/Segs/Individual/SMa') 
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/Segs/Individual/SMb') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/Segs/Individual/SMb') 
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/Segs/Individual/SMc') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/Segs/Individual/SMc') 
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/Segs/Individual/SMd') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/Segs/Individual/SMd') 
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/Segs/Zones/Zone_1') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/Segs/Zones/Zone_1')
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/Segs/Zones/Zone_2') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/Segs/Zones/Zone_2')
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/Segs/Zones/Zone_3') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/Segs/Zones/Zone_3')
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/Segs/Zones/Zone_4') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/Segs/Zones/Zone_4')
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/Segs/Zones/Zone_5') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/Segs/Zones/Zone_5')
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/CSV') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/CSV')
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/Export_DEM') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/Export_DEM')
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/Final_topography') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/Final_topography')
if path.exists(str(export_directory)+'/Output_Run_K1ldevelopcal/Metadata') == False:
    os.mkdir(str(export_directory)+'/Output_Run_K1ldevelopcal/Metadata')

# Section break
print(' ')

#%% Create helper functions

# Print status
print('Creating helper functions...')

# Enforce colorbar tickmark label scientific notation decimal places to 2 
def sci_notation_format(x, _):
    return f"{x:.2e}"

# Function to find upstream nodes
def upstream_nodes(target):
    visited = set()
    q = deque([target])
    while q:
        n = q.popleft()
        for d in donors[n]:
            if d not in visited:
                visited.add(d)
                q.append(d)
    return np.array(list(visited))

# Section break
print(' ')

#%% Grid parameters

# Print status
print('Setting parameters...')

# DEM info
DEM_path = project_directory + '\\0_Input\\Level_2\\Model_Grid.asc'     # Grid
dxy = 100                                                               # Grid resolution
no_data_value_DEM = -9999                                               # Grid no data value
pour_point_node = 712                                                   # Watershed outlet node, identified manually. 

# Stream power exponents
m_sp = 0.5                  # Area exponent in stream power equation. 
n_sp = 1                    # Slope exponent in stream power equation. 
# K_sed = 8.8E-5              # Sediment / regolith erodibility, calibrated in previous workflow step

# Time parameters
dt = 0.1                    # Timestep (years)
tmax = 120                  # Max runtime (years)

# K0 and K1 info
K_br_path = project_directory + '\\0_Input\\Level_2\\K0.asc'            # Bedrock erodibility, created during earlier workflow step
K1_path = project_directory + '\\0_Input\\Level_2\\K1l.asc'            # Bedrock erodibility, created during earlier workflow step

# DTB info
DTB_path = project_directory + '\\0_Input\\Level_2\\DTB.asc'            # Depth to bedrock, created during earlier workflow step
no_data_value_DTB = -99999                                              # Depth to bedrock no-data value

# Land cover parameters
lc_path = project_directory + '\\0_Input\\Level_1\\NLCD_1985_32616.asc' 
lc_scheme_path = project_directory + '\\0_Input\\Level_1\\Erosion_Rate_Scheme.csv'

# Lithology parameters
Lith_ID_path = project_directory + '\\0_Input\\Level_1\\Lith_ID.asc' 

# 10Be data
Be10_Uplift = 9.15 * 1E-6               # 10^Be MCER at Gauge G from Reusser et al., 2015, recalculated by Octopus. (m / yr^-1)
Be10_Uplift_std = 2.15 * 1E-6           # 10^Be MCER error at Gauge G from Reusser et al., 2015, recalculated by Octopus. (m / yr^-1)

# Stream gauge coordinates
gauge_node_A_coords = [780850.762, 3824985.949]
gauge_node_B_coords = [768064.846, 3779955.623]
gauge_node_C_coords = [758441.612, 3765378.193]
gauge_node_D_coords = [735493.421, 3749456.656]
gauge_node_E_coords = [715720.492, 3726516.927]
gauge_node_F_coords = [695018.190, 3706087.663]
gauge_node_G_coords = [670097.647, 3640185.768]
gauge_node_H_coords = [679855.490, 3459872.720]

# Gauge radius
gauge_radius = 500      # Radius around gauge coordinates in which to identify gauge node (meters)

# Dam information
WL_Lanier = 327                         # Lanier water level (m)
dam_node_Lanier = 7551143               # Lanier dam node
start_Lanier = 56.0                     # Lanier model opening year
#
WL_WestPoint = 192                      # West Point water level (m)
dam_node_WestPoint = 4803339            # West Point dam node
start_WestPoint = 74.0                  # West Point model opening year
#
WL_Harding = 159                        # Harding water level (m)
dam_node_Harding = 4250150              # Harding dam node
start_Harding = 26.0                    # Harding model opening year
#
WL_GoatRock = 123                       # Goat Rock water level (m)
dam_node_GoatRock = 4136366             # Goat Rock dam node
start_GoatRock = 12.0                   # Goat Rock model opening year
#
WL_Oliver = 103                         # Oliver water level (m)
dam_node_Oliver = 3932391               # Oliver dam node
start_Oliver = 59.0                     # Oliver model opening year
#
WL_WFG = 58                             # WFG water level (m)
dam_node_WFG = 1991931                  # WFG dam node
start_WFG = 63.0                        # WFG model opening year
#
WL_Seminole = 24                        # Seminole water level (m)
dam_node_Seminole = pour_point_node     # Seminole dam node
start_Seminole = 54.0                   # Seminole model opening year

# Segment info (Node X,Y for the channel heads of interest)
seg_MS_head_X = 810494    
seg_MS_head_Y = 3858970
xlim_MS = [0, 800000 / 1000]
ylim_MS = [0, 800]
#
seg_WPa_head_X = 689188
seg_WPa_head_Y = 3745865
#
seg_WPb_head_X = 759292
seg_WPb_head_Y = 3746463
#
seg_WPc_head_X = 664096
seg_WPc_head_Y = 3700365
#
seg_WPd_head_X = 709594
seg_WPd_head_Y = 3682061
#
seg_HDa_head_X = 642995
seg_HDa_head_Y = 3627864
#
seg_HDb_head_X = 710189
seg_HDb_head_Y = 3636558
#
seg_GRa_head_X = 713095
seg_GRa_head_Y = 3638267
#
seg_OVa_head_X = 704595
seg_OVa_head_Y = 3611367
#
seg_WGa_head_X = 657011
seg_WGa_head_Y = 3609647
#
seg_WGb_head_X = 739893
seg_WGb_head_Y = 3607171
#
seg_WGc_head_X = 638303
seg_WGc_head_Y = 3571870
#
seg_WGd_head_X = 720202
seg_WGd_head_Y = 3552271
#
seg_WGe_head_X = 662510
seg_WGe_head_Y = 3513858
#
seg_WGf_head_X = 711897
seg_WGf_head_Y = 3554180
#
seg_SMa_head_X = 664592
seg_SMa_head_Y = 3512361
#
seg_SMb_head_X = 703698
seg_SMb_head_Y = 3497950
#
seg_SMc_head_X = 696089
seg_SMc_head_Y = 3453167
#
seg_SMd_head_X = 678901
seg_SMd_head_Y = 3417269

# Map focus zones
Zone_1_X = [750950, 829340]
Zone_1_Y = [3776866, 3859116]
#
Zone_2_X = [648946, 784436]
Zone_2_Y = [3639526, 3790847]
#
Zone_3_X = [642952, 722136]
Zone_3_Y = [3591569, 3659863]
#
Zone_4_X = [633240, 740032]
Zone_4_Y = [3495256, 3622506]
#
Zone_5_X = [650550, 707024]
Zone_5_Y = [3398916, 3516384]

# Plot intervals
Plot_interval = 10
Export_DEM_Interval = 150

# Toggle node field exports
Plot__topographic__elevation = True
Plot__dbedelevdt = True
Plot__dsoildepthdt = True
Plot__dzdt = True
Plot__erosionrate = True
Plot__netdz = True
Plot__sediment__flux = True

# Toggle sediment flux timeseries
Plot__sediment__flux_timeseries = True

# Toggle segments
Plot__segs = True

# Toggle DEM export
Export_DEM = False

# Plotting options
min_drainage_area = (dxy**2) * 1000     # Threshold drainage area to define channel extraction (m^2)
mapping_percentile = 97.7               # Percentile to limit color scaling. 
alpha = 0.7                             # Opacity

# Export options                    
Export_format = 'png'               # Export format
dpi = 600                           # Export dpi

# Section break
print(' ')

#%% Record run metadata

# Print status
print('Saving run metadata...')

with open("Output_Run_K1ldevelopcal/Metadata/Metadata_Run_K1.txt", "w") as f:
    f.write(f"Run = Run_K1\n")
    f.write(f"DEM_path = {DEM_path}\n")
    f.write(f"dxy = {dxy}\n")
    f.write(f"no_data_value_DEM = {no_data_value_DEM}\n")
    f.write(f"pour_point_node = {pour_point_node}\n")
    f.write(f"m_sp = {m_sp}\n")
    f.write(f"n_sp = {n_sp}\n")
    # f.write(f"K_sed = {K_sed}\n")
    f.write(f"dt = {dt}\n")
    f.write(f"tmax = {tmax}\n")
    f.write(f"K_br_path = {K_br_path}\n")
    f.write(f"K1_path = {K1_path}\n")
    f.write(f"DTB_path = {DTB_path}\n")
    f.write(f"no_data_value_DTB = {no_data_value_DTB}\n")
    f.write(f"Be10_Uplift = {Be10_Uplift}\n")
    f.write(f"Be10_Uplift_std = {Be10_Uplift_std}\n")
    f.write(f"gauge_node_A_coords = {gauge_node_A_coords}\n")
    f.write(f"gauge_node_B_coords = {gauge_node_B_coords}\n")
    f.write(f"gauge_node_C_coords = {gauge_node_C_coords}\n")
    f.write(f"gauge_node_D_coords = {gauge_node_D_coords}\n")
    f.write(f"gauge_node_E_coords = {gauge_node_E_coords}\n")
    f.write(f"gauge_node_F_coords = {gauge_node_F_coords}\n")
    f.write(f"gauge_node_G_coords = {gauge_node_G_coords}\n")
    f.write(f"gauge_node_H_coords = {gauge_node_H_coords}\n")
    f.write(f"gauge_radius = {gauge_radius}\n")
    f.write(f"WL_Lanier = {WL_Lanier}\n")
    f.write(f"dam_node_Lanier = {dam_node_Lanier}\n")
    f.write(f"start_Lanier = {start_Lanier}\n")
    f.write(f"WL_WestPoint = {WL_WestPoint}\n")
    f.write(f"dam_node_WestPoint = {dam_node_WestPoint}\n")
    f.write(f"start_WestPoint = {start_WestPoint}\n")
    f.write(f"WL_Harding = {WL_Harding}\n")
    f.write(f"dam_node_Harding = {dam_node_Harding}\n")
    f.write(f"start_Harding = {start_Harding}\n")
    f.write(f"WL_GoatRock = {WL_GoatRock}\n")
    f.write(f"dam_node_GoatRock = {dam_node_GoatRock}\n")
    f.write(f"start_GoatRock = {start_GoatRock}\n")
    f.write(f"WL_Oliver = {WL_Oliver}\n")
    f.write(f"dam_node_Oliver = {dam_node_Oliver}\n")
    f.write(f"start_Oliver = {start_Oliver}\n")
    f.write(f"WL_WFG = {WL_WFG}\n")
    f.write(f"dam_node_WFG = {dam_node_WFG}\n")
    f.write(f"start_WFG = {start_WFG}\n")
    f.write(f"WL_Seminole = {WL_Seminole}\n")
    f.write(f"dam_node_Seminole = {dam_node_Seminole}\n")
    f.write(f"start_Seminole = {start_Seminole}\n")
    f.write(f"seg_MS_head_X = {seg_MS_head_X}\n")
    f.write(f"seg_MS_head_Y = {seg_MS_head_Y}\n")
    f.write(f"xlim_MS = {xlim_MS}\n")
    f.write(f"ylim_MS = {ylim_MS}\n")
    f.write(f"seg_WPa_head_X = {seg_WPa_head_X}\n")
    f.write(f"seg_WPa_head_Y = {seg_WPa_head_Y}\n")
    f.write(f"seg_WPb_head_X = {seg_WPb_head_X}\n")
    f.write(f"seg_WPb_head_Y = {seg_WPb_head_Y}\n")
    f.write(f"seg_WPc_head_X = {seg_WPc_head_X}\n")
    f.write(f"seg_WPc_head_Y = {seg_WPc_head_Y}\n")
    f.write(f"seg_WPd_head_X = {seg_WPd_head_X}\n")
    f.write(f"seg_WPd_head_Y = {seg_WPd_head_Y}\n")
    f.write(f"seg_HDa_head_X = {seg_HDa_head_X}\n")
    f.write(f"seg_HDa_head_Y = {seg_HDa_head_Y}\n")
    f.write(f"seg_HDb_head_X = {seg_HDb_head_X}\n")
    f.write(f"seg_HDb_head_Y = {seg_HDb_head_Y}\n")
    f.write(f"seg_GRa_head_X = {seg_GRa_head_X}\n")
    f.write(f"seg_GRa_head_Y = {seg_GRa_head_Y}\n")
    f.write(f"seg_OVa_head_X = {seg_OVa_head_X}\n")
    f.write(f"seg_OVa_head_Y = {seg_OVa_head_Y}\n")
    f.write(f"seg_WGa_head_X = {seg_WGa_head_X}\n")
    f.write(f"seg_WGa_head_Y = {seg_WGa_head_Y}\n")
    f.write(f"seg_WGb_head_X = {seg_WGb_head_X}\n")
    f.write(f"seg_WGb_head_Y = {seg_WGb_head_Y}\n")
    f.write(f"seg_WGc_head_X = {seg_WGc_head_X}\n")
    f.write(f"seg_WGc_head_Y = {seg_WGc_head_Y}\n")
    f.write(f"seg_WGd_head_X = {seg_WGd_head_X}\n")
    f.write(f"seg_WGd_head_Y = {seg_WGd_head_Y}\n")
    f.write(f"seg_WGe_head_X = {seg_WGe_head_X}\n")
    f.write(f"seg_WGe_head_Y = {seg_WGe_head_Y}\n")
    f.write(f"seg_WGf_head_X = {seg_WGf_head_X}\n")
    f.write(f"seg_WGf_head_Y = {seg_WGf_head_Y}\n")
    f.write(f"seg_SMa_head_X = {seg_SMa_head_X}\n")
    f.write(f"seg_SMa_head_Y = {seg_SMa_head_Y}\n")
    f.write(f"seg_SMb_head_X = {seg_SMb_head_X}\n")
    f.write(f"seg_SMb_head_Y = {seg_SMb_head_Y}\n")
    f.write(f"seg_SMc_head_X = {seg_SMc_head_X}\n")
    f.write(f"seg_SMc_head_Y = {seg_SMc_head_Y}\n")
    f.write(f"seg_SMd_head_X = {seg_SMd_head_X}\n")
    f.write(f"seg_SMd_head_Y = {seg_SMd_head_Y}\n")
    f.write(f"Zone_1_X = {Zone_1_X}\n")
    f.write(f"Zone_1_Y = {Zone_1_Y}\n")
    f.write(f"Zone_2_X = {Zone_2_X}\n")
    f.write(f"Zone_2_Y = {Zone_2_Y}\n")
    f.write(f"Zone_3_X = {Zone_3_X}\n")
    f.write(f"Zone_3_Y = {Zone_3_Y}\n")
    f.write(f"Zone_4_X = {Zone_4_X}\n")
    f.write(f"Zone_4_Y = {Zone_4_Y}\n")
    f.write(f"Zone_5_X = {Zone_5_X}\n")
    f.write(f"Zone_5_Y = {Zone_5_Y}\n")
    f.write(f"Plot_interval = {Plot_interval}\n")
    f.write(f"Export_DEM_Interval = {Export_DEM_Interval}\n")
    f.write(f"Plot__topographic__elevation = {Plot__topographic__elevation}\n")
    f.write(f"Plot__dbedelevdt = {Plot__dbedelevdt}\n")
    f.write(f"Plot__dsoildepthdt = {Plot__dsoildepthdt}\n")
    f.write(f"Plot__dzdt = {Plot__dzdt}\n")
    f.write(f"Plot__erosionrate = {Plot__erosionrate}\n")
    f.write(f"Plot__netdz = {Plot__netdz}\n")
    f.write(f"Plot__sediment__flux = {Plot__sediment__flux}\n")
    f.write(f"Plot__sediment__flux_timeseries = {Plot__sediment__flux_timeseries}\n")
    f.write(f"Plot__segs = {Plot__segs}\n")
    f.write(f"Export_DEM = {Export_DEM}\n")
    f.write(f"min_drainage_area = {min_drainage_area}\n")
    f.write(f"mapping_percentile = {mapping_percentile}\n")
    f.write(f"alpha = {alpha}\n")
    f.write(f"Export_format = {Export_format}\n")
    f.write(f"dpi = {dpi}\n")
    
# Section break
print(' ')

#%% Initialize grid

# Print status
print('Initializing grid...')

# Set random seed
np.random.seed(0) 

# Import grid
(mg, zr) = read_esri_ascii(DEM_path, name='topographic__elevation')

# Handle model grid dimensions and non-value nodes
mg.set_nodata_nodes_to_closed(zr, no_data_value_DEM)
no_data_nodes = np.where(mg.at_node['topographic__elevation'] == no_data_value_DEM)
no_data_nodes = no_data_nodes[0]

# Create node keys
mg.add_zeros('node', 'dzdt')

# Handle grid boundaries
mg.set_status_at_node_on_edges(right=4, top=4, left=4, bottom=4)
mg.status_at_node[pour_point_node] = mg.BC_NODE_IS_FIXED_VALUE

# Fill sinks
sfb = SinkFillerBarnes(mg, method="D8", fill_flat=False)
sfb.run_one_step()

# Initialize flowAccumulator
frr = PriorityFloodFlowRouter(mg, flow_metric='D8')
frr.run_one_step()

# Set uplift rate
U = np.ones(mg.number_of_nodes) * Be10_Uplift

# Find nodes within radius of Gauge A
gauge_node_A = mg.find_nearest_node(gauge_node_A_coords)
distance = np.copy(mg.at_node['topographic__elevation'])
distance[:] = nan
distance = ( ((mg.x_of_node - mg.x_of_node[gauge_node_A]) ** 2) + ((mg.y_of_node - mg.y_of_node[gauge_node_A]) ** 2) ) ** 0.5
gauge_radius_nodes_A = np.where(distance < gauge_radius)
gauge_radius_nodes_A = gauge_radius_nodes_A[0]

# Find nodes within radius of Gauge B
gauge_node_B = mg.find_nearest_node(gauge_node_B_coords)
distance = np.copy(mg.at_node['topographic__elevation'])
distance[:] = nan
distance = ( ((mg.x_of_node - mg.x_of_node[gauge_node_B]) ** 2) + ((mg.y_of_node - mg.y_of_node[gauge_node_B]) ** 2) ) ** 0.5
gauge_radius_nodes_B = np.where(distance < gauge_radius)
gauge_radius_nodes_B = gauge_radius_nodes_B[0]

# Find nodes within radius of Gauge C
gauge_node_C = mg.find_nearest_node(gauge_node_C_coords)
distance = np.copy(mg.at_node['topographic__elevation'])
distance[:] = nan
distance = ( ((mg.x_of_node - mg.x_of_node[gauge_node_C]) ** 2) + ((mg.y_of_node - mg.y_of_node[gauge_node_C]) ** 2) ) ** 0.5
gauge_radius_nodes_C = np.where(distance < gauge_radius)
gauge_radius_nodes_C = gauge_radius_nodes_C[0]

# Find nodes within radius of Gauge D
gauge_node_D = mg.find_nearest_node(gauge_node_D_coords)
distance = np.copy(mg.at_node['topographic__elevation'])
distance[:] = nan
distance = ( ((mg.x_of_node - mg.x_of_node[gauge_node_D]) ** 2) + ((mg.y_of_node - mg.y_of_node[gauge_node_D]) ** 2) ) ** 0.5
gauge_radius_nodes_D = np.where(distance < gauge_radius)
gauge_radius_nodes_D = gauge_radius_nodes_D[0]

# Find nodes within radius of Gauge E
gauge_node_E = mg.find_nearest_node(gauge_node_E_coords)
distance = np.copy(mg.at_node['topographic__elevation'])
distance[:] = nan
distance = ( ((mg.x_of_node - mg.x_of_node[gauge_node_E]) ** 2) + ((mg.y_of_node - mg.y_of_node[gauge_node_E]) ** 2) ) ** 0.5
gauge_radius_nodes_E = np.where(distance < gauge_radius)
gauge_radius_nodes_E = gauge_radius_nodes_E[0]

# Find nodes within radius of Gauge F
gauge_node_F = mg.find_nearest_node(gauge_node_F_coords)
distance = np.copy(mg.at_node['topographic__elevation'])
distance[:] = nan
distance = ( ((mg.x_of_node - mg.x_of_node[gauge_node_F]) ** 2) + ((mg.y_of_node - mg.y_of_node[gauge_node_F]) ** 2) ) ** 0.5
gauge_radius_nodes_F = np.where(distance < gauge_radius)
gauge_radius_nodes_F = gauge_radius_nodes_F[0]

# Find nodes within radius of Gauge G
gauge_node_G = mg.find_nearest_node(gauge_node_G_coords)
distance = np.copy(mg.at_node['topographic__elevation'])
distance[:] = nan
distance = ( ((mg.x_of_node - mg.x_of_node[gauge_node_G]) ** 2) + ((mg.y_of_node - mg.y_of_node[gauge_node_G]) ** 2) ) ** 0.5
gauge_radius_nodes_G = np.where(distance < gauge_radius)
gauge_radius_nodes_G = gauge_radius_nodes_G[0]

# Find nodes within radius of Gauge H
gauge_node_H = mg.find_nearest_node(gauge_node_H_coords)
distance = np.copy(mg.at_node['topographic__elevation'])
distance[:] = nan
distance = ( ((mg.x_of_node - mg.x_of_node[gauge_node_H]) ** 2) + ((mg.y_of_node - mg.y_of_node[gauge_node_H]) ** 2) ) ** 0.5
gauge_radius_nodes_H = np.where(distance < gauge_radius)
gauge_radius_nodes_H = gauge_radius_nodes_H[0]

# Find node immediately upstream of pourpoint
distance = np.copy(mg.at_node['topographic__elevation'])
distance[:] = nan
distance = ( ((mg.x_of_node - mg.x_of_node[pour_point_node]) ** 2) + ((mg.y_of_node - mg.y_of_node[pour_point_node]) ** 2) ) ** 0.5
outlet_radius_nodes = np.where(distance < gauge_radius)
outlet_radius_nodes = outlet_radius_nodes[0]

# Section break
print(' ')

#%% Import K0 and DTB (depth to bedrock) and handle contact

# Print status
print('Initializing K0 and DTB...')

# Import DTB
(mg2, dtb) = read_esri_ascii(DTB_path, name='dtb')

# Handle DTB no_data values (open water)
dtb_no_data_fix_amount = np.mean(mg2.at_node['dtb'])
mg2.at_node['dtb'][np.where(mg2.at_node['dtb'] == no_data_value_DTB)] = dtb_no_data_fix_amount

# Handle DTB no data values
mg2.set_nodata_nodes_to_closed(dtb, no_data_value_DTB)

# Convert dtb units from cm to m
mg2.at_node['dtb'] /= 100                                       

# Handle bedrock-regolith contact
mg.at_node['soil__depth'] = mg2.at_node['dtb']
mg.at_node['bedrock__elevation'] = mg.at_node['topographic__elevation'] - mg.at_node['soil__depth']

# Import K0
(mg3, K_br) = read_esri_ascii(K_br_path, name='K_br')

# Store initial conditions
zr0 = np.copy(mg.at_node['topographic__elevation'])
br0 = np.copy(mg.at_node['bedrock__elevation'])
sd0 = np.copy(mg.at_node['soil__depth'])

# Section break
print(' ')

#%% Import land cover information

# Print status
print('Importing land cover information...')

# Import land cover data and erosion rate scheme
(mg4, K1) = read_esri_ascii(K1_path, name='K1')

# Import land cover data and erosion rate scheme
lc = read_esri_ascii(lc_path)
lc = lc[1]

# # Handle developed nodes
# developed = np.where((lc >= 21) & (lc <= 24))
# developed = developed[0]
# mg.at_node['water__unit_flux_in'][developed] = mg.at_node['water__unit_flux_in'][developed] * 10

# Section break
print(' ')

#%% Set urban runoff

# Print status
print('Handling urban runoff...')

# Q = CIA. Assume forested C = 0.01 (HEC-22 & ASCE). Developed C = [(NLCD mean impervious cover - forested C) / forested C]
mg.at_node['water__unit_flux_in'][np.where(lc == 22)] = 2.5
mg.at_node['water__unit_flux_in'][np.where(lc == 23)] = 5.5
mg.at_node['water__unit_flux_in'][np.where(lc == 23)] = 8

# Section break
print(' ')

#%% Import and handle Lith_ID and provenance

# Print status
print('Handling urban runoff...')

# Import land cover data and erosion rate scheme
(mg11, Lith_ID) = read_esri_ascii(Lith_ID_path, name='Lith_ID')

# Create node keys
mg.add_ones('node', 'Lith_ID')
mg.at_node['Lith_ID'] = mg.at_node['Lith_ID'] * Lith_ID

# Create provenance variable here


# Section break
print(' ')

#%% Set-up and plot initial channel segments

# Print status
print('Handling channel segments of interest...')

# Find segment head nodes
seg_MS_head = mg.find_nearest_node([seg_MS_head_X, seg_MS_head_Y])
seg_WPa_head = mg.find_nearest_node([seg_WPa_head_X, seg_WPa_head_Y])
seg_WPb_head = mg.find_nearest_node([seg_WPb_head_X, seg_WPb_head_Y])
seg_WPc_head = mg.find_nearest_node([seg_WPc_head_X, seg_WPc_head_Y])
seg_WPd_head = mg.find_nearest_node([seg_WPd_head_X, seg_WPd_head_Y])
seg_HDa_head = mg.find_nearest_node([seg_HDa_head_X, seg_HDa_head_Y])
seg_HDb_head = mg.find_nearest_node([seg_HDb_head_X, seg_HDb_head_Y])
seg_GRa_head = mg.find_nearest_node([seg_GRa_head_X, seg_GRa_head_Y])
seg_OVa_head = mg.find_nearest_node([seg_OVa_head_X, seg_OVa_head_Y])
seg_WGa_head = mg.find_nearest_node([seg_WGa_head_X, seg_WGa_head_Y])
seg_WGb_head = mg.find_nearest_node([seg_WGb_head_X, seg_WGb_head_Y])
seg_WGc_head = mg.find_nearest_node([seg_WGc_head_X, seg_WGc_head_Y])
seg_WGd_head = mg.find_nearest_node([seg_WGd_head_X, seg_WGd_head_Y])
seg_WGe_head = mg.find_nearest_node([seg_WGe_head_X, seg_WGe_head_Y])
seg_WGf_head = mg.find_nearest_node([seg_WGf_head_X, seg_WGf_head_Y])
seg_SMa_head = mg.find_nearest_node([seg_SMa_head_X, seg_SMa_head_Y])
seg_SMb_head = mg.find_nearest_node([seg_SMb_head_X, seg_SMb_head_Y])
seg_SMc_head = mg.find_nearest_node([seg_SMc_head_X, seg_SMc_head_Y])
seg_SMd_head = mg.find_nearest_node([seg_SMd_head_X, seg_SMd_head_Y])

# Get flow recievers
receivers = mg.at_node["flow__receiver_node"]

# Extract initial seg_MS
start_node = seg_MS_head
seg_MS_nodes = [start_node]
current_node = start_node
while True:
    next_node = receivers[current_node]
    if next_node == current_node:
        break  
    seg_MS_nodes.append(next_node)
    current_node = next_node
seg_MS_nodes = np.flip(np.array(seg_MS_nodes))
seg_MS_distance = seg_MS_nodes * 0
for i in np.arange(1, len(seg_MS_nodes)):
    seg_MS_distance[i] = seg_MS_distance[i-1] + ( ((mg.x_of_node[seg_MS_nodes[i]] - mg.x_of_node[seg_MS_nodes[i-1]]) ** 2) + ((mg.y_of_node[seg_MS_nodes[i]] - mg.y_of_node[seg_MS_nodes[i-1]]) ** 2) ) ** 0.5

# Extract initial seg_WPa
start_node = seg_WPa_head
seg_WPa_nodes = [start_node]
current_node = start_node
while True:
    next_node = receivers[current_node]
    if next_node == current_node:
        break  
    seg_WPa_nodes.append(next_node)
    current_node = next_node
seg_WPa_nodes = np.flip(np.array(seg_WPa_nodes))
seg_WPa_distance = seg_WPa_nodes * 0
for i in np.arange(1, len(seg_WPa_nodes)):
    seg_WPa_distance[i] = seg_WPa_distance[i-1] + ( ((mg.x_of_node[seg_WPa_nodes[i]] - mg.x_of_node[seg_WPa_nodes[i-1]]) ** 2) + ((mg.y_of_node[seg_WPa_nodes[i]] - mg.y_of_node[seg_WPa_nodes[i-1]]) ** 2) ) ** 0.5
seg_WPa_nodes_trib = seg_WPa_nodes[~np.isin(seg_WPa_nodes, seg_MS_nodes)]
seg_WPa_distance_trib = seg_WPa_distance[~np.isin(seg_WPa_nodes, seg_MS_nodes)]

# Extract initial seg_WPb
start_node = seg_WPb_head
seg_WPb_nodes = [start_node]
current_node = start_node
while True:
    next_node = receivers[current_node]
    if next_node == current_node:
        break  
    seg_WPb_nodes.append(next_node)
    current_node = next_node
seg_WPb_nodes = np.flip(np.array(seg_WPb_nodes))
seg_WPb_distance = seg_WPb_nodes * 0
for i in np.arange(1, len(seg_WPb_nodes)):
    seg_WPb_distance[i] = seg_WPb_distance[i-1] + ( ((mg.x_of_node[seg_WPb_nodes[i]] - mg.x_of_node[seg_WPb_nodes[i-1]]) ** 2) + ((mg.y_of_node[seg_WPb_nodes[i]] - mg.y_of_node[seg_WPb_nodes[i-1]]) ** 2) ) ** 0.5
seg_WPb_nodes_trib = seg_WPb_nodes[~np.isin(seg_WPb_nodes, seg_MS_nodes)]
seg_WPb_distance_trib = seg_WPb_distance[~np.isin(seg_WPb_nodes, seg_MS_nodes)]

# Extract initial seg_WPc
start_node = seg_WPc_head
seg_WPc_nodes = [start_node]
current_node = start_node
while True:
    next_node = receivers[current_node]
    if next_node == current_node:
        break  
    seg_WPc_nodes.append(next_node)
    current_node = next_node
seg_WPc_nodes = np.flip(np.array(seg_WPc_nodes))
seg_WPc_distance = seg_WPc_nodes * 0
for i in np.arange(1, len(seg_WPc_nodes)):
    seg_WPc_distance[i] = seg_WPc_distance[i-1] + ( ((mg.x_of_node[seg_WPc_nodes[i]] - mg.x_of_node[seg_WPc_nodes[i-1]]) ** 2) + ((mg.y_of_node[seg_WPc_nodes[i]] - mg.y_of_node[seg_WPc_nodes[i-1]]) ** 2) ) ** 0.5
seg_WPc_nodes_trib = seg_WPc_nodes[~np.isin(seg_WPc_nodes, seg_MS_nodes)]
seg_WPc_distance_trib = seg_WPc_distance[~np.isin(seg_WPc_nodes, seg_MS_nodes)]

# Extract initial seg_WPd
start_node = seg_WPd_head
seg_WPd_nodes = [start_node]
current_node = start_node
while True:
    next_node = receivers[current_node]
    if next_node == current_node:
        break  
    seg_WPd_nodes.append(next_node)
    current_node = next_node
seg_WPd_nodes = np.flip(np.array(seg_WPd_nodes))
seg_WPd_distance = seg_WPd_nodes * 0
for i in np.arange(1, len(seg_WPd_nodes)):
    seg_WPd_distance[i] = seg_WPd_distance[i-1] + ( ((mg.x_of_node[seg_WPd_nodes[i]] - mg.x_of_node[seg_WPd_nodes[i-1]]) ** 2) + ((mg.y_of_node[seg_WPd_nodes[i]] - mg.y_of_node[seg_WPd_nodes[i-1]]) ** 2) ) ** 0.5
seg_WPd_nodes_trib = seg_WPd_nodes[~np.isin(seg_WPd_nodes, seg_MS_nodes)]
seg_WPd_distance_trib = seg_WPd_distance[~np.isin(seg_WPd_nodes, seg_MS_nodes)]

# Extract initial seg_HDa
start_node = seg_HDa_head
seg_HDa_nodes = [start_node]
current_node = start_node
while True:
    next_node = receivers[current_node]
    if next_node == current_node:
        break  
    seg_HDa_nodes.append(next_node)
    current_node = next_node
seg_HDa_nodes = np.flip(np.array(seg_HDa_nodes))
seg_HDa_distance = seg_HDa_nodes * 0
for i in np.arange(1, len(seg_HDa_nodes)):
    seg_HDa_distance[i] = seg_HDa_distance[i-1] + ( ((mg.x_of_node[seg_HDa_nodes[i]] - mg.x_of_node[seg_HDa_nodes[i-1]]) ** 2) + ((mg.y_of_node[seg_HDa_nodes[i]] - mg.y_of_node[seg_HDa_nodes[i-1]]) ** 2) ) ** 0.5
seg_HDa_nodes_trib = seg_HDa_nodes[~np.isin(seg_HDa_nodes, seg_MS_nodes)]
seg_HDa_distance_trib = seg_HDa_distance[~np.isin(seg_HDa_nodes, seg_MS_nodes)]

# Extract initial seg_HDb
start_node = seg_HDb_head
seg_HDb_nodes = [start_node]
current_node = start_node
while True:
    next_node = receivers[current_node]
    if next_node == current_node:
        break  
    seg_HDb_nodes.append(next_node)
    current_node = next_node
seg_HDb_nodes = np.flip(np.array(seg_HDb_nodes))
seg_HDb_distance = seg_HDb_nodes * 0
for i in np.arange(1, len(seg_HDb_nodes)):
    seg_HDb_distance[i] = seg_HDb_distance[i-1] + ( ((mg.x_of_node[seg_HDb_nodes[i]] - mg.x_of_node[seg_HDb_nodes[i-1]]) ** 2) + ((mg.y_of_node[seg_HDb_nodes[i]] - mg.y_of_node[seg_HDb_nodes[i-1]]) ** 2) ) ** 0.5
seg_HDb_nodes_trib = seg_HDb_nodes[~np.isin(seg_HDb_nodes, seg_MS_nodes)]
seg_HDb_distance_trib = seg_HDb_distance[~np.isin(seg_HDb_nodes, seg_MS_nodes)]

# Extract initial seg_GRa
start_node = seg_GRa_head
seg_GRa_nodes = [start_node]
current_node = start_node
while True:
    next_node = receivers[current_node]
    if next_node == current_node:
        break  
    seg_GRa_nodes.append(next_node)
    current_node = next_node
seg_GRa_nodes = np.flip(np.array(seg_GRa_nodes))
seg_GRa_distance = seg_GRa_nodes * 0
for i in np.arange(1, len(seg_GRa_nodes)):
    seg_GRa_distance[i] = seg_GRa_distance[i-1] + ( ((mg.x_of_node[seg_GRa_nodes[i]] - mg.x_of_node[seg_GRa_nodes[i-1]]) ** 2) + ((mg.y_of_node[seg_GRa_nodes[i]] - mg.y_of_node[seg_GRa_nodes[i-1]]) ** 2) ) ** 0.5
seg_GRa_nodes_trib = seg_GRa_nodes[~np.isin(seg_GRa_nodes, seg_MS_nodes)]
seg_GRa_distance_trib = seg_GRa_distance[~np.isin(seg_GRa_nodes, seg_MS_nodes)]

# Extract initial seg_OVa
start_node = seg_OVa_head
seg_OVa_nodes = [start_node]
current_node = start_node
while True:
    next_node = receivers[current_node]
    if next_node == current_node:
        break  
    seg_OVa_nodes.append(next_node)
    current_node = next_node
seg_OVa_nodes = np.flip(np.array(seg_OVa_nodes))
seg_OVa_distance = seg_OVa_nodes * 0
for i in np.arange(1, len(seg_OVa_nodes)):
    seg_OVa_distance[i] = seg_OVa_distance[i-1] + ( ((mg.x_of_node[seg_OVa_nodes[i]] - mg.x_of_node[seg_OVa_nodes[i-1]]) ** 2) + ((mg.y_of_node[seg_OVa_nodes[i]] - mg.y_of_node[seg_OVa_nodes[i-1]]) ** 2) ) ** 0.5
seg_OVa_nodes_trib = seg_OVa_nodes[~np.isin(seg_OVa_nodes, seg_MS_nodes)]
seg_OVa_distance_trib = seg_OVa_distance[~np.isin(seg_OVa_nodes, seg_MS_nodes)]

# Extract initial seg_WGa
start_node = seg_WGa_head
seg_WGa_nodes = [start_node]
current_node = start_node
while True:
    next_node = receivers[current_node]
    if next_node == current_node:
        break  
    seg_WGa_nodes.append(next_node)
    current_node = next_node
seg_WGa_nodes = np.flip(np.array(seg_WGa_nodes))
seg_WGa_distance = seg_WGa_nodes * 0
for i in np.arange(1, len(seg_WGa_nodes)):
    seg_WGa_distance[i] = seg_WGa_distance[i-1] + ( ((mg.x_of_node[seg_WGa_nodes[i]] - mg.x_of_node[seg_WGa_nodes[i-1]]) ** 2) + ((mg.y_of_node[seg_WGa_nodes[i]] - mg.y_of_node[seg_WGa_nodes[i-1]]) ** 2) ) ** 0.5
seg_WGa_nodes_trib = seg_WGa_nodes[~np.isin(seg_WGa_nodes, seg_MS_nodes)]
seg_WGa_distance_trib = seg_WGa_distance[~np.isin(seg_WGa_nodes, seg_MS_nodes)]

# Extract initial seg_WGb
start_node = seg_WGb_head
seg_WGb_nodes = [start_node]
current_node = start_node
while True:
    next_node = receivers[current_node]
    if next_node == current_node:
        break  
    seg_WGb_nodes.append(next_node)
    current_node = next_node
seg_WGb_nodes = np.flip(np.array(seg_WGb_nodes))
seg_WGb_distance = seg_WGb_nodes * 0
for i in np.arange(1, len(seg_WGb_nodes)):
    seg_WGb_distance[i] = seg_WGb_distance[i-1] + ( ((mg.x_of_node[seg_WGb_nodes[i]] - mg.x_of_node[seg_WGb_nodes[i-1]]) ** 2) + ((mg.y_of_node[seg_WGb_nodes[i]] - mg.y_of_node[seg_WGb_nodes[i-1]]) ** 2) ) ** 0.5
seg_WGb_nodes_trib = seg_WGb_nodes[~np.isin(seg_WGb_nodes, seg_MS_nodes)]
seg_WGb_distance_trib = seg_WGb_distance[~np.isin(seg_WGb_nodes, seg_MS_nodes)]

# Extract initial seg_WGc
start_node = seg_WGc_head
seg_WGc_nodes = [start_node]
current_node = start_node
while True:
    next_node = receivers[current_node]
    if next_node == current_node:
        break  
    seg_WGc_nodes.append(next_node)
    current_node = next_node
seg_WGc_nodes = np.flip(np.array(seg_WGc_nodes))
seg_WGc_distance = seg_WGc_nodes * 0
for i in np.arange(1, len(seg_WGc_nodes)):
    seg_WGc_distance[i] = seg_WGc_distance[i-1] + ( ((mg.x_of_node[seg_WGc_nodes[i]] - mg.x_of_node[seg_WGc_nodes[i-1]]) ** 2) + ((mg.y_of_node[seg_WGc_nodes[i]] - mg.y_of_node[seg_WGc_nodes[i-1]]) ** 2) ) ** 0.5
seg_WGc_nodes_trib = seg_WGc_nodes[~np.isin(seg_WGc_nodes, seg_MS_nodes)]
seg_WGc_distance_trib = seg_WGc_distance[~np.isin(seg_WGc_nodes, seg_MS_nodes)]

# Extract initial seg_WGd
start_node = seg_WGd_head
seg_WGd_nodes = [start_node]
current_node = start_node
while True:
    next_node = receivers[current_node]
    if next_node == current_node:
        break  
    seg_WGd_nodes.append(next_node)
    current_node = next_node
seg_WGd_nodes = np.flip(np.array(seg_WGd_nodes))
seg_WGd_distance = seg_WGd_nodes * 0
for i in np.arange(1, len(seg_WGd_nodes)):
    seg_WGd_distance[i] = seg_WGd_distance[i-1] + ( ((mg.x_of_node[seg_WGd_nodes[i]] - mg.x_of_node[seg_WGd_nodes[i-1]]) ** 2) + ((mg.y_of_node[seg_WGd_nodes[i]] - mg.y_of_node[seg_WGd_nodes[i-1]]) ** 2) ) ** 0.5
seg_WGd_nodes_trib = seg_WGd_nodes[~np.isin(seg_WGd_nodes, seg_MS_nodes)]
seg_WGd_distance_trib = seg_WGd_distance[~np.isin(seg_WGd_nodes, seg_MS_nodes)]

# Extract initial seg_WGe
start_node = seg_WGe_head
seg_WGe_nodes = [start_node]
current_node = start_node
while True:
    next_node = receivers[current_node]
    if next_node == current_node:
        break  
    seg_WGe_nodes.append(next_node)
    current_node = next_node
seg_WGe_nodes = np.flip(np.array(seg_WGe_nodes))
seg_WGe_distance = seg_WGe_nodes * 0
for i in np.arange(1, len(seg_WGe_nodes)):
    seg_WGe_distance[i] = seg_WGe_distance[i-1] + ( ((mg.x_of_node[seg_WGe_nodes[i]] - mg.x_of_node[seg_WGe_nodes[i-1]]) ** 2) + ((mg.y_of_node[seg_WGe_nodes[i]] - mg.y_of_node[seg_WGe_nodes[i-1]]) ** 2) ) ** 0.5
seg_WGe_nodes_trib = seg_WGe_nodes[~np.isin(seg_WGe_nodes, seg_MS_nodes)]
seg_WGe_distance_trib = seg_WGe_distance[~np.isin(seg_WGe_nodes, seg_MS_nodes)]

# Extract initial seg_WGf
start_node = seg_WGf_head
seg_WGf_nodes = [start_node]
current_node = start_node
while True:
    next_node = receivers[current_node]
    if next_node == current_node:
        break  
    seg_WGf_nodes.append(next_node)
    current_node = next_node
seg_WGf_nodes = np.flip(np.array(seg_WGf_nodes))
seg_WGf_distance = seg_WGf_nodes * 0
for i in np.arange(1, len(seg_WGf_nodes)):
    seg_WGf_distance[i] = seg_WGf_distance[i-1] + ( ((mg.x_of_node[seg_WGf_nodes[i]] - mg.x_of_node[seg_WGf_nodes[i-1]]) ** 2) + ((mg.y_of_node[seg_WGf_nodes[i]] - mg.y_of_node[seg_WGf_nodes[i-1]]) ** 2) ) ** 0.5
seg_WGf_nodes_trib = seg_WGf_nodes[~np.isin(seg_WGf_nodes, seg_MS_nodes)]
seg_WGf_distance_trib = seg_WGf_distance[~np.isin(seg_WGf_nodes, seg_MS_nodes)]

# Extract initial seg_SMa
start_node = seg_SMa_head
seg_SMa_nodes = [start_node]
current_node = start_node
while True:
    next_node = receivers[current_node]
    if next_node == current_node:
        break  
    seg_SMa_nodes.append(next_node)
    current_node = next_node
seg_SMa_nodes = np.flip(np.array(seg_SMa_nodes))
seg_SMa_distance = seg_SMa_nodes * 0
for i in np.arange(1, len(seg_SMa_nodes)):
    seg_SMa_distance[i] = seg_SMa_distance[i-1] + ( ((mg.x_of_node[seg_SMa_nodes[i]] - mg.x_of_node[seg_SMa_nodes[i-1]]) ** 2) + ((mg.y_of_node[seg_SMa_nodes[i]] - mg.y_of_node[seg_SMa_nodes[i-1]]) ** 2) ) ** 0.5
seg_SMa_nodes_trib = seg_SMa_nodes[~np.isin(seg_SMa_nodes, seg_MS_nodes)]
seg_SMa_distance_trib = seg_SMa_distance[~np.isin(seg_SMa_nodes, seg_MS_nodes)]

# Extract initial seg_SMb
start_node = seg_SMb_head
seg_SMb_nodes = [start_node]
current_node = start_node
while True:
    next_node = receivers[current_node]
    if next_node == current_node:
        break  
    seg_SMb_nodes.append(next_node)
    current_node = next_node
seg_SMb_nodes = np.flip(np.array(seg_SMb_nodes))
seg_SMb_distance = seg_SMb_nodes * 0
for i in np.arange(1, len(seg_SMb_nodes)):
    seg_SMb_distance[i] = seg_SMb_distance[i-1] + ( ((mg.x_of_node[seg_SMb_nodes[i]] - mg.x_of_node[seg_SMb_nodes[i-1]]) ** 2) + ((mg.y_of_node[seg_SMb_nodes[i]] - mg.y_of_node[seg_SMb_nodes[i-1]]) ** 2) ) ** 0.5
seg_SMb_nodes_trib = seg_SMb_nodes[~np.isin(seg_SMb_nodes, seg_MS_nodes)]
seg_SMb_distance_trib = seg_SMb_distance[~np.isin(seg_SMb_nodes, seg_MS_nodes)]

# Extract initial seg_SMc
start_node = seg_SMc_head
seg_SMc_nodes = [start_node]
current_node = start_node
while True:
    next_node = receivers[current_node]
    if next_node == current_node:
        break  
    seg_SMc_nodes.append(next_node)
    current_node = next_node
seg_SMc_nodes = np.flip(np.array(seg_SMc_nodes))
seg_SMc_distance = seg_SMc_nodes * 0
for i in np.arange(1, len(seg_SMc_nodes)):
    seg_SMc_distance[i] = seg_SMc_distance[i-1] + ( ((mg.x_of_node[seg_SMc_nodes[i]] - mg.x_of_node[seg_SMc_nodes[i-1]]) ** 2) + ((mg.y_of_node[seg_SMc_nodes[i]] - mg.y_of_node[seg_SMc_nodes[i-1]]) ** 2) ) ** 0.5
seg_SMc_nodes_trib = seg_SMc_nodes[~np.isin(seg_SMc_nodes, seg_MS_nodes)]
seg_SMc_distance_trib = seg_SMc_distance[~np.isin(seg_SMc_nodes, seg_MS_nodes)]

# Extract initial seg_SMd
start_node = seg_SMd_head
seg_SMd_nodes = [start_node]
current_node = start_node
while True:
    next_node = receivers[current_node]
    if next_node == current_node:
        break  
    seg_SMd_nodes.append(next_node)
    current_node = next_node
seg_SMd_nodes = np.flip(np.array(seg_SMd_nodes))
seg_SMd_distance = seg_SMd_nodes * 0
for i in np.arange(1, len(seg_SMd_nodes)):
    seg_SMd_distance[i] = seg_SMd_distance[i-1] + ( ((mg.x_of_node[seg_SMd_nodes[i]] - mg.x_of_node[seg_SMd_nodes[i-1]]) ** 2) + ((mg.y_of_node[seg_SMd_nodes[i]] - mg.y_of_node[seg_SMd_nodes[i-1]]) ** 2) ) ** 0.5
seg_SMd_nodes_trib = seg_SMd_nodes[~np.isin(seg_SMd_nodes, seg_MS_nodes)]
seg_SMd_distance_trib = seg_SMd_distance[~np.isin(seg_SMd_nodes, seg_MS_nodes)]

# Plot individual seg_MS
fig = plt.figure()
plt.plot(seg_MS_distance / 1000, mg.at_node['topographic__elevation'][seg_MS_nodes], 'r--', linewidth = 0.5)
plt.plot(seg_MS_distance / 1000, mg.at_node['bedrock__elevation'][seg_MS_nodes], 'k--', linewidth = 0.5)
plt.xlim(xlim_MS)
plt.ylim(ylim_MS)
plt.grid()
plt.xlabel('Distance (km)')
plt.ylabel('Elevation (m)')
plt.title('t = 0 years')
plt.legend(['Topographic elevation', 'Bedrock elevation'], loc = 'upper left')
plt.tight_layout()
fig.savefig('Output_Run_K1ldevelopcal/Segs/Individual/MS/0.'+Export_format,  format=Export_format, dpi=dpi)
plt.close(fig)

# Plot individual seg_WPa
fig = plt.figure()
plt.plot(seg_WPa_distance_trib / 1000, mg.at_node['topographic__elevation'][seg_WPa_nodes_trib], 'r--', linewidth = 0.5)
plt.plot(seg_WPa_distance_trib / 1000, mg.at_node['bedrock__elevation'][seg_WPa_nodes_trib], 'k--', linewidth = 0.5)
plt.grid()
plt.xlabel('Distance (km)')
plt.ylabel('Elevation (m)')
plt.title('t = 0 years')
plt.legend(['Topographic elevation', 'Bedrock elevation'], loc = 'upper left')
plt.tight_layout()
fig.savefig('Output_Run_K1ldevelopcal/Segs/Individual/WPa/0.'+Export_format,  format=Export_format, dpi=dpi)
xlim_WPa = plt.xlim()
ylim_WPa = plt.ylim()
plt.close(fig)

# Plot individual seg_WPb
fig = plt.figure()
plt.plot(seg_WPb_distance_trib / 1000, mg.at_node['topographic__elevation'][seg_WPb_nodes_trib], 'r--', linewidth = 0.5)
plt.plot(seg_WPb_distance_trib / 1000, mg.at_node['bedrock__elevation'][seg_WPb_nodes_trib], 'k--', linewidth = 0.5)
plt.grid()
plt.xlabel('Distance (km)')
plt.ylabel('Elevation (m)')
plt.title('t = 0 years')
plt.legend(['Topographic elevation', 'Bedrock elevation'], loc = 'upper left')
plt.tight_layout()
fig.savefig('Output_Run_K1ldevelopcal/Segs/Individual/WPb/0.'+Export_format,  format=Export_format, dpi=dpi)
xlim_WPb = plt.xlim()
ylim_WPb = plt.ylim()
plt.close(fig)

# Plot individual seg_WPc
fig = plt.figure()
plt.plot(seg_WPc_distance_trib / 1000, mg.at_node['topographic__elevation'][seg_WPc_nodes_trib], 'r--', linewidth = 0.5)
plt.plot(seg_WPc_distance_trib / 1000, mg.at_node['bedrock__elevation'][seg_WPc_nodes_trib], 'k--', linewidth = 0.5)
plt.grid()
plt.xlabel('Distance (km)')
plt.ylabel('Elevation (m)')
plt.title('t = 0 years')
plt.legend(['Topographic elevation', 'Bedrock elevation'], loc = 'upper left')
plt.tight_layout()
fig.savefig('Output_Run_K1ldevelopcal/Segs/Individual/WPc/0.'+Export_format,  format=Export_format, dpi=dpi)
xlim_WPc = plt.xlim()
ylim_WPc = plt.ylim()
plt.close(fig)

# Plot individual seg_WPd
fig = plt.figure()
plt.plot(seg_WPd_distance_trib / 1000, mg.at_node['topographic__elevation'][seg_WPd_nodes_trib], 'r--', linewidth = 0.5)
plt.plot(seg_WPd_distance_trib / 1000, mg.at_node['bedrock__elevation'][seg_WPd_nodes_trib], 'k--', linewidth = 0.5)
plt.grid()
plt.xlabel('Distance (km)')
plt.ylabel('Elevation (m)')
plt.title('t = 0 years')
plt.legend(['Topographic elevation', 'Bedrock elevation'], loc = 'upper left')
plt.tight_layout()
fig.savefig('Output_Run_K1ldevelopcal/Segs/Individual/WPd/0.'+Export_format,  format=Export_format, dpi=dpi)
xlim_WPd = plt.xlim()
ylim_WPd = plt.ylim()
plt.close(fig)

# Plot individual seg_HDa
fig = plt.figure()
plt.plot(seg_HDa_distance_trib / 1000, mg.at_node['topographic__elevation'][seg_HDa_nodes_trib], 'r--', linewidth = 0.5)
plt.plot(seg_HDa_distance_trib / 1000, mg.at_node['bedrock__elevation'][seg_HDa_nodes_trib], 'k--', linewidth = 0.5)
plt.grid()
plt.xlabel('Distance (km)')
plt.ylabel('Elevation (m)')
plt.title('t = 0 years')
plt.legend(['Topographic elevation', 'Bedrock elevation'], loc = 'upper left')
plt.tight_layout()
fig.savefig('Output_Run_K1ldevelopcal/Segs/Individual/HDa/0.'+Export_format,  format=Export_format, dpi=dpi)
xlim_HDa = plt.xlim()
ylim_HDa = plt.ylim()
plt.close(fig)

# Plot individual seg_HDb
fig = plt.figure()
plt.plot(seg_HDb_distance_trib / 1000, mg.at_node['topographic__elevation'][seg_HDb_nodes_trib], 'r--', linewidth = 0.5)
plt.plot(seg_HDb_distance_trib / 1000, mg.at_node['bedrock__elevation'][seg_HDb_nodes_trib], 'k--', linewidth = 0.5)
plt.grid()
plt.xlabel('Distance (km)')
plt.ylabel('Elevation (m)')
plt.title('t = 0 years')
plt.legend(['Topographic elevation', 'Bedrock elevation'], loc = 'upper left')
plt.tight_layout()
fig.savefig('Output_Run_K1ldevelopcal/Segs/Individual/HDb/0.'+Export_format,  format=Export_format, dpi=dpi)
xlim_HDb = plt.xlim()
ylim_HDb = plt.ylim()
plt.close(fig)

# Plot individual seg_GRa
fig = plt.figure()
plt.plot(seg_GRa_distance_trib / 1000, mg.at_node['topographic__elevation'][seg_GRa_nodes_trib], 'r--', linewidth = 0.5)
plt.plot(seg_GRa_distance_trib / 1000, mg.at_node['bedrock__elevation'][seg_GRa_nodes_trib], 'k--', linewidth = 0.5)
plt.grid()
plt.xlabel('Distance (km)')
plt.ylabel('Elevation (m)')
plt.title('t = 0 years')
plt.legend(['Topographic elevation', 'Bedrock elevation'], loc = 'upper left')
plt.tight_layout()
fig.savefig('Output_Run_K1ldevelopcal/Segs/Individual/GRa/0.'+Export_format,  format=Export_format, dpi=dpi)
xlim_GRa = plt.xlim()
ylim_GRa = plt.ylim()
plt.close(fig)

# Plot individual seg_OVa
fig = plt.figure()
plt.plot(seg_OVa_distance_trib / 1000, mg.at_node['topographic__elevation'][seg_OVa_nodes_trib], 'r--', linewidth = 0.5)
plt.plot(seg_OVa_distance_trib / 1000, mg.at_node['bedrock__elevation'][seg_OVa_nodes_trib], 'k--', linewidth = 0.5)
plt.grid()
plt.xlabel('Distance (km)')
plt.ylabel('Elevation (m)')
plt.title('t = 0 years')
plt.legend(['Topographic elevation', 'Bedrock elevation'], loc = 'upper left')
plt.tight_layout()
fig.savefig('Output_Run_K1ldevelopcal/Segs/Individual/OVa/0.'+Export_format,  format=Export_format, dpi=dpi)
xlim_OVa = plt.xlim()
ylim_OVa = plt.ylim()
plt.close(fig)

# Plot individual seg_WGa
fig = plt.figure()
plt.plot(seg_WGa_distance_trib / 1000, mg.at_node['topographic__elevation'][seg_WGa_nodes_trib], 'r--', linewidth = 0.5)
plt.plot(seg_WGa_distance_trib / 1000, mg.at_node['bedrock__elevation'][seg_WGa_nodes_trib], 'k--', linewidth = 0.5)
plt.grid()
plt.xlabel('Distance (km)')
plt.ylabel('Elevation (m)')
plt.title('t = 0 years')
plt.legend(['Topographic elevation', 'Bedrock elevation'], loc = 'upper left')
plt.tight_layout()
fig.savefig('Output_Run_K1ldevelopcal/Segs/Individual/WGa/0.'+Export_format,  format=Export_format, dpi=dpi)
xlim_WGa = plt.xlim()
ylim_WGa = plt.ylim()
plt.close(fig)

# Plot individual seg_WGb
fig = plt.figure()
plt.plot(seg_WGb_distance_trib / 1000, mg.at_node['topographic__elevation'][seg_WGb_nodes_trib], 'r--', linewidth = 0.5)
plt.plot(seg_WGb_distance_trib / 1000, mg.at_node['bedrock__elevation'][seg_WGb_nodes_trib], 'k--', linewidth = 0.5)
plt.grid()
plt.xlabel('Distance (km)')
plt.ylabel('Elevation (m)')
plt.title('t = 0 years')
plt.legend(['Topographic elevation', 'Bedrock elevation'], loc = 'upper left')
plt.tight_layout()
fig.savefig('Output_Run_K1ldevelopcal/Segs/Individual/WGb/0.'+Export_format,  format=Export_format, dpi=dpi)
xlim_WGb = plt.xlim()
ylim_WGb = plt.ylim()
plt.close(fig)

# Plot individual seg_WGc
fig = plt.figure()
plt.plot(seg_WGc_distance_trib / 1000, mg.at_node['topographic__elevation'][seg_WGc_nodes_trib], 'r--', linewidth = 0.5)
plt.plot(seg_WGc_distance_trib / 1000, mg.at_node['bedrock__elevation'][seg_WGc_nodes_trib], 'k--', linewidth = 0.5)
plt.grid()
plt.xlabel('Distance (km)')
plt.ylabel('Elevation (m)')
plt.title('t = 0 years')
plt.legend(['Topographic elevation', 'Bedrock elevation'], loc = 'upper left')
plt.tight_layout()
fig.savefig('Output_Run_K1ldevelopcal/Segs/Individual/WGc/0.'+Export_format,  format=Export_format, dpi=dpi)
xlim_WGc = plt.xlim()
ylim_WGc = plt.ylim()
plt.close(fig)

# Plot individual seg_WGd
fig = plt.figure()
plt.plot(seg_WGd_distance_trib / 1000, mg.at_node['topographic__elevation'][seg_WGd_nodes_trib], 'r--', linewidth = 0.5)
plt.plot(seg_WGd_distance_trib / 1000, mg.at_node['bedrock__elevation'][seg_WGd_nodes_trib], 'k--', linewidth = 0.5)
plt.grid()
plt.xlabel('Distance (km)')
plt.ylabel('Elevation (m)')
plt.title('t = 0 years')
plt.legend(['Topographic elevation', 'Bedrock elevation'], loc = 'upper left')
plt.tight_layout()
fig.savefig('Output_Run_K1ldevelopcal/Segs/Individual/WGd/0.'+Export_format,  format=Export_format, dpi=dpi)
xlim_WGd = plt.xlim()
ylim_WGd = plt.ylim()
plt.close(fig)

# Plot individual seg_WGe
fig = plt.figure()
plt.plot(seg_WGe_distance_trib / 1000, mg.at_node['topographic__elevation'][seg_WGe_nodes_trib], 'r--', linewidth = 0.5)
plt.plot(seg_WGe_distance_trib / 1000, mg.at_node['bedrock__elevation'][seg_WGe_nodes_trib], 'k--', linewidth = 0.5)
plt.grid()
plt.xlabel('Distance (km)')
plt.ylabel('Elevation (m)')
plt.title('t = 0 years')
plt.legend(['Topographic elevation', 'Bedrock elevation'], loc = 'upper left')
plt.tight_layout()
fig.savefig('Output_Run_K1ldevelopcal/Segs/Individual/WGe/0.'+Export_format,  format=Export_format, dpi=dpi)
xlim_WGe = plt.xlim()
ylim_WGe = plt.ylim()
plt.close(fig)

# Plot individual seg_WGf
fig = plt.figure()
plt.plot(seg_WGf_distance_trib / 1000, mg.at_node['topographic__elevation'][seg_WGf_nodes_trib], 'r--', linewidth = 0.5)
plt.plot(seg_WGf_distance_trib / 1000, mg.at_node['bedrock__elevation'][seg_WGf_nodes_trib], 'k--', linewidth = 0.5)
plt.grid()
plt.xlabel('Distance (km)')
plt.ylabel('Elevation (m)')
plt.title('t = 0 years')
plt.legend(['Topographic elevation', 'Bedrock elevation'], loc = 'upper left')
plt.tight_layout()
fig.savefig('Output_Run_K1ldevelopcal/Segs/Individual/WGf/0.'+Export_format,  format=Export_format, dpi=dpi)
xlim_WGf = plt.xlim()
ylim_WGf = plt.ylim()
plt.close(fig)

# Plot individual seg_SMa
fig = plt.figure()
plt.plot(seg_SMa_distance_trib / 1000, mg.at_node['topographic__elevation'][seg_SMa_nodes_trib], 'r--', linewidth = 0.5)
plt.plot(seg_SMa_distance_trib / 1000, mg.at_node['bedrock__elevation'][seg_SMa_nodes_trib], 'k--', linewidth = 0.5)
plt.grid()
plt.xlabel('Distance (km)')
plt.ylabel('Elevation (m)')
plt.title('t = 0 years')
plt.legend(['Topographic elevation', 'Bedrock elevation'], loc = 'upper left')
plt.tight_layout()
fig.savefig('Output_Run_K1ldevelopcal/Segs/Individual/SMa/0.'+Export_format,  format=Export_format, dpi=dpi)
xlim_SMa = plt.xlim()
ylim_SMa = plt.ylim()
plt.close(fig)

# Plot individual seg_SMb
fig = plt.figure()
plt.plot(seg_SMb_distance_trib / 1000, mg.at_node['topographic__elevation'][seg_SMb_nodes_trib], 'r--', linewidth = 0.5)
plt.plot(seg_SMb_distance_trib / 1000, mg.at_node['bedrock__elevation'][seg_SMb_nodes_trib], 'k--', linewidth = 0.5)
plt.grid()
plt.xlabel('Distance (km)')
plt.ylabel('Elevation (m)')
plt.title('t = 0 years')
plt.legend(['Topographic elevation', 'Bedrock elevation'], loc = 'upper left')
plt.tight_layout()
fig.savefig('Output_Run_K1ldevelopcal/Segs/Individual/SMb/0.'+Export_format,  format=Export_format, dpi=dpi)
xlim_SMb = plt.xlim()
ylim_SMb = plt.ylim()
plt.close(fig)

# Plot individual seg_SMc
fig = plt.figure()
plt.plot(seg_SMc_distance_trib / 1000, mg.at_node['topographic__elevation'][seg_SMc_nodes_trib], 'r--', linewidth = 0.5)
plt.plot(seg_SMc_distance_trib / 1000, mg.at_node['bedrock__elevation'][seg_SMc_nodes_trib], 'k--', linewidth = 0.5)
plt.grid()
plt.xlabel('Distance (km)')
plt.ylabel('Elevation (m)')
plt.title('t = 0 years')
plt.legend(['Topographic elevation', 'Bedrock elevation'], loc = 'upper left')
plt.tight_layout()
fig.savefig('Output_Run_K1ldevelopcal/Segs/Individual/SMc/0.'+Export_format,  format=Export_format, dpi=dpi)
xlim_SMc = plt.xlim()
ylim_SMc = plt.ylim()
plt.close(fig)

# Plot individual seg_SMd
fig = plt.figure()
plt.plot(seg_SMd_distance_trib / 1000, mg.at_node['topographic__elevation'][seg_SMd_nodes_trib], 'r--', linewidth = 0.5)
plt.plot(seg_SMd_distance_trib / 1000, mg.at_node['bedrock__elevation'][seg_SMd_nodes_trib], 'k--', linewidth = 0.5)
plt.grid()
plt.xlabel('Distance (km)')
plt.ylabel('Elevation (m)')
plt.title('t = 0 years')
plt.legend(['Topographic elevation', 'Bedrock elevation'], loc = 'upper left')
plt.tight_layout()
fig.savefig('Output_Run_K1ldevelopcal/Segs/Individual/SMd/0.'+Export_format,  format=Export_format, dpi=dpi)
xlim_SMd = plt.xlim()
ylim_SMd = plt.ylim()
plt.close(fig)

# Plot combined segments
fig = plt.figure()
plt.plot(seg_MS_distance / 1000, mg.at_node['topographic__elevation'][seg_MS_nodes], 'r--', linewidth = 0.5)
plt.plot(seg_MS_distance / 1000, mg.at_node['bedrock__elevation'][seg_MS_nodes], 'k--', linewidth = 0.5)
plt.plot(seg_WPa_distance_trib / 1000, mg.at_node['topographic__elevation'][seg_WPa_nodes_trib], 'r--', linewidth = 0.5)
plt.plot(seg_WPa_distance_trib / 1000, mg.at_node['bedrock__elevation'][seg_WPa_nodes_trib], 'k--', linewidth = 0.5)
plt.plot(seg_WPb_distance_trib / 1000, mg.at_node['topographic__elevation'][seg_WPb_nodes_trib], 'r--', linewidth = 0.5)
plt.plot(seg_WPb_distance_trib / 1000, mg.at_node['bedrock__elevation'][seg_WPb_nodes_trib], 'k--', linewidth = 0.5)
plt.plot(seg_WPc_distance_trib / 1000, mg.at_node['topographic__elevation'][seg_WPc_nodes_trib], 'r--', linewidth = 0.5)
plt.plot(seg_WPc_distance_trib / 1000, mg.at_node['bedrock__elevation'][seg_WPc_nodes_trib], 'k--', linewidth = 0.5)
plt.plot(seg_WPd_distance_trib / 1000, mg.at_node['topographic__elevation'][seg_WPd_nodes_trib], 'r--', linewidth = 0.5)
plt.plot(seg_WPd_distance_trib / 1000, mg.at_node['bedrock__elevation'][seg_WPd_nodes_trib], 'k--', linewidth = 0.5)
plt.plot(seg_HDa_distance_trib / 1000, mg.at_node['topographic__elevation'][seg_HDa_nodes_trib], 'r--', linewidth = 0.5)
plt.plot(seg_HDa_distance_trib / 1000, mg.at_node['bedrock__elevation'][seg_HDa_nodes_trib], 'k--', linewidth = 0.5)
plt.plot(seg_HDb_distance_trib / 1000, mg.at_node['topographic__elevation'][seg_HDb_nodes_trib], 'r--', linewidth = 0.5)
plt.plot(seg_HDb_distance_trib / 1000, mg.at_node['bedrock__elevation'][seg_HDb_nodes_trib], 'k--', linewidth = 0.5)
plt.plot(seg_GRa_distance_trib / 1000, mg.at_node['topographic__elevation'][seg_GRa_nodes_trib], 'r--', linewidth = 0.5)
plt.plot(seg_GRa_distance_trib / 1000, mg.at_node['bedrock__elevation'][seg_GRa_nodes_trib], 'k--', linewidth = 0.5)
plt.plot(seg_OVa_distance_trib / 1000, mg.at_node['topographic__elevation'][seg_OVa_nodes_trib], 'r--', linewidth = 0.5)
plt.plot(seg_OVa_distance_trib / 1000, mg.at_node['bedrock__elevation'][seg_OVa_nodes_trib], 'k--', linewidth = 0.5)
plt.plot(seg_WGa_distance_trib / 1000, mg.at_node['topographic__elevation'][seg_WGa_nodes_trib], 'r--', linewidth = 0.5)
plt.plot(seg_WGa_distance_trib / 1000, mg.at_node['bedrock__elevation'][seg_WGa_nodes_trib], 'k--', linewidth = 0.5)
plt.plot(seg_WGb_distance_trib / 1000, mg.at_node['topographic__elevation'][seg_WGb_nodes_trib], 'r--', linewidth = 0.5)
plt.plot(seg_WGb_distance_trib / 1000, mg.at_node['bedrock__elevation'][seg_WGb_nodes_trib], 'k--', linewidth = 0.5)
plt.plot(seg_WGc_distance_trib / 1000, mg.at_node['topographic__elevation'][seg_WGc_nodes_trib], 'r--', linewidth = 0.5)
plt.plot(seg_WGc_distance_trib / 1000, mg.at_node['bedrock__elevation'][seg_WGc_nodes_trib], 'k--', linewidth = 0.5)
plt.plot(seg_WGd_distance_trib / 1000, mg.at_node['topographic__elevation'][seg_WGd_nodes_trib], 'r--', linewidth = 0.5)
plt.plot(seg_WGd_distance_trib / 1000, mg.at_node['bedrock__elevation'][seg_WGd_nodes_trib], 'k--', linewidth = 0.5)
plt.plot(seg_WGe_distance_trib / 1000, mg.at_node['topographic__elevation'][seg_WGe_nodes_trib], 'r--', linewidth = 0.5)
plt.plot(seg_WGe_distance_trib / 1000, mg.at_node['bedrock__elevation'][seg_WGe_nodes_trib], 'k--', linewidth = 0.5)
plt.plot(seg_WGf_distance_trib / 1000, mg.at_node['topographic__elevation'][seg_WGf_nodes_trib], 'r--', linewidth = 0.5)
plt.plot(seg_WGf_distance_trib / 1000, mg.at_node['bedrock__elevation'][seg_WGf_nodes_trib], 'k--', linewidth = 0.5)
plt.plot(seg_SMa_distance_trib / 1000, mg.at_node['topographic__elevation'][seg_SMa_nodes_trib], 'r--', linewidth = 0.5)
plt.plot(seg_SMa_distance_trib / 1000, mg.at_node['bedrock__elevation'][seg_SMa_nodes_trib], 'k--', linewidth = 0.5)
plt.plot(seg_SMb_distance_trib / 1000, mg.at_node['topographic__elevation'][seg_SMb_nodes_trib], 'r--', linewidth = 0.5)
plt.plot(seg_SMb_distance_trib / 1000, mg.at_node['bedrock__elevation'][seg_SMb_nodes_trib], 'k--', linewidth = 0.5)
plt.plot(seg_SMc_distance_trib / 1000, mg.at_node['topographic__elevation'][seg_SMc_nodes_trib], 'r--', linewidth = 0.5)
plt.plot(seg_SMc_distance_trib / 1000, mg.at_node['bedrock__elevation'][seg_SMc_nodes_trib], 'k--', linewidth = 0.5)
plt.plot(seg_SMd_distance_trib / 1000, mg.at_node['topographic__elevation'][seg_SMd_nodes_trib], 'r--', linewidth = 0.5)
plt.plot(seg_SMd_distance_trib / 1000, mg.at_node['bedrock__elevation'][seg_SMd_nodes_trib], 'k--', linewidth = 0.5)
plt.xlim(xlim_MS)
plt.ylim(ylim_MS)
plt.grid()
plt.xlabel('Distance (km)')
plt.ylabel('Elevation (m)')
plt.title('t = 0 years')
plt.legend(['Topographic elevation', 'Bedrock elevation'], loc = 'upper left')
plt.tight_layout()
fig.savefig('Output_Run_K1ldevelopcal/Segs/Combined/0.'+Export_format,  format=Export_format, dpi=dpi)
plt.close(fig)

# Get longitudinal profile zone limits
focus = (mg.y_of_node[seg_MS_nodes] > Zone_1_Y[0]) & (mg.y_of_node[seg_MS_nodes] < Zone_1_Y[1])
seg_MS_zone_1_nodes = seg_MS_nodes[(mg.y_of_node[seg_MS_nodes] > Zone_1_Y[0]) & (mg.y_of_node[seg_MS_nodes] < Zone_1_Y[1])]
seg_MS_zone_1_distance = seg_MS_distance[(mg.y_of_node[seg_MS_nodes] > Zone_1_Y[0]) & (mg.y_of_node[seg_MS_nodes] < Zone_1_Y[1])]
#
focus = (mg.y_of_node[seg_MS_nodes] > Zone_2_Y[0]) & (mg.y_of_node[seg_MS_nodes] < Zone_2_Y[1])
seg_MS_zone_2_nodes = seg_MS_nodes[(mg.y_of_node[seg_MS_nodes] > Zone_2_Y[0]) & (mg.y_of_node[seg_MS_nodes] < Zone_2_Y[1])]
seg_MS_zone_2_distance = seg_MS_distance[(mg.y_of_node[seg_MS_nodes] > Zone_2_Y[0]) & (mg.y_of_node[seg_MS_nodes] < Zone_2_Y[1])]
#
focus = (mg.y_of_node[seg_MS_nodes] > Zone_3_Y[0]) & (mg.y_of_node[seg_MS_nodes] < Zone_3_Y[1])
seg_MS_zone_3_nodes = seg_MS_nodes[(mg.y_of_node[seg_MS_nodes] > Zone_3_Y[0]) & (mg.y_of_node[seg_MS_nodes] < Zone_3_Y[1])]
seg_MS_zone_3_distance = seg_MS_distance[(mg.y_of_node[seg_MS_nodes] > Zone_3_Y[0]) & (mg.y_of_node[seg_MS_nodes] < Zone_3_Y[1])]
#
focus = (mg.y_of_node[seg_MS_nodes] > Zone_4_Y[0]) & (mg.y_of_node[seg_MS_nodes] < Zone_4_Y[1])
seg_MS_zone_4_nodes = seg_MS_nodes[(mg.y_of_node[seg_MS_nodes] > Zone_4_Y[0]) & (mg.y_of_node[seg_MS_nodes] < Zone_4_Y[1])]
seg_MS_zone_4_distance = seg_MS_distance[(mg.y_of_node[seg_MS_nodes] > Zone_4_Y[0]) & (mg.y_of_node[seg_MS_nodes] < Zone_4_Y[1])]
#
focus = (mg.y_of_node[seg_MS_nodes] > Zone_5_Y[0]) & (mg.y_of_node[seg_MS_nodes] < Zone_5_Y[1])
seg_MS_zone_5_nodes = seg_MS_nodes[(mg.y_of_node[seg_MS_nodes] > Zone_5_Y[0]) & (mg.y_of_node[seg_MS_nodes] < Zone_5_Y[1])]
seg_MS_zone_5_distance = seg_MS_distance[(mg.y_of_node[seg_MS_nodes] > Zone_5_Y[0]) & (mg.y_of_node[seg_MS_nodes] < Zone_5_Y[1])]

# Plot Zone 1
fig = plt.figure()
plt.plot(seg_MS_zone_1_distance / 1000, mg.at_node['topographic__elevation'][seg_MS_zone_1_nodes], 'r--', linewidth = 0.5)
plt.plot(seg_MS_zone_1_distance / 1000, mg.at_node['bedrock__elevation'][seg_MS_zone_1_nodes], 'k--', linewidth = 0.5)
plt.grid()
plt.xlabel('Distance (km)')
plt.ylabel('Elevation (m)')
plt.title('t = 0 years')
plt.legend(['Topographic elevation', 'Bedrock elevation'], loc = 'upper left')
plt.tight_layout()
fig.savefig('Output_Run_K1ldevelopcal/Segs/Zones/Zone_1/0.'+Export_format,  format=Export_format, dpi=dpi)
xlim_Zone_1 = plt.xlim()
ylim_Zone_1 = plt.ylim()
plt.close(fig)

# Plot Zone 2
fig = plt.figure()
plt.plot(seg_MS_zone_2_distance / 1000, mg.at_node['topographic__elevation'][seg_MS_zone_2_nodes], 'r--', linewidth = 0.5)
plt.plot(seg_MS_zone_2_distance / 1000, mg.at_node['bedrock__elevation'][seg_MS_zone_2_nodes], 'k--', linewidth = 0.5)
plt.plot(seg_WPa_distance_trib / 1000, mg.at_node['topographic__elevation'][seg_WPa_nodes_trib], 'r--', linewidth = 0.5)
plt.plot(seg_WPa_distance_trib / 1000, mg.at_node['bedrock__elevation'][seg_WPa_nodes_trib], 'k--', linewidth = 0.5)
plt.plot(seg_WPb_distance_trib / 1000, mg.at_node['topographic__elevation'][seg_WPb_nodes_trib], 'r--', linewidth = 0.5)
plt.plot(seg_WPb_distance_trib / 1000, mg.at_node['bedrock__elevation'][seg_WPb_nodes_trib], 'k--', linewidth = 0.5)
plt.plot(seg_WPc_distance_trib / 1000, mg.at_node['topographic__elevation'][seg_WPc_nodes_trib], 'r--', linewidth = 0.5)
plt.plot(seg_WPc_distance_trib / 1000, mg.at_node['bedrock__elevation'][seg_WPc_nodes_trib], 'k--', linewidth = 0.5)
plt.plot(seg_WPd_distance_trib / 1000, mg.at_node['topographic__elevation'][seg_WPd_nodes_trib], 'r--', linewidth = 0.5)
plt.plot(seg_WPd_distance_trib / 1000, mg.at_node['bedrock__elevation'][seg_WPd_nodes_trib], 'k--', linewidth = 0.5)
plt.grid()
plt.xlabel('Distance (km)')
plt.ylabel('Elevation (m)')
plt.title('t = 0 years')
plt.legend(['Topographic elevation', 'Bedrock elevation'], loc = 'upper left')
plt.tight_layout()
fig.savefig('Output_Run_K1ldevelopcal/Segs/Zones/Zone_2/0.'+Export_format,  format=Export_format, dpi=dpi)
xlim_Zone_2 = plt.xlim()
ylim_Zone_2 = plt.ylim()
plt.close(fig)

# Plot Zone 3
fig = plt.figure()
plt.plot(seg_MS_zone_3_distance / 1000, mg.at_node['topographic__elevation'][seg_MS_zone_3_nodes], 'r--', linewidth = 0.5)
plt.plot(seg_MS_zone_3_distance / 1000, mg.at_node['bedrock__elevation'][seg_MS_zone_3_nodes], 'k--', linewidth = 0.5)
plt.plot(seg_HDa_distance_trib / 1000, mg.at_node['topographic__elevation'][seg_HDa_nodes_trib], 'r--', linewidth = 0.5)
plt.plot(seg_HDa_distance_trib / 1000, mg.at_node['bedrock__elevation'][seg_HDa_nodes_trib], 'k--', linewidth = 0.5)
plt.plot(seg_HDb_distance_trib / 1000, mg.at_node['topographic__elevation'][seg_HDb_nodes_trib], 'r--', linewidth = 0.5)
plt.plot(seg_HDb_distance_trib / 1000, mg.at_node['bedrock__elevation'][seg_HDb_nodes_trib], 'k--', linewidth = 0.5)
plt.plot(seg_GRa_distance_trib / 1000, mg.at_node['topographic__elevation'][seg_GRa_nodes_trib], 'r--', linewidth = 0.5)
plt.plot(seg_GRa_distance_trib / 1000, mg.at_node['bedrock__elevation'][seg_GRa_nodes_trib], 'k--', linewidth = 0.5)
plt.plot(seg_OVa_distance_trib / 1000, mg.at_node['topographic__elevation'][seg_OVa_nodes_trib], 'r--', linewidth = 0.5)
plt.plot(seg_OVa_distance_trib / 1000, mg.at_node['bedrock__elevation'][seg_OVa_nodes_trib], 'k--', linewidth = 0.5)
plt.grid()
plt.xlabel('Distance (km)')
plt.ylabel('Elevation (m)')
plt.title('t = 0 years')
plt.legend(['Topographic elevation', 'Bedrock elevation'], loc = 'upper left')
plt.tight_layout()
fig.savefig('Output_Run_K1ldevelopcal/Segs/Zones/Zone_3/0.'+Export_format,  format=Export_format, dpi=dpi)
xlim_Zone_3 = plt.xlim()
ylim_Zone_3 = plt.ylim()
plt.close(fig)

# Plot Zone 4
fig = plt.figure()
plt.plot(seg_MS_zone_4_distance / 1000, mg.at_node['topographic__elevation'][seg_MS_zone_4_nodes], 'r--', linewidth = 0.5)
plt.plot(seg_MS_zone_4_distance / 1000, mg.at_node['bedrock__elevation'][seg_MS_zone_4_nodes], 'k--', linewidth = 0.5)
plt.plot(seg_WGa_distance_trib / 1000, mg.at_node['topographic__elevation'][seg_WGa_nodes_trib], 'r--', linewidth = 0.5)
plt.plot(seg_WGa_distance_trib / 1000, mg.at_node['bedrock__elevation'][seg_WGa_nodes_trib], 'k--', linewidth = 0.5)
plt.plot(seg_WGb_distance_trib / 1000, mg.at_node['topographic__elevation'][seg_WGb_nodes_trib], 'r--', linewidth = 0.5)
plt.plot(seg_WGb_distance_trib / 1000, mg.at_node['bedrock__elevation'][seg_WGb_nodes_trib], 'k--', linewidth = 0.5)
plt.plot(seg_WGc_distance_trib / 1000, mg.at_node['topographic__elevation'][seg_WGc_nodes_trib], 'r--', linewidth = 0.5)
plt.plot(seg_WGc_distance_trib / 1000, mg.at_node['bedrock__elevation'][seg_WGc_nodes_trib], 'k--', linewidth = 0.5)
plt.plot(seg_WGd_distance_trib / 1000, mg.at_node['topographic__elevation'][seg_WGd_nodes_trib], 'r--', linewidth = 0.5)
plt.plot(seg_WGd_distance_trib / 1000, mg.at_node['bedrock__elevation'][seg_WGd_nodes_trib], 'k--', linewidth = 0.5)
plt.plot(seg_WGe_distance_trib / 1000, mg.at_node['topographic__elevation'][seg_WGe_nodes_trib], 'r--', linewidth = 0.5)
plt.plot(seg_WGe_distance_trib / 1000, mg.at_node['bedrock__elevation'][seg_WGe_nodes_trib], 'k--', linewidth = 0.5)
plt.plot(seg_WGf_distance_trib / 1000, mg.at_node['topographic__elevation'][seg_WGf_nodes_trib], 'r--', linewidth = 0.5)
plt.plot(seg_WGf_distance_trib / 1000, mg.at_node['bedrock__elevation'][seg_WGf_nodes_trib], 'k--', linewidth = 0.5)
plt.grid()
plt.xlabel('Distance (km)')
plt.ylabel('Elevation (m)')
plt.title('t = 0 years')
plt.legend(['Topographic elevation', 'Bedrock elevation'], loc = 'upper left')
plt.tight_layout()
fig.savefig('Output_Run_K1ldevelopcal/Segs/Zones/Zone_4/0.'+Export_format,  format=Export_format, dpi=dpi)
xlim_Zone_4 = plt.xlim()
ylim_Zone_4 = plt.ylim()
plt.close(fig)

# Plot Zone 5
fig = plt.figure()
plt.plot(seg_MS_zone_5_distance / 1000, mg.at_node['topographic__elevation'][seg_MS_zone_5_nodes], 'r--', linewidth = 0.5)
plt.plot(seg_MS_zone_5_distance / 1000, mg.at_node['bedrock__elevation'][seg_MS_zone_5_nodes], 'k--', linewidth = 0.5)
plt.plot(seg_SMa_distance_trib / 1000, mg.at_node['topographic__elevation'][seg_SMa_nodes_trib], 'r--', linewidth = 0.5)
plt.plot(seg_SMa_distance_trib / 1000, mg.at_node['bedrock__elevation'][seg_SMa_nodes_trib], 'k--', linewidth = 0.5)
plt.plot(seg_SMb_distance_trib / 1000, mg.at_node['topographic__elevation'][seg_SMb_nodes_trib], 'r--', linewidth = 0.5)
plt.plot(seg_SMb_distance_trib / 1000, mg.at_node['bedrock__elevation'][seg_SMb_nodes_trib], 'k--', linewidth = 0.5)
plt.plot(seg_SMc_distance_trib / 1000, mg.at_node['topographic__elevation'][seg_SMc_nodes_trib], 'r--', linewidth = 0.5)
plt.plot(seg_SMc_distance_trib / 1000, mg.at_node['bedrock__elevation'][seg_SMc_nodes_trib], 'k--', linewidth = 0.5)
plt.plot(seg_SMd_distance_trib / 1000, mg.at_node['topographic__elevation'][seg_SMd_nodes_trib], 'r--', linewidth = 0.5)
plt.plot(seg_SMd_distance_trib / 1000, mg.at_node['bedrock__elevation'][seg_SMd_nodes_trib], 'k--', linewidth = 0.5)
plt.grid()
plt.xlabel('Distance (km)')
plt.ylabel('Elevation (m)')
plt.title('t = 0 years')
plt.legend(['Topographic elevation', 'Bedrock elevation'], loc = 'upper left')
plt.tight_layout()
fig.savefig('Output_Run_K1ldevelopcal/Segs/Zones/Zone_5/0.'+Export_format,  format=Export_format, dpi=dpi)
xlim_Zone_5 = plt.xlim()
ylim_Zone_5 = plt.ylim()
plt.close(fig)

# Plot Overview Map
fig = plt.figure()  
#
ax = imshowhs_grid(mg, "topographic__elevation", plot_type='Drape1', drape1=mg.at_node['topographic__elevation'],cmap='terrain',alpha=alpha,color_for_background='k',color_for_closed='k',allow_colorbar=True,cbar_loc="right",cbar_or='vertical',bbox_to_anchor=(1.05, 0.0, 0.03, 1.0),cbar_width="100%", cbar_height="100%", var_name='Elevation (m)', colorbar_label_x=1.5, colorbar_label_y=0.5, cbar_label_fontweight='regular', add_label_bbox=False)
formatter = ScalarFormatter()
formatter.set_powerlimits((-3, 3))  # Switch to scientific notation if the range is <10^-3 or >10^3
ax.xaxis.set_major_formatter(formatter)
#
ax.plot(mg.x_of_node[seg_SMa_nodes], mg.y_of_node[seg_SMa_nodes], color = 'magenta', marker = '.', markersize = 1.5)
ax.plot(mg.x_of_node[seg_SMb_nodes], mg.y_of_node[seg_SMb_nodes], color = 'magenta', marker = '.', markersize = 1.5)
ax.plot(mg.x_of_node[seg_SMc_nodes], mg.y_of_node[seg_SMc_nodes], color = 'magenta', marker = '.', markersize = 1.5)
ax.plot(mg.x_of_node[seg_SMd_nodes], mg.y_of_node[seg_SMd_nodes], color = 'magenta', marker = '.', markersize = 1.5)
ax.plot(mg.x_of_node[seg_WGa_nodes], mg.y_of_node[seg_WGa_nodes], color = 'cyan', marker = '.', markersize = 1.5)
ax.plot(mg.x_of_node[seg_WGb_nodes], mg.y_of_node[seg_WGb_nodes], color = 'cyan', marker = '.', markersize = 1.5)
ax.plot(mg.x_of_node[seg_WGc_nodes], mg.y_of_node[seg_WGc_nodes], color = 'cyan', marker = '.', markersize = 1.5)
ax.plot(mg.x_of_node[seg_WGd_nodes], mg.y_of_node[seg_WGd_nodes], color = 'cyan', marker = '.', markersize = 1.5)
ax.plot(mg.x_of_node[seg_WGe_nodes], mg.y_of_node[seg_WGe_nodes], color = 'cyan', marker = '.', markersize = 1.5)
ax.plot(mg.x_of_node[seg_WGf_nodes], mg.y_of_node[seg_WGf_nodes], color = 'cyan', marker = '.', markersize = 1.5)
ax.plot(mg.x_of_node[seg_OVa_nodes], mg.y_of_node[seg_OVa_nodes], color = 'green', marker = '.', markersize = 1.5)
ax.plot(mg.x_of_node[seg_GRa_nodes], mg.y_of_node[seg_GRa_nodes], color = 'yellow', marker = '.', markersize = 1.5)
ax.plot(mg.x_of_node[seg_HDb_nodes], mg.y_of_node[seg_HDb_nodes], color = 'orange', marker = '.', markersize = 1.5)
ax.plot(mg.x_of_node[seg_HDa_nodes], mg.y_of_node[seg_HDa_nodes], color = 'orange', marker = '.', markersize = 1.5)
ax.plot(mg.x_of_node[seg_WPd_nodes], mg.y_of_node[seg_WPd_nodes], color = 'red', marker = '.', markersize = 1.5)
ax.plot(mg.x_of_node[seg_WPc_nodes], mg.y_of_node[seg_WPc_nodes], color = 'red', marker = '.', markersize = 1.5)
ax.plot(mg.x_of_node[seg_WPb_nodes], mg.y_of_node[seg_WPb_nodes], color = 'red', marker = '.', markersize = 1.5)
ax.plot(mg.x_of_node[seg_WPa_nodes], mg.y_of_node[seg_WPa_nodes], color = 'red', marker = '.', markersize = 1.5)
ax.plot(mg.x_of_node[seg_MS_nodes], mg.y_of_node[seg_MS_nodes], 'b.', markersize = 1.5)
#
rect_1 = Rectangle((Zone_1_X[0], Zone_1_Y[0]), Zone_1_X[1] - Zone_1_X[0], Zone_1_Y[1] - Zone_1_Y[0], fill=False, edgecolor='red', linewidth=2)
rect_2 = Rectangle((Zone_2_X[0], Zone_2_Y[0]), Zone_2_X[1] - Zone_2_X[0], Zone_2_Y[1] - Zone_2_Y[0], fill=False, edgecolor='red', linewidth=2)
rect_3 = Rectangle((Zone_3_X[0], Zone_3_Y[0]), Zone_3_X[1] - Zone_3_X[0], Zone_3_Y[1] - Zone_3_Y[0], fill=False, edgecolor='red', linewidth=2)
rect_4 = Rectangle((Zone_4_X[0], Zone_4_Y[0]), Zone_4_X[1] - Zone_4_X[0], Zone_4_Y[1] - Zone_4_Y[0], fill=False, edgecolor='red', linewidth=2)
rect_5 = Rectangle((Zone_5_X[0], Zone_5_Y[0]), Zone_5_X[1] - Zone_5_X[0], Zone_5_Y[1] - Zone_5_Y[0], fill=False, edgecolor='red', linewidth=2)
#
ax.add_patch(rect_1)
ax.add_patch(rect_2)
ax.add_patch(rect_3)
ax.add_patch(rect_4)
ax.add_patch(rect_5)
#
plt.tight_layout()
fig.savefig('Output_Run_K1ldevelopcal/Overview_Map/Overview_Map.'+Export_format,  format=Export_format, dpi=dpi)
plt.close(fig)

# Section break
print(' ')

#%% Handle dams

# Print status
print('Handling dams...')

# Initiate Upstream (flooded node array, all reservoirs)
Upstream = []
dam_nodes = []

# D1 (Buford Dam, Lake Lanier)
D1_upstream = []
receivers = mg.at_node["flow__receiver_node"]
donors = defaultdict(list)
for node, rec in enumerate(receivers):
    if node != rec:          # ignore pits/self receivers
        donors[rec].append(node)
D1_upstream = upstream_nodes(dam_node_Lanier)
D1_upstream = D1_upstream[np.where(mg.at_node['topographic__elevation'][D1_upstream] < WL_Lanier)]

# D2 (West Point Dam and Lake)
D2_upstream = []
receivers = mg.at_node["flow__receiver_node"]
donors = defaultdict(list)
for node, rec in enumerate(receivers):
    if node != rec:          # ignore pits/self receivers
        donors[rec].append(node)
D2_upstream = upstream_nodes(dam_node_WestPoint)
D2_upstream = D2_upstream[np.where(mg.at_node['topographic__elevation'][D2_upstream] < WL_WestPoint)]

# D3 (Bartlet's Ferry Dam and Harding Lake)
D3_upstream = []
receivers = mg.at_node["flow__receiver_node"]
donors = defaultdict(list)
for node, rec in enumerate(receivers):
    if node != rec:          # ignore pits/self receivers
        donors[rec].append(node)
D3_upstream = upstream_nodes(dam_node_Harding)
D3_upstream = D3_upstream[np.where(mg.at_node['topographic__elevation'][D3_upstream] < WL_Harding)]

# D4 (Goat Rock Lake and Dam)
D4_upstream = []
receivers = mg.at_node["flow__receiver_node"]
donors = defaultdict(list)
for node, rec in enumerate(receivers):
    if node != rec:          # ignore pits/self receivers
        donors[rec].append(node)
D4_upstream = upstream_nodes(dam_node_GoatRock)
D4_upstream = D4_upstream[np.where(mg.at_node['topographic__elevation'][D4_upstream] < WL_GoatRock)]

# D5 (Oliver Lake and Dam)
D5_upstream = []
receivers = mg.at_node["flow__receiver_node"]
donors = defaultdict(list)
for node, rec in enumerate(receivers):
    if node != rec:          # ignore pits/self receivers
        donors[rec].append(node)
D5_upstream = upstream_nodes(dam_node_Oliver)
D5_upstream = D5_upstream[np.where(mg.at_node['topographic__elevation'][D5_upstream] < WL_Oliver)]

# D6 (WFG Lake and Dam)
D6_upstream = []
receivers = mg.at_node["flow__receiver_node"]
donors = defaultdict(list)
for node, rec in enumerate(receivers):
    if node != rec:          # ignore pits/self receivers
        donors[rec].append(node)
D6_upstream = upstream_nodes(dam_node_WFG)
D6_upstream = D6_upstream[np.where(mg.at_node['topographic__elevation'][D6_upstream] < WL_WFG)]

# D7 (Woodruff Dam and Lake Seminole)
D7_upstream = []
receivers = mg.at_node["flow__receiver_node"]
donors = defaultdict(list)
for node, rec in enumerate(receivers):
    if node != rec:          # ignore pits/self receivers
        donors[rec].append(node)
D7_upstream = upstream_nodes(dam_node_Seminole)
D7_upstream = D7_upstream[np.where(mg.at_node['topographic__elevation'][D7_upstream] < WL_Seminole)]

# Section break
print(' ')

#%% Set clocks

# Print 
print('Setting clocks...')

# Zero clocks
total_time = 0 
Plot_Ticker = 0
Export_DEM_Ticker = 0
timestep_integer = 0

# Set t
t = np.arange(0, tmax, dt) 

# Set tickers
Plot_Ticker = 0
Export_DEM_Ticker = 0
total_time_r = 0

# Section break
print(' ')

#%% Initialize components and parameter trackers

# Print status
print('Initializing components and parameter trackers...')

# Initialize SPACE
spr = SpaceLargeScaleEroder(mg, K_sed = K1, K_br = K_br, F_f = 0.0, phi = 0.3, H_star = 0.1, v_s = 300, v_s_lake = None, m_sp = m_sp, n_sp = n_sp, sp_crit_sed = 0.0, sp_crit_br = 0.0, discharge_field = "surface_water__discharge", erode_flooded_nodes = False, thickness_lim = 100)

# Initialize ErosionElevationTracker
eet = EET.ErosionElevationTracker(mg, bedrock__and__soil = True)

# Initialize appendable arrays
timesteps = []
times = []
#
z_means = []
z_medians = []
z_2s = []
z_98s = []
z_mins = []
z_maxs = []
#
dbedelevdt_means = []
dbedelevdt_medians = []
dbedelevdt_2s = []
dbedelevdt_98s = []
dbedelevdt_mins = []
dbedelevdt_maxs = []
#
dsoildepthdt_means = []
dsoildepthdt_medians = []
dsoildepthdt_2s = []
dsoildepthdt_98s = []
dsoildepthdt_mins = []
dsoildepthdt_maxs = []
#
dzdt_means = []
dzdt_medians = []
dzdt_2s = []
dzdt_98s = []
dzdt_mins = []
dzdt_maxs = []
#
erosionrate_means = []
erosionrate_medians = []
erosionrate_2s = []
erosionrate_98s = []
erosionrate_mins = []
erosionrate_maxs = []
#
netdz_means = []
netdz_medians = []
netdz_2s = []
netdz_98s = []
netdz_mins = []
netdz_maxs = []
#
sediment_flux_gauge_A = []
sediment_flux_gauge_B = []
sediment_flux_gauge_C = []
sediment_flux_gauge_D = []
sediment_flux_gauge_E = []
sediment_flux_gauge_F = []
sediment_flux_gauge_G = []
sediment_flux_gauge_H = []
sediment_flux_outlet = []
#
D1_dvol = []
D2_dvol = []
D3_dvol = []
D4_dvol = []
D5_dvol = []
D6_dvol = []
D7_dvol = []

# Section break
print(' ')

#%% Time loop
 
# Print status
print('Starting time loop...')

# Time loop
for ti in t:
      
    # Uplift topograpghy
    mg.at_node['bedrock__elevation'][mg.core_nodes] += U[mg.core_nodes] * dt    
    mg.at_node['topographic__elevation'][mg.core_nodes] = mg.at_node['bedrock__elevation'][mg.core_nodes] + mg.at_node['soil__depth'][mg.core_nodes]

    # Activate Goat Rock Dam (4) in 1912
    if total_time_r == start_GoatRock:
        Upstream = np.append(Upstream, D4_upstream)
        Upstream = Upstream.astype('int')
        dam_nodes = np.append(dam_nodes, dam_node_GoatRock)
        dam_nodes = dam_nodes.astype('int')
        
    # Activate Bartlet's Ferry Dam (3) in 1926
    if total_time_r == start_Harding:
        Upstream = np.append(Upstream, D3_upstream)
        Upstream = Upstream.astype('int')
        dam_nodes = np.append(dam_nodes, dam_node_Harding)
        dam_nodes = dam_nodes.astype('int')
        
    # Activate Woodruff Dam (7) in 1954
    if total_time_r == start_Seminole:
        Upstream = np.append(Upstream, D7_upstream)
        Upstream = Upstream.astype('int')
        dam_nodes = np.append(dam_nodes, pour_point_node)
        dam_nodes = dam_nodes.astype('int')
        
    # Activate Bufford Dam (1) in 1956
    if total_time_r == start_Lanier:
        Upstream = np.append(Upstream, D1_upstream)
        Upstream = Upstream.astype('int')
        dam_nodes = np.append(dam_nodes, dam_node_Lanier)
        dam_nodes = dam_nodes.astype('int')
        
    # Activate Oliver Dam (5) in 1959
    if total_time_r == start_Oliver:
        Upstream = np.append(Upstream, D5_upstream)
        Upstream = Upstream.astype('int')
        dam_nodes = np.append(dam_nodes, dam_node_Oliver)
        dam_nodes = dam_nodes.astype('int')
        
    # Activate WFG Dam (6) in 1963
    if total_time_r == start_WFG:
        Upstream = np.append(Upstream, D6_upstream)
        Upstream = Upstream.astype('int')
        dam_nodes = np.append(dam_nodes, dam_node_WFG)
        dam_nodes = dam_nodes.astype('int')
        
    # Activate West Point Dam (2) in 1974
    if total_time_r == start_WestPoint:
        Upstream = np.append(Upstream, D2_upstream)
        Upstream = Upstream.astype('int')
        dam_nodes = np.append(dam_nodes, dam_node_WestPoint)
        dam_nodes = dam_nodes.astype('int')
    
    # Run one steps                       
    frr.run_one_step()   
    mg.at_node['surface_water__discharge'][Upstream] = dxy ** 2                             
    spr.run_one_step(dt)
    eet.run_one_step(dt, uplift = Be10_Uplift * dt)

    # Calculate dz_dt and erosion rate metrics
    dbedelevdt = eet.return_dbedelevdt()
    dsoildepthdt = eet.return_dsoildepthdt()    
    dzdt = eet.return_dzdt()
    erosionrate = eet.return_erosionrate()
    netdz = mg.at_node['topographic__elevation'] - zr0
    
    # Correct for no_data_nodes
    z_adjust = np.copy(mg.at_node['topographic__elevation'])
    z_adjust[no_data_nodes] = nan
    dbedelevdt_adjust = np.copy(dbedelevdt)
    dbedelevdt_adjust[no_data_nodes] = nan
    dsoildepthdt_adjust = np.copy(dsoildepthdt)
    dsoildepthdt_adjust[no_data_nodes] = nan
    dzdt_adjust = np.copy(dzdt)
    dzdt_adjust[no_data_nodes] = nan
    erosionrate_adjust = np.copy(erosionrate)
    erosionrate_adjust[no_data_nodes] = nan
    netdz_adjust = np.copy(netdz)
    netdz_adjust[no_data_nodes] = nan
    
    # Append timestep stats
    timesteps = np.append(timesteps, timestep_integer)
    times = timesteps * dt
    #
    z_means = np.append(z_means, np.nanmean(z_adjust))
    z_medians = np.append(z_medians, np.nanmedian(z_adjust))
    z_2s = np.append(z_2s, np.nanpercentile(z_adjust, 2.3))
    z_98s = np.append(z_98s, np.nanpercentile(z_adjust, 97.7))
    z_mins = np.append(z_mins, np.nanmin(z_adjust))
    z_maxs = np.append(z_maxs, np.nanmax(z_adjust))
    #
    dbedelevdt_means = np.append(dbedelevdt_means, np.nanmean(dbedelevdt_adjust))
    dbedelevdt_medians = np.append(dbedelevdt_medians, np.nanmedian(dbedelevdt_adjust))
    dbedelevdt_2s = np.append(dbedelevdt_2s, np.nanpercentile(dbedelevdt_adjust, 2.3))
    dbedelevdt_98s = np.append(dbedelevdt_98s, np.nanpercentile(dbedelevdt_adjust, 97.7))
    dbedelevdt_mins = np.append(dbedelevdt_mins, np.nanmin(dbedelevdt_adjust))
    dbedelevdt_maxs = np.append(dbedelevdt_maxs, np.nanmax(dbedelevdt_adjust))
    #
    dsoildepthdt_means = np.append(dsoildepthdt_means, np.nanmean(dsoildepthdt_adjust))
    dsoildepthdt_medians = np.append(dsoildepthdt_medians, np.nanmedian(dsoildepthdt_adjust))
    dsoildepthdt_2s = np.append(dsoildepthdt_2s, np.nanpercentile(dsoildepthdt_adjust, 2.3))
    dsoildepthdt_98s = np.append(dsoildepthdt_98s, np.nanpercentile(dsoildepthdt_adjust, 97.7))
    dsoildepthdt_mins = np.append(dsoildepthdt_mins, np.nanmin(dsoildepthdt_adjust))
    dsoildepthdt_maxs = np.append(dsoildepthdt_maxs, np.nanmax(dsoildepthdt_adjust))
    #
    dzdt_means = np.append(dzdt_means, np.nanmean(dzdt_adjust))
    dzdt_medians = np.append(dzdt_medians, np.nanmedian(dzdt_adjust))
    dzdt_2s = np.append(dzdt_2s, np.nanpercentile(dzdt_adjust, 2.3))
    dzdt_98s = np.append(dzdt_98s, np.nanpercentile(dzdt_adjust, 97.7))
    dzdt_mins = np.append(dzdt_mins, np.nanmin(dzdt_adjust))
    dzdt_maxs = np.append(dzdt_maxs, np.nanmax(dzdt_adjust))
    #
    erosionrate_means = np.append(erosionrate_means, np.nanmean(erosionrate_adjust))
    erosionrate_medians = np.append(erosionrate_medians, np.nanmedian(erosionrate_adjust))
    erosionrate_2s = np.append(erosionrate_2s, np.nanpercentile(erosionrate_adjust, 2.3))
    erosionrate_98s = np.append(erosionrate_98s, np.nanpercentile(erosionrate_adjust, 97.7))
    erosionrate_mins = np.append(erosionrate_mins, np.nanmin(erosionrate_adjust))
    erosionrate_maxs = np.append(erosionrate_maxs, np.nanmax(erosionrate_adjust))
    #
    netdz_means = np.append(netdz_means, np.nanmean(netdz_adjust))
    netdz_medians = np.append(netdz_medians, np.nanmedian(netdz_adjust))
    netdz_2s = np.append(netdz_2s, np.nanpercentile(netdz_adjust, 2.3))
    netdz_98s = np.append(netdz_98s, np.nanpercentile(netdz_adjust, 97.7))
    netdz_mins = np.append(netdz_mins, np.nanmin(netdz_adjust))
    netdz_maxs = np.append(netdz_maxs, np.nanmax(netdz_adjust))

    # Append fluxes
    sediment_flux_gauge_A = np.append(sediment_flux_gauge_A, np.max(mg.at_node['sediment__flux'][gauge_radius_nodes_A]))
    sediment_flux_gauge_B = np.append(sediment_flux_gauge_B, np.max(mg.at_node['sediment__flux'][gauge_radius_nodes_B]))
    sediment_flux_gauge_C = np.append(sediment_flux_gauge_C, np.max(mg.at_node['sediment__flux'][gauge_radius_nodes_C]))
    sediment_flux_gauge_D = np.append(sediment_flux_gauge_D, np.max(mg.at_node['sediment__flux'][gauge_radius_nodes_D]))
    sediment_flux_gauge_E = np.append(sediment_flux_gauge_E, np.max(mg.at_node['sediment__flux'][gauge_radius_nodes_E]))
    sediment_flux_gauge_F = np.append(sediment_flux_gauge_F, np.max(mg.at_node['sediment__flux'][gauge_radius_nodes_F]))
    sediment_flux_gauge_G = np.append(sediment_flux_gauge_G, np.max(mg.at_node['sediment__flux'][gauge_radius_nodes_G]))
    sediment_flux_gauge_H = np.append(sediment_flux_gauge_H, np.max(mg.at_node['sediment__flux'][gauge_radius_nodes_H]))
    sediment_flux_outlet = np.append(sediment_flux_outlet, np.max(mg.at_node['sediment__flux'][outlet_radius_nodes]))
    
    # Get current rate of reservoir volume change (m^3 / year)
    D1_dvol_i = np.sum(erosionrate[D1_upstream]) * dxy * dxy
    D2_dvol_i = np.sum(erosionrate[D2_upstream]) * dxy * dxy
    D3_dvol_i = np.sum(erosionrate[D3_upstream]) * dxy * dxy
    D4_dvol_i = np.sum(erosionrate[D4_upstream]) * dxy * dxy
    D5_dvol_i = np.sum(erosionrate[D5_upstream]) * dxy * dxy
    D6_dvol_i = np.sum(erosionrate[D6_upstream]) * dxy * dxy
    D7_dvol_i = np.sum(erosionrate[D7_upstream]) * dxy * dxy

    # Append rates of reservoir volume change (m^3 / year)
    D1_dvol = np.append(D1_dvol, D1_dvol_i)
    D2_dvol = np.append(D2_dvol, D2_dvol_i)
    D3_dvol = np.append(D3_dvol, D3_dvol_i)
    D4_dvol = np.append(D4_dvol, D4_dvol_i)
    D5_dvol = np.append(D5_dvol, D5_dvol_i)
    D6_dvol = np.append(D6_dvol, D6_dvol_i)
    D7_dvol = np.append(D7_dvol, D7_dvol_i)
    
    # Provenance Tracking Scheme Here
    
    # Update time
    total_time += dt                                    
    Plot_Ticker += dt
    Export_DEM_Ticker += dt
    timestep_integer += 1
    total_time_r = np.round(total_time, decimals = 1)
    print(total_time_r)

    # Plots
    if Plot_Ticker >= Plot_interval - 0.0000000001:
        print('Exporting figures... Please be patient!')
        
        # Plot__topographic__elevation
        if Plot__topographic__elevation == True:
            #
            fig = plt.figure()       
            ax = imshowhs_grid(mg, "topographic__elevation", plot_type='Drape1', drape1=mg.at_node['topographic__elevation'],cmap='terrain',alpha=alpha,color_for_background='k',color_for_closed='k',allow_colorbar=True,cbar_loc="right",cbar_or='vertical',bbox_to_anchor=(1.05, 0.0, 0.03, 1.0),cbar_width="100%", cbar_height="100%", var_name='Elevation (m)', colorbar_label_x=1.5, colorbar_label_y=0.5, cbar_label_fontweight='regular', add_label_bbox=False)
            ax.set_title('$Year$=' + str(total_time_r), fontsize=12, loc='center', pad=20)
            formatter = ScalarFormatter()
            formatter.set_powerlimits((-3, 3))  # Switch to scientific notation if the range is <10^-3 or >10^3
            ax.xaxis.set_major_formatter(formatter)
            # ax.plot(mg.x_of_node[seg_SMa_nodes], mg.y_of_node[seg_SMa_nodes], color = 'magenta', marker = '.', markersize = 1.5)
            # ax.plot(mg.x_of_node[seg_SMb_nodes], mg.y_of_node[seg_SMb_nodes], color = 'magenta', marker = '.', markersize = 1.5)
            # ax.plot(mg.x_of_node[seg_SMc_nodes], mg.y_of_node[seg_SMc_nodes], color = 'magenta', marker = '.', markersize = 1.5)
            # ax.plot(mg.x_of_node[seg_SMd_nodes], mg.y_of_node[seg_SMd_nodes], color = 'magenta', marker = '.', markersize = 1.5)
            # ax.plot(mg.x_of_node[seg_WGa_nodes], mg.y_of_node[seg_WGa_nodes], color = 'cyan', marker = '.', markersize = 1.5)
            # ax.plot(mg.x_of_node[seg_WGb_nodes], mg.y_of_node[seg_WGb_nodes], color = 'cyan', marker = '.', markersize = 1.5)
            # ax.plot(mg.x_of_node[seg_WGc_nodes], mg.y_of_node[seg_WGc_nodes], color = 'cyan', marker = '.', markersize = 1.5)
            # ax.plot(mg.x_of_node[seg_WGd_nodes], mg.y_of_node[seg_WGd_nodes], color = 'cyan', marker = '.', markersize = 1.5)
            # ax.plot(mg.x_of_node[seg_WGe_nodes], mg.y_of_node[seg_WGe_nodes], color = 'cyan', marker = '.', markersize = 1.5)
            # ax.plot(mg.x_of_node[seg_WGf_nodes], mg.y_of_node[seg_WGf_nodes], color = 'cyan', marker = '.', markersize = 1.5)
            # ax.plot(mg.x_of_node[seg_OVa_nodes], mg.y_of_node[seg_OVa_nodes], color = 'green', marker = '.', markersize = 1.5)
            # ax.plot(mg.x_of_node[seg_GRa_nodes], mg.y_of_node[seg_GRa_nodes], color = 'yellow', marker = '.', markersize = 1.5)
            # ax.plot(mg.x_of_node[seg_HDb_nodes], mg.y_of_node[seg_HDb_nodes], color = 'orange', marker = '.', markersize = 1.5)
            # ax.plot(mg.x_of_node[seg_HDa_nodes], mg.y_of_node[seg_HDa_nodes], color = 'orange', marker = '.', markersize = 1.5)
            # ax.plot(mg.x_of_node[seg_WPd_nodes], mg.y_of_node[seg_WPd_nodes], color = 'red', marker = '.', markersize = 1.5)
            # ax.plot(mg.x_of_node[seg_WPc_nodes], mg.y_of_node[seg_WPc_nodes], color = 'red', marker = '.', markersize = 1.5)
            # ax.plot(mg.x_of_node[seg_WPb_nodes], mg.y_of_node[seg_WPb_nodes], color = 'red', marker = '.', markersize = 1.5)
            # ax.plot(mg.x_of_node[seg_WPa_nodes], mg.y_of_node[seg_WPa_nodes], color = 'red', marker = '.', markersize = 1.5)
            # ax.plot(mg.x_of_node[seg_MS_nodes], mg.y_of_node[seg_MS_nodes], 'b.', markersize = 1.5)
            ax.plot(mg.x_of_node[dam_nodes], mg.y_of_node[dam_nodes], 'rs')
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/topographic__elevation_Map/Full/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)
            #
            ax.set_xlim(Zone_1_X)
            ax.set_ylim(Zone_1_Y)   
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/topographic__elevation_Map/Zone_1/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)  
            #
            ax.set_xlim(Zone_2_X)
            ax.set_ylim(Zone_2_Y)
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/topographic__elevation_Map/Zone_2/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)   
            #
            ax.set_xlim(Zone_3_X)
            ax.set_ylim(Zone_3_Y)    
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/topographic__elevation_Map/Zone_3/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)
            #
            ax.set_xlim(Zone_4_X)
            ax.set_ylim(Zone_4_Y)    
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/topographic__elevation_Map/Zone_4/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)
            #
            ax.set_xlim(Zone_5_X)
            ax.set_ylim(Zone_5_Y)    
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/topographic__elevation_Map/Zone_5/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)
            #
            plt.close(fig) 
            # 
            fig = plt.figure()
            plt.plot(times, z_means, color = 'blue', zorder = 4) 
            plt.plot(times, z_medians, color = 'red', zorder = 4)
            plt.fill_between(times, z_2s, z_98s, alpha=0.50, color = 'blue', zorder = 3)
            plt.xlabel('Model year')
            plt.ylabel("Elevation (m)")
            plt.grid()
            plt.legend(['Mean', 'Median', "2σ"], loc='upper left', framealpha = 1)
            fig.savefig('Output_Run_K1ldevelopcal/topographic__elevation_timeseries/topographic__elevation_timeseries.'+Export_format,  format=Export_format, dpi=dpi)
            #
            plt.close(fig)
            
        # Plot__dbedelevdt
        if Plot__dbedelevdt == True:
            #
            fig, ax = plt.subplots()
            drape1 = dbedelevdt
            cmap = 'PRGn'
            label = "d(bed elevation) dt⁻¹ (m yr⁻¹)"
            vmin = -np.percentile(np.abs(drape1), mapping_percentile)
            vmax = np.percentile(np.abs(drape1), mapping_percentile)
            im = imshowhs_grid(mg, "topographic__elevation", plot_type='Drape1', drape1=drape1, cmap=cmap, alpha=alpha, color_for_background='k', color_for_closed='k', allow_colorbar=False, cbar_loc="right", cbar_or='vertical', bbox_to_anchor=(1.05, 0.0, 0.03, 1.0), cbar_width="100%", cbar_height="100%", var_name='Bedrock elevation (m)', colorbar_label_x=1.5, colorbar_label_y=0.5, cbar_label_fontweight='regular', add_label_bbox=False, vmin = vmin, vmax = vmax)
            ax.plot(mg.x_of_node[dam_nodes], mg.y_of_node[dam_nodes], 'rs')
            ticks = np.linspace(vmin, vmax, 7)            
            sm = plt.cm.ScalarMappable(cmap=cmap, norm=mcolors.Normalize(vmin=vmin, vmax=vmax))
            sm.set_array([])  # No data, just for colorbar
            cbar = fig.colorbar(sm, ax=ax, ticks=ticks)
            cbar.set_label(label, fontsize=12)
            ax.set_title('$Year$=' + str(total_time_r), fontsize=12, loc='center', pad=20)
            formatter = ScalarFormatter()
            formatter.set_powerlimits((-3, 3))  # Switch to scientific notation if the range is <10^-3 or >10^3
            ax.xaxis.set_major_formatter(formatter)
            cbar.ax.yaxis.set_major_formatter(FuncFormatter(sci_notation_format))
            #
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/dbedelevdt_Map/Full/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)
            #
            ax.set_xlim(Zone_1_X)
            ax.set_ylim(Zone_1_Y)  
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/dbedelevdt_Map/Zone_1/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)  
            #
            ax.set_xlim(Zone_2_X)
            ax.set_ylim(Zone_2_Y) 
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/dbedelevdt_Map/Zone_2/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)   
            #
            ax.set_xlim(Zone_3_X)
            ax.set_ylim(Zone_3_Y)    
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/dbedelevdt_Map/Zone_3/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)
            #
            ax.set_xlim(Zone_4_X)
            ax.set_ylim(Zone_4_Y)    
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/dbedelevdt_Map/Zone_4/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)
            #
            ax.set_xlim(Zone_5_X)
            ax.set_ylim(Zone_5_Y)    
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/dbedelevdt_Map/Zone_5/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)
            #
            plt.close(fig)  
            #
            if path.exists('Output_Run_K1ldevelopcal/dbedelevdt_timeseries') == False:
                os.mkdir('Output_Run_K1ldevelopcal/dbedelevdt_timeseries')  
            fig = plt.figure()
            plt.plot(times, dbedelevdt_means, color = 'blue', zorder = 4) 
            plt.plot(times, dbedelevdt_medians, color = 'red', zorder = 4)
            plt.fill_between(times, dbedelevdt_2s, dbedelevdt_98s, alpha=0.50, color = 'blue', zorder = 3)
            plt.xlabel('Model year')
            plt.ylabel("d(bed elevation) dt⁻¹ (m yr⁻¹)")
            plt.grid()
            plt.legend(['Mean', 'Median', "2σ"], loc='lower left', framealpha = 1)
            fig.savefig('Output_Run_K1ldevelopcal/dbedelevdt_timeseries/dbedelevdt_timeseries.'+Export_format,  format=Export_format, dpi=dpi)
            #
            plt.close(fig)
            
        # Plot__dsoildepthdt
        if Plot__dsoildepthdt == True:
            #
            fig, ax = plt.subplots()
            drape1 = dsoildepthdt
            cmap = 'PiYG'
            label = "d(regolith depth) dt⁻¹ (m yr⁻¹)"
            vmin = -np.percentile(np.abs(drape1), mapping_percentile)
            vmax = np.percentile(np.abs(drape1), mapping_percentile)
            im = imshowhs_grid(mg, "topographic__elevation", plot_type='Drape1', drape1=drape1, cmap=cmap, alpha=alpha, color_for_background='k', color_for_closed='k', allow_colorbar=False, cbar_loc="right", cbar_or='vertical', bbox_to_anchor=(1.05, 0.0, 0.03, 1.0), cbar_width="100%", cbar_height="100%", var_name='Bedrock elevation (m)', colorbar_label_x=1.5, colorbar_label_y=0.5, cbar_label_fontweight='regular', add_label_bbox=False, vmin = vmin, vmax = vmax)
            ax.plot(mg.x_of_node[dam_nodes], mg.y_of_node[dam_nodes], 'rs')
            ticks = np.linspace(vmin, vmax, 7)            
            sm = plt.cm.ScalarMappable(cmap=cmap, norm=mcolors.Normalize(vmin=vmin, vmax=vmax))
            sm.set_array([])  # No data, just for colorbar
            cbar = fig.colorbar(sm, ax=ax, ticks=ticks)
            cbar.set_label(label, fontsize=12)
            ax.set_title('$Year$=' + str(total_time_r), fontsize=12, loc='center', pad=20)
            formatter = ScalarFormatter()
            formatter.set_powerlimits((-3, 3))  # Switch to scientific notation if the range is <10^-3 or >10^3
            ax.xaxis.set_major_formatter(formatter)      
            cbar.ax.yaxis.set_major_formatter(FuncFormatter(sci_notation_format))
            #
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/dsoildepthdt_Map/Full/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)
            #
            ax.set_xlim(Zone_1_X)
            ax.set_ylim(Zone_1_Y)   
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/dsoildepthdt_Map/Zone_1/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)  
            #
            ax.set_xlim(Zone_2_X)
            ax.set_ylim(Zone_2_Y) 
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/dsoildepthdt_Map/Zone_2/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)   
            #
            ax.set_xlim(Zone_3_X)
            ax.set_ylim(Zone_3_Y)     
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/dsoildepthdt_Map/Zone_3/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)
            #
            ax.set_xlim(Zone_4_X)
            ax.set_ylim(Zone_4_Y)     
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/dsoildepthdt_Map/Zone_4/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)
            #
            ax.set_xlim(Zone_5_X)
            ax.set_ylim(Zone_5_Y)     
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/dsoildepthdt_Map/Zone_5/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)
            #
            plt.close(fig)  
            #
            fig = plt.figure()
            plt.plot(times, dsoildepthdt_means, color = 'blue', zorder = 4) 
            plt.plot(times, dsoildepthdt_medians, color = 'red', zorder = 4)
            plt.fill_between(times, dsoildepthdt_2s, dsoildepthdt_98s, alpha=0.50, color = 'blue', zorder = 3)
            plt.xlabel('Model year')
            plt.ylabel("d(regolith depth) dt⁻¹ (m yr⁻¹)")
            plt.grid()
            plt.legend(['Mean', 'Median', "2σ"], loc='lower right', framealpha = 1)
            fig.savefig('Output_Run_K1ldevelopcal/dsoildepthdt_timeseries/dsoildepthdt_timeseries.'+Export_format,  format=Export_format, dpi=dpi)
            #
            plt.close(fig)

        # Plot__dzdt
        if Plot__dzdt == True:
            #
            fig, ax = plt.subplots()
            drape1 = dzdt
            cmap = 'seismic_r'
            label = "dz dt⁻¹ (m yr⁻¹)" 
            vmin = -np.percentile(np.abs(drape1), mapping_percentile)
            vmax = np.percentile(np.abs(drape1), mapping_percentile)
            im = imshowhs_grid(mg, "topographic__elevation", plot_type='Drape1', drape1=drape1, cmap=cmap, alpha=alpha, color_for_background='k', color_for_closed='k', allow_colorbar=False, cbar_loc="right", cbar_or='vertical', bbox_to_anchor=(1.05, 0.0, 0.03, 1.0), cbar_width="100%", cbar_height="100%", var_name='Bedrock elevation (m)', colorbar_label_x=1.5, colorbar_label_y=0.5, cbar_label_fontweight='regular', add_label_bbox=False, vmin = vmin, vmax = vmax)
            ax.plot(mg.x_of_node[dam_nodes], mg.y_of_node[dam_nodes], 'rs')
            ticks = np.linspace(vmin, vmax, 7)            
            sm = plt.cm.ScalarMappable(cmap=cmap, norm=mcolors.Normalize(vmin=vmin, vmax=vmax))
            sm.set_array([])  # No data, just for colorbar
            cbar = fig.colorbar(sm, ax=ax, ticks=ticks)
            cbar.set_label(label, fontsize=12)
            ax.set_title('$Year$=' + str(total_time_r), fontsize=12, loc='center', pad=20)
            formatter = ScalarFormatter()
            formatter.set_powerlimits((-3, 3))  # Switch to scientific notation if the range is <10^-3 or >10^3
            ax.xaxis.set_major_formatter(formatter)    
            cbar.ax.yaxis.set_major_formatter(FuncFormatter(sci_notation_format))
            #
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/dzdt_Map/Full/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)
            #
            ax.set_xlim(Zone_1_X)
            ax.set_ylim(Zone_1_Y)   
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/dzdt_Map/Zone_1/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)  
            #
            ax.set_xlim(Zone_2_X)
            ax.set_ylim(Zone_2_Y)  
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/dzdt_Map/Zone_2/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)   
            #
            ax.set_xlim(Zone_3_X)
            ax.set_ylim(Zone_3_Y)      
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/dzdt_Map/Zone_3/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)
            #
            ax.set_xlim(Zone_4_X)
            ax.set_ylim(Zone_4_Y)      
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/dzdt_Map/Zone_4/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)
            #
            ax.set_xlim(Zone_5_X)
            ax.set_ylim(Zone_5_Y)      
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/dzdt_Map/Zone_5/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)
            #
            plt.close(fig)  
            #
            fig = plt.figure()
            plt.plot(times, dzdt_means, color = 'blue', zorder = 4) 
            plt.plot(times, dzdt_medians, color = 'red', zorder = 4)
            plt.fill_between(times, dzdt_2s, dzdt_98s, alpha=0.50, color = 'blue', zorder = 3)
            plt.xlabel('Model year')
            plt.ylabel("dz dt⁻¹ (m yr⁻¹)")
            plt.grid()
            plt.legend(['Mean', 'Median', "2σ"], loc='lower right', framealpha = 1)
            fig.savefig('Output_Run_K1ldevelopcal/dzdt_timeseries/dzdt_timeseries.'+Export_format,  format=Export_format, dpi=dpi)
            #
            plt.close(fig)
            
        # Plot__erosionrate
        if Plot__erosionrate == True:
            #        
            fig, ax = plt.subplots()
            drape1 = erosionrate
            cmap = 'BrBG_r'
            label = "Erosion rate (m yr⁻¹)" 
            vmin = -np.percentile(np.abs(drape1), mapping_percentile)
            vmax = np.percentile(np.abs(drape1), mapping_percentile)
            im = imshowhs_grid(mg, "topographic__elevation", plot_type='Drape1', drape1=drape1, cmap=cmap, alpha=alpha, color_for_background='k', color_for_closed='k', allow_colorbar=False, cbar_loc="right", cbar_or='vertical', bbox_to_anchor=(1.05, 0.0, 0.03, 1.0), cbar_width="100%", cbar_height="100%", var_name='Bedrock elevation (m)', colorbar_label_x=1.5, colorbar_label_y=0.5, cbar_label_fontweight='regular', add_label_bbox=False, vmin = vmin, vmax = vmax)
            ax.plot(mg.x_of_node[dam_nodes], mg.y_of_node[dam_nodes], 'rs')
            ticks = np.linspace(vmin, vmax, 7)            
            sm = plt.cm.ScalarMappable(cmap=cmap, norm=mcolors.Normalize(vmin=vmin, vmax=vmax))
            sm.set_array([])  # No data, just for colorbar
            cbar = fig.colorbar(sm, ax=ax, ticks=ticks)
            cbar.set_label(label, fontsize=12)
            ax.set_title('$Year$=' + str(total_time_r), fontsize=12, loc='center', pad=20)
            formatter = ScalarFormatter()
            formatter.set_powerlimits((-3, 3))  # Switch to scientific notation if the range is <10^-3 or >10^3
            ax.xaxis.set_major_formatter(formatter)  
            cbar.ax.yaxis.set_major_formatter(FuncFormatter(sci_notation_format))
            #
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/erosionrate_Map/Full/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)
            #
            ax.set_xlim(Zone_1_X)
            ax.set_ylim(Zone_1_Y)   
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/erosionrate_Map/Zone_1/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)  
            #
            ax.set_xlim(Zone_2_X)
            ax.set_ylim(Zone_2_Y)   
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/erosionrate_Map/Zone_2/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)   
            #
            ax.set_xlim(Zone_3_X)
            ax.set_ylim(Zone_3_Y)        
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/erosionrate_Map/Zone_3/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)
            #
            ax.set_xlim(Zone_4_X)
            ax.set_ylim(Zone_4_Y)        
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/erosionrate_Map/Zone_4/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)
            #
            ax.set_xlim(Zone_5_X)
            ax.set_ylim(Zone_5_Y)        
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/erosionrate_Map/Zone_5/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)
            #
            plt.close(fig)  
            # 
            fig = plt.figure()
            plt.plot(times, erosionrate_means, color = 'blue', zorder = 4) 
            plt.plot(times, erosionrate_medians, color = 'red', zorder = 4)
            plt.fill_between(times, erosionrate_2s, erosionrate_98s, alpha=0.50, color = 'blue', zorder = 3)
            plt.xlabel('Model year')
            plt.ylabel("erosion rate (m yr⁻¹)")
            plt.grid()
            plt.legend(['Mean', 'Median', "2σ"], loc='upper right', framealpha = 1)
            fig.savefig('Output_Run_K1ldevelopcal/erosionrate_timeseries/erosionrate_timeseries.'+Export_format,  format=Export_format, dpi=dpi)
            #
            plt.close(fig)

        # Plot__netdz
        if Plot__netdz == True:
            #
            fig, ax = plt.subplots()
            drape1 = netdz
            cmap = 'seismic_r'
            label = "Net elevational change (m)" 
            vmin = -np.percentile(np.abs(drape1), mapping_percentile)
            vmax = np.percentile(np.abs(drape1), mapping_percentile)
            im = imshowhs_grid(mg, "topographic__elevation", plot_type='Drape1', drape1=drape1, cmap=cmap, alpha=alpha, color_for_background='k', color_for_closed='k', allow_colorbar=False, cbar_loc="right", cbar_or='vertical', bbox_to_anchor=(1.05, 0.0, 0.03, 1.0), cbar_width="100%", cbar_height="100%", var_name='Bedrock elevation (m)', colorbar_label_x=1.5, colorbar_label_y=0.5, cbar_label_fontweight='regular', add_label_bbox=False, vmin = vmin, vmax = vmax)
            ax.plot(mg.x_of_node[dam_nodes], mg.y_of_node[dam_nodes], 'rs')
            ticks = np.linspace(vmin, vmax, 7)            
            sm = plt.cm.ScalarMappable(cmap=cmap, norm=mcolors.Normalize(vmin=vmin, vmax=vmax))
            sm.set_array([])  # No data, just for colorbar
            cbar = fig.colorbar(sm, ax=ax, ticks=ticks)
            cbar.set_label(label, fontsize=12)
            ax.set_title('$Year$=' + str(total_time_r), fontsize=12, loc='center', pad=20)
            formatter = ScalarFormatter()
            formatter.set_powerlimits((-3, 3))  # Switch to scientific notation if the range is <10^-3 or >10^3
            ax.xaxis.set_major_formatter(formatter) 
            cbar.ax.yaxis.set_major_formatter(FuncFormatter(sci_notation_format))
            #
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/netdz_Map/Full/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)
            #
            ax.set_xlim(Zone_1_X)
            ax.set_ylim(Zone_1_Y)   
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/netdz_Map/Zone_1/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)  
            #
            ax.set_xlim(Zone_2_X)
            ax.set_ylim(Zone_2_Y)   
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/netdz_Map/Zone_2/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)   
            #
            ax.set_xlim(Zone_3_X)
            ax.set_ylim(Zone_3_Y)       
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/netdz_Map/Zone_3/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)
            #
            ax.set_xlim(Zone_4_X)
            ax.set_ylim(Zone_4_Y)       
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/netdz_Map/Zone_4/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)
            #
            ax.set_xlim(Zone_5_X)
            ax.set_ylim(Zone_5_Y)       
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/netdz_Map/Zone_5/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)
            #
            plt.close(fig) 
            #
            fig = plt.figure()
            plt.plot(times, netdz_means, color = 'blue', zorder = 4) 
            plt.plot(times, netdz_medians, color = 'red', zorder = 4)
            plt.fill_between(times, netdz_2s, netdz_98s, alpha=0.50, color = 'blue', zorder = 3)
            plt.xlabel('Model year')
            plt.ylabel("Net elevational change (m)")
            plt.grid()
            plt.legend(['Mean', 'Median', "2σ"], loc='lower left', framealpha = 1)
            fig.savefig('Output_Run_K1ldevelopcal/netdz_timeseries/netdz_timeseries.'+Export_format,  format=Export_format, dpi=dpi)
            #
            plt.close(fig)           
            
        # Plot__sediment__flux
        if Plot__sediment__flux == True:
            #
            fig, ax = plt.subplots()
            drape1 = np.copy(mg.at_node['sediment__flux'])
            drape1[no_data_nodes] = nan
            cmap = 'viridis'
            label = "Sediment flux (m³)" 
            vmin = 0 # np.nanpercentile(np.abs(drape1), 100 - mapping_percentile)
            vmax = np.nanpercentile(np.abs(drape1), 99)
            im = imshowhs_grid(mg, "topographic__elevation", plot_type='Drape1', drape1=drape1, cmap=cmap, alpha=alpha, color_for_background='k', color_for_closed='k', allow_colorbar=False, cbar_loc="right", cbar_or='vertical', bbox_to_anchor=(1.05, 0.0, 0.03, 1.0), cbar_width="100%", cbar_height="100%", var_name="Sediment flux (m³)", colorbar_label_x=1.5, colorbar_label_y=0.5, cbar_label_fontweight='regular', add_label_bbox=False, vmin = vmin, vmax = vmax)
            ax.plot(mg.x_of_node[dam_nodes], mg.y_of_node[dam_nodes], 'rs')
            ticks = np.linspace(vmin, vmax, 7)            
            sm = plt.cm.ScalarMappable(cmap=cmap, norm=mcolors.Normalize(vmin=vmin, vmax=vmax))
            sm.set_array([])  # No data, just for colorbar
            cbar = fig.colorbar(sm, ax=ax, ticks=ticks)
            cbar.set_label(label, fontsize=12)
            ax.set_title('$Year$=' + str(total_time_r), fontsize=12, loc='center', pad=20)
            formatter = ScalarFormatter()
            formatter.set_powerlimits((-3, 3))  # Switch to scientific notation if the range is <10^-3 or >10^3
            ax.xaxis.set_major_formatter(formatter) 
            cbar.ax.yaxis.set_major_formatter(FuncFormatter(sci_notation_format))
            #
            fig.savefig('Output_Run_K1ldevelopcal/sediment__flux_Map/Full/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)
            #
            ax.set_xlim(Zone_1_X)
            ax.set_ylim(Zone_1_Y)   
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/sediment__flux_Map/Zone_1/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)  
            #
            ax.set_xlim(Zone_2_X)
            ax.set_ylim(Zone_2_Y)
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/sediment__flux_Map/Zone_2/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)   
            #
            ax.set_xlim(Zone_3_X)
            ax.set_ylim(Zone_3_Y)    
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/sediment__flux_Map/Zone_3/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)
            #
            ax.set_xlim(Zone_4_X)
            ax.set_ylim(Zone_4_Y)    
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/sediment__flux_Map/Zone_4/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)
            #
            ax.set_xlim(Zone_5_X)
            ax.set_ylim(Zone_5_Y)    
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/sediment__flux_Map/Zone_5/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)
            #
            plt.close(fig)
            
        # Plot sediment flux timeseries
        if Plot__sediment__flux_timeseries == True:
            
            # sediment__flux_timeseries_gauge_A
            fig, ax1 = plt.subplots()
            ax1.plot(times, sediment_flux_gauge_A, 'k-', zorder = 2)
            ax1.set_xlabel('Model year')
            ax1.set_ylabel('Sediment flux at Gauge A (m³ yr⁻¹)')
            ax1.grid(linestyle='--')
            #
            y = (times * 0) + 28325.1573988047
            yl = (times * 0) + 6099.04252735909
            yh = (times * 0) + 28932.523826568
            ax1.plot(times, y, 'r--', zorder = 2)
            ax1.fill_between(times, yl, yh, alpha=0.50, color = 'red', zorder = 1)
            #
            y = (times * 0) + (Be10_Uplift * np.max(mg.at_node['drainage_area'][gauge_radius_nodes_A]))
            yl = (times * 0) + ((Be10_Uplift - Be10_Uplift_std) * np.max(mg.at_node['drainage_area'][gauge_radius_nodes_A]))
            yh = (times * 0) + ((Be10_Uplift + Be10_Uplift_std) * np.max(mg.at_node['drainage_area'][gauge_radius_nodes_A]))
            ax1.plot(times, y, 'b--', zorder = 2)
            ax1.fill_between(times, yl, yh, alpha=0.50, color = 'blue', zorder = 1)
            #
            ax2 = ax1.twinx()
            ymin, ymax = ax1.get_ylim()
            ax2.set_ylim(ymin / np.max(mg.at_node['drainage_area'][gauge_radius_nodes_A]), ymax / np.max(mg.at_node['drainage_area'][gauge_radius_nodes_A]))
            ax2.set_ylabel('Equivalent MCER (m yr⁻¹)')
            # ax1.legend(['Model data at Gauge A', 'Rating curve-implied MCER', 'Rating curve-implied MCER ± 1σ', '¹⁰Be-implied MCER', "¹⁰Be-implied ± 1σ"], loc='lower right', framealpha=1)            
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/sediment__flux_timeseries_gauge/sediment__flux_timeseries_gauge_A.' + Export_format,  format = Export_format, dpi=dpi)
            plt.close(fig) 
            
            # sediment__flux_timeseries_gauge_B
            fig, ax1 = plt.subplots()
            ax1.plot(times, sediment_flux_gauge_B, 'k-', zorder = 2)
            ax1.set_xlabel('Model year')
            ax1.set_ylabel('Sediment flux at Gauge B (m³ yr⁻¹)')
            ax1.grid(linestyle='--')
            #
            y = (times * 0) + 18636.694660535
            yl = (times * 0) + 11743.8975311791
            yh = (times * 0) + 22521.9493687378
            ax1.plot(times, y, 'r--', zorder = 2)
            ax1.fill_between(times, yl, yh, alpha=0.50, color = 'red', zorder = 1)
            #
            y = (times * 0) + (Be10_Uplift * np.max(mg.at_node['drainage_area'][gauge_radius_nodes_B]))
            yl = (times * 0) + ((Be10_Uplift - Be10_Uplift_std) * np.max(mg.at_node['drainage_area'][gauge_radius_nodes_B]))
            yh = (times * 0) + ((Be10_Uplift + Be10_Uplift_std) * np.max(mg.at_node['drainage_area'][gauge_radius_nodes_B]))
            ax1.plot(times, y, 'b--', zorder = 2)
            ax1.fill_between(times, yl, yh, alpha=0.50, color = 'blue', zorder = 1)
            #
            ax2 = ax1.twinx()
            ymin, ymax = ax1.get_ylim()
            ax2.set_ylim(ymin / np.max(mg.at_node['drainage_area'][gauge_radius_nodes_B]), ymax / np.max(mg.at_node['drainage_area'][gauge_radius_nodes_B]))
            ax2.set_ylabel('Equivalent MCER (m yr⁻¹)')
            # ax1.legend(['Model data at Gauge B', 'Rating curve-implied MCER', 'Rating curve-implied MCER ± 1σ', '¹⁰Be-implied MCER', "¹⁰Be-implied ± 1σ"], loc='lower right', framealpha=1)            
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/sediment__flux_timeseries_gauge/sediment__flux_timeseries_gauge_B.' + Export_format,  format = Export_format, dpi=dpi)
            plt.close(fig) 
            
            # sediment__flux_timeseries_gauge_C
            fig, ax1 = plt.subplots()
            ax1.plot(times, sediment_flux_gauge_C, 'k-', zorder = 2)
            ax1.set_xlabel('Model year')
            ax1.set_ylabel('Sediment flux at Gauge C (m³ yr⁻¹)')
            ax1.grid(linestyle='--')
            #
            y = (times * 0) + 4598.09808316094
            yl = (times * 0) + 3951.62460627954
            yh = (times * 0) + 5364.36836955236
            ax1.plot(times, y, 'r--', zorder = 2)
            ax1.fill_between(times, yl, yh, alpha=0.50, color = 'red', zorder = 1)
            #
            y = (times * 0) + (Be10_Uplift * np.max(mg.at_node['drainage_area'][gauge_radius_nodes_C]))
            yl = (times * 0) + ((Be10_Uplift - Be10_Uplift_std) * np.max(mg.at_node['drainage_area'][gauge_radius_nodes_C]))
            yh = (times * 0) + ((Be10_Uplift + Be10_Uplift_std) * np.max(mg.at_node['drainage_area'][gauge_radius_nodes_C]))
            ax1.plot(times, y, 'b--', zorder = 2)
            ax1.fill_between(times, yl, yh, alpha=0.50, color = 'blue', zorder = 1)
            #
            ax2 = ax1.twinx()
            ymin, ymax = ax1.get_ylim()
            ax2.set_ylim(ymin / np.max(mg.at_node['drainage_area'][gauge_radius_nodes_C]), ymax / np.max(mg.at_node['drainage_area'][gauge_radius_nodes_C]))
            ax2.set_ylabel('Equivalent MCER (m yr⁻¹)')
            # ax1.legend(['Model data at Gauge C', 'Rating curve-implied MCER', 'Rating curve-implied MCER ± 1σ', '¹⁰Be-implied MCER', "¹⁰Be-implied ± 1σ"], loc='lower right', framealpha=1)            
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/sediment__flux_timeseries_gauge/sediment__flux_timeseries_gauge_C.' + Export_format,  format = Export_format, dpi=dpi)
            plt.close(fig) 
            
            # sediment__flux_timeseries_gauge_D
            fig, ax1 = plt.subplots()
            ax1.plot(times, sediment_flux_gauge_D, 'k-', zorder = 2)
            ax1.set_xlabel('Model year')
            ax1.set_ylabel('Sediment flux at Gauge D (m³ yr⁻¹)')
            ax1.grid(linestyle='--')
            #
            y = (times * 0) + 39134.6479978908
            yl = (times * 0) + 22393.9828095615
            yh = (times * 0) + 52328.3330150515
            ax1.plot(times, y, 'r--', zorder = 2)
            ax1.fill_between(times, yl, yh, alpha=0.50, color = 'red', zorder = 1)
            #
            y = (times * 0) + (Be10_Uplift * np.max(mg.at_node['drainage_area'][gauge_radius_nodes_D]))
            yl = (times * 0) + ((Be10_Uplift - Be10_Uplift_std) * np.max(mg.at_node['drainage_area'][gauge_radius_nodes_D]))
            yh = (times * 0) + ((Be10_Uplift + Be10_Uplift_std) * np.max(mg.at_node['drainage_area'][gauge_radius_nodes_D]))
            ax1.plot(times, y, 'b--', zorder = 2)
            ax1.fill_between(times, yl, yh, alpha=0.50, color = 'blue', zorder = 1)
            #
            ax2 = ax1.twinx()
            ymin, ymax = ax1.get_ylim()
            ax2.set_ylim(ymin / np.max(mg.at_node['drainage_area'][gauge_radius_nodes_D]), ymax / np.max(mg.at_node['drainage_area'][gauge_radius_nodes_D]))
            ax2.set_ylabel('Equivalent MCER (m yr⁻¹)')
            # ax1.legend(['Model data at Gauge D', 'Rating curve-implied MCER', 'Rating curve-implied MCER ± 1σ', '¹⁰Be-implied MCER', "¹⁰Be-implied ± 1σ"], loc='lower right', framealpha=1)            
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/sediment__flux_timeseries_gauge/sediment__flux_timeseries_gauge_D.' + Export_format,  format = Export_format, dpi=dpi)
            plt.close(fig) 
            
            # sediment__flux_timeseries_gauge_E
            fig, ax1 = plt.subplots()
            ax1.plot(times, sediment_flux_gauge_E, 'k-', zorder = 2)
            ax1.set_xlabel('Model year')
            ax1.set_ylabel('Sediment flux at Gauge E (m³ yr⁻¹)')
            ax1.grid(linestyle='--')
            #
            y = (times * 0) + 223887.656003536
            yl = (times * 0) + 159208.755217335
            yh = (times * 0) + 295853.517732217
            ax1.plot(times, y, 'r--', zorder = 2)
            ax1.fill_between(times, yl, yh, alpha=0.50, color = 'red', zorder = 1)
            #
            y = (times * 0) + (Be10_Uplift * np.max(mg.at_node['drainage_area'][gauge_radius_nodes_E]))
            yl = (times * 0) + ((Be10_Uplift - Be10_Uplift_std) * np.max(mg.at_node['drainage_area'][gauge_radius_nodes_E]))
            yh = (times * 0) + ((Be10_Uplift + Be10_Uplift_std) * np.max(mg.at_node['drainage_area'][gauge_radius_nodes_E]))
            ax1.plot(times, y, 'b--', zorder = 2)
            ax1.fill_between(times, yl, yh, alpha=0.50, color = 'blue', zorder = 1)
            #
            ax2 = ax1.twinx()
            ymin, ymax = ax1.get_ylim()
            ax2.set_ylim(ymin / np.max(mg.at_node['drainage_area'][gauge_radius_nodes_E]), ymax / np.max(mg.at_node['drainage_area'][gauge_radius_nodes_E]))
            ax2.set_ylabel('Equivalent MCER (m yr⁻¹)')
            # ax1.legend(['Model data at Gauge E', 'Rating curve-implied MCER', 'Rating curve-implied MCER ± 1σ', '¹⁰Be-implied MCER', "¹⁰Be-implied ± 1σ"], loc='lower right', framealpha=1)            
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/sediment__flux_timeseries_gauge/sediment__flux_timeseries_gauge_E.' + Export_format,  format = Export_format, dpi=dpi)
            plt.close(fig) 
            
            # sediment__flux_timeseries_gauge_F
            fig, ax1 = plt.subplots()
            ax1.plot(times, sediment_flux_gauge_F, 'k-', zorder = 2)
            ax1.set_xlabel('Model year')
            ax1.set_ylabel('Sediment flux at Gauge F (m³ yr⁻¹)')
            ax1.grid(linestyle='--')
            #
            y = (times * 0) + 204578.832613164
            yl = (times * 0) + 109520.386529563
            yh = (times * 0) + 295662.265296733
            ax1.plot(times, y, 'r--', zorder = 2)
            ax1.fill_between(times, yl, yh, alpha=0.50, color = 'red', zorder = 1)
            #
            y = (times * 0) + (Be10_Uplift * np.max(mg.at_node['drainage_area'][gauge_radius_nodes_F]))
            yl = (times * 0) + ((Be10_Uplift - Be10_Uplift_std) * np.max(mg.at_node['drainage_area'][gauge_radius_nodes_F]))
            yh = (times * 0) + ((Be10_Uplift + Be10_Uplift_std) * np.max(mg.at_node['drainage_area'][gauge_radius_nodes_F]))
            ax1.plot(times, y, 'b--', zorder = 2)
            ax1.fill_between(times, yl, yh, alpha=0.50, color = 'blue', zorder = 1)
            #
            ax2 = ax1.twinx()
            ymin, ymax = ax1.get_ylim()
            ax2.set_ylim(ymin / np.max(mg.at_node['drainage_area'][gauge_radius_nodes_F]), ymax / np.max(mg.at_node['drainage_area'][gauge_radius_nodes_F]))
            ax2.set_ylabel('Equivalent MCER (m yr⁻¹)')
            # ax1.legend(['Model data at Gauge F', 'Rating curve-implied MCER', 'Rating curve-implied MCER ± 1σ', '¹⁰Be-implied MCER', "¹⁰Be-implied ± 1σ"], loc='lower right', framealpha=1)            
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/sediment__flux_timeseries_gauge/sediment__flux_timeseries_gauge_F.' + Export_format,  format = Export_format, dpi=dpi)
            plt.close(fig) 
            
            # sediment__flux_timeseries_gauge_H
            fig, ax1 = plt.subplots()
            ax1.plot(times, sediment_flux_gauge_H, 'k-', zorder = 2)
            ax1.set_xlabel('Model year')
            ax1.set_ylabel('Sediment flux at Gauge H (m³ yr⁻¹)')
            ax1.grid(linestyle='--')
            #
            y = (times * 0) + 62340.9714598844
            yl = (times * 0) + 29097.3089350222
            yh = (times * 0) + 78950.8616188175
            ax1.plot(times, y, 'r--', zorder = 2)
            ax1.fill_between(times, yl, yh, alpha=0.50, color = 'red', zorder = 1)
            #
            y = (times * 0) + (Be10_Uplift * np.max(mg.at_node['drainage_area'][gauge_radius_nodes_H]))
            yl = (times * 0) + ((Be10_Uplift - Be10_Uplift_std) * np.max(mg.at_node['drainage_area'][gauge_radius_nodes_H]))
            yh = (times * 0) + ((Be10_Uplift + Be10_Uplift_std) * np.max(mg.at_node['drainage_area'][gauge_radius_nodes_H]))
            ax1.plot(times, y, 'b--', zorder = 2)
            ax1.fill_between(times, yl, yh, alpha=0.50, color = 'blue', zorder = 1)
            #
            ax2 = ax1.twinx()
            ymin, ymax = ax1.get_ylim()
            ax2.set_ylim(ymin / np.max(mg.at_node['drainage_area'][gauge_radius_nodes_H]), ymax / np.max(mg.at_node['drainage_area'][gauge_radius_nodes_H]))
            ax2.set_ylabel('Equivalent MCER (m yr⁻¹)')
            # ax1.legend(['Model data at Gauge H', 'Rating curve-implied MCER', 'Rating curve-implied MCER ± 1σ', '¹⁰Be-implied MCER', "¹⁰Be-implied ± 1σ"], loc='lower right', framealpha=1)            
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/sediment__flux_timeseries_gauge/sediment__flux_timeseries_gauge_H.' + Export_format,  format = Export_format, dpi=dpi)
            plt.close(fig) 
            
            # sediment__flux_timeseries_gauge_G
            fig, ax1 = plt.subplots()
            ax1.plot(times, sediment_flux_gauge_G, 'k-', zorder = 2)
            ax1.set_xlabel('Model year')
            ax1.set_ylabel('Sediment flux at Gauge G (m³ yr⁻¹)')
            ax1.grid(linestyle='--')
            #
            y = (times * 0) + (Be10_Uplift * np.max(mg.at_node['drainage_area'][gauge_radius_nodes_G]))
            yl = (times * 0) + ((Be10_Uplift - Be10_Uplift_std) * np.max(mg.at_node['drainage_area'][gauge_radius_nodes_G]))
            yh = (times * 0) + ((Be10_Uplift + Be10_Uplift_std) * np.max(mg.at_node['drainage_area'][gauge_radius_nodes_G]))
            #
            ax1.plot(times, y, 'b--', zorder = 2)
            ax1.fill_between(times, yl, yh, alpha=0.50, color = 'blue', zorder = 1)
            ax2 = ax1.twinx()
            ymin, ymax = ax1.get_ylim()
            ax2.set_ylim(ymin / np.max(mg.at_node['drainage_area'][gauge_radius_nodes_G]), ymax / np.max(mg.at_node['drainage_area'][gauge_radius_nodes_G]))
            ax2.set_ylabel('Equivalent MCER (m yr⁻¹)')
            # ax1.legend(['Model data at Gauge G', '¹⁰Be-implied MCER', "¹⁰Be-implied ± 1σ"], loc='lower right', framealpha=1)            
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/sediment__flux_timeseries_gauge/sediment__flux_timeseries_gauge_G.' + Export_format,  format = Export_format, dpi=dpi)
            plt.close(fig) 
            
            # sediment__flux_timeseries_outlet
            fig, ax1 = plt.subplots()
            ax1.plot(times, sediment_flux_outlet, 'k-', zorder = 2)
            ax1.set_xlabel('Model year')
            ax1.set_ylabel('Sediment flux at outlet (m³ yr⁻¹)')
            ax1.grid(linestyle='--')
            # #
            # y = (times * 0) + 62340.9714598844
            # yl = (times * 0) + 29097.3089350222
            # yh = (times * 0) + 78950.8616188175
            # ax1.plot(times, y, 'r--', zorder = 2)
            # ax1.fill_between(times, yl, yh, alpha=0.50, color = 'red', zorder = 1)
            # #
            y = (times * 0) + (Be10_Uplift * np.max(mg.at_node['drainage_area'][outlet_radius_nodes]))
            yl = (times * 0) + ((Be10_Uplift - Be10_Uplift_std) * np.max(mg.at_node['drainage_area'][outlet_radius_nodes]))
            yh = (times * 0) + ((Be10_Uplift + Be10_Uplift_std) * np.max(mg.at_node['drainage_area'][outlet_radius_nodes]))
            ax1.plot(times, y, 'b--', zorder = 2)
            ax1.fill_between(times, yl, yh, alpha=0.50, color = 'blue', zorder = 1)
            #
            ax2 = ax1.twinx()
            ymin, ymax = ax1.get_ylim()
            ax2.set_ylim(ymin / np.max(mg.at_node['drainage_area'][outlet_radius_nodes]), ymax / np.max(mg.at_node['drainage_area'][outlet_radius_nodes]))
            ax2.set_ylabel('Equivalent MCER (m yr⁻¹)')
            # ax1.legend(['Model data at outlet', '¹⁰Be-implied MCER', "¹⁰Be-implied ± 1σ"], loc='lower right', framealpha=1)            
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/sediment__flux_timeseries_gauge/sediment__flux_timeseries_outlet.' + Export_format,  format = Export_format, dpi=dpi)
            plt.close(fig) 
        
        # Plot__segs
        if Plot__segs == True:
            
            # Get flow recievers
            receivers = mg.at_node["flow__receiver_node"]
     
            # Extract new seg_MS
            start_node = seg_MS_head
            seg_MS_nodes_ti = [start_node]
            current_node = start_node
            while True:
                next_node = receivers[current_node]
                if next_node == current_node:
                    break  
                seg_MS_nodes_ti.append(next_node)
                current_node = next_node
            seg_MS_nodes_ti = np.flip(np.array(seg_MS_nodes_ti))
            seg_MS_distance_ti = seg_MS_nodes_ti * 0
            for i in np.arange(1, len(seg_MS_nodes_ti)):
                seg_MS_distance_ti[i] = seg_MS_distance_ti[i-1] + ( ((mg.x_of_node[seg_MS_nodes_ti[i]] - mg.x_of_node[seg_MS_nodes_ti[i-1]]) ** 2) + ((mg.y_of_node[seg_MS_nodes_ti[i]] - mg.y_of_node[seg_MS_nodes_ti[i-1]]) ** 2) ) ** 0.5
            #
            # Find overlapping nodes between current and initial profiles
            seg_MS_nodes_use = []
            seg_MS_distance_use = []
            for i in np.arange(0, len(seg_MS_nodes)):
                if seg_MS_nodes[i] in seg_MS_nodes_ti:
                    seg_MS_nodes_use = np.append(seg_MS_nodes_use, seg_MS_nodes[i])
                    seg_MS_distance_use = np.append(seg_MS_distance_use, seg_MS_distance[i])
            seg_MS_nodes_use = seg_MS_nodes_use.astype(int)
            #
            # Find whether seg_MS_nodes_use are depositing or eroding
            seg_MS_nodes_use_ed = np.copy(seg_MS_nodes_use).astype(float)
            for i in np.arange(0, len(seg_MS_nodes_use)):
                if erosionrate[seg_MS_nodes_use[i]] > 0:
                    seg_MS_nodes_use_ed[i] = -1
                elif erosionrate[seg_MS_nodes_use[i]] < 0:
                    seg_MS_nodes_use_ed[i] = 1
                elif erosionrate[seg_MS_nodes_use[i]] == 1:
                    seg_MS_nodes_use_ed[i] = 0
            
            # Extract new seg_WPa
            start_node = seg_WPa_head
            seg_WPa_nodes_ti = [start_node]
            current_node = start_node
            while True:
                next_node = receivers[current_node]
                if next_node == current_node:
                    break  
                seg_WPa_nodes_ti.append(next_node)
                current_node = next_node
            seg_WPa_nodes_ti = np.flip(np.array(seg_WPa_nodes_ti))
            seg_WPa_distance_ti = seg_WPa_nodes_ti * 0
            for i in np.arange(1, len(seg_WPa_nodes_ti)):
                seg_WPa_distance_ti[i] = seg_WPa_distance_ti[i-1] + ( ((mg.x_of_node[seg_WPa_nodes_ti[i]] - mg.x_of_node[seg_WPa_nodes_ti[i-1]]) ** 2) + ((mg.y_of_node[seg_WPa_nodes_ti[i]] - mg.y_of_node[seg_WPa_nodes_ti[i-1]]) ** 2) ) ** 0.5
            #
            # Find overlapping nodes between current and initial profiles
            seg_WPa_nodes_use = []
            seg_WPa_distance_use = []
            for i in np.arange(0, len(seg_WPa_nodes)):
                if seg_WPa_nodes[i] in seg_WPa_nodes_ti:
                    seg_WPa_nodes_use = np.append(seg_WPa_nodes_use, seg_WPa_nodes[i])
                    seg_WPa_distance_use = np.append(seg_WPa_distance_use, seg_WPa_distance[i])
            seg_WPa_nodes_use = seg_WPa_nodes_use.astype(int)
            #
            # Find whether seg_WPa_nodes_use are depositing or eroding
            seg_WPa_nodes_use_ed = np.copy(seg_WPa_nodes_use).astype(float)
            for i in np.arange(0, len(seg_WPa_nodes_use)):
                if erosionrate[seg_WPa_nodes_use[i]] > 0:
                    seg_WPa_nodes_use_ed[i] = -1
                elif erosionrate[seg_WPa_nodes_use[i]] < 0:
                    seg_WPa_nodes_use_ed[i] = 1
                elif erosionrate[seg_WPa_nodes_use[i]] == 1:
                    seg_WPa_nodes_use_ed[i] = 0
                    
            # Extract new seg_WPb
            start_node = seg_WPb_head
            seg_WPb_nodes_ti = [start_node]
            current_node = start_node
            while True:
                next_node = receivers[current_node]
                if next_node == current_node:
                    break  
                seg_WPb_nodes_ti.append(next_node)
                current_node = next_node
            seg_WPb_nodes_ti = np.flip(np.array(seg_WPb_nodes_ti))
            seg_WPb_distance_ti = seg_WPb_nodes_ti * 0
            for i in np.arange(1, len(seg_WPb_nodes_ti)):
                seg_WPb_distance_ti[i] = seg_WPb_distance_ti[i-1] + ( ((mg.x_of_node[seg_WPb_nodes_ti[i]] - mg.x_of_node[seg_WPb_nodes_ti[i-1]]) ** 2) + ((mg.y_of_node[seg_WPb_nodes_ti[i]] - mg.y_of_node[seg_WPb_nodes_ti[i-1]]) ** 2) ) ** 0.5
            #
            # Find overlapping nodes between current and initial profiles
            seg_WPb_nodes_use = []
            seg_WPb_distance_use = []
            for i in np.arange(0, len(seg_WPb_nodes)):
                if seg_WPb_nodes[i] in seg_WPb_nodes_ti:
                    seg_WPb_nodes_use = np.append(seg_WPb_nodes_use, seg_WPb_nodes[i])
                    seg_WPb_distance_use = np.append(seg_WPb_distance_use, seg_WPb_distance[i])
            seg_WPb_nodes_use = seg_WPb_nodes_use.astype(int)
            #
            # Find whether seg_WPb_nodes_use are depositing or eroding
            seg_WPb_nodes_use_ed = np.copy(seg_WPb_nodes_use).astype(float)
            for i in np.arange(0, len(seg_WPb_nodes_use)):
                if erosionrate[seg_WPb_nodes_use[i]] > 0:
                    seg_WPb_nodes_use_ed[i] = -1
                elif erosionrate[seg_WPb_nodes_use[i]] < 0:
                    seg_WPb_nodes_use_ed[i] = 1
                elif erosionrate[seg_WPb_nodes_use[i]] == 1:
                    seg_WPb_nodes_use_ed[i] = 0
                    
            # Extract new seg_WPb
            start_node = seg_WPb_head
            seg_WPb_nodes_ti = [start_node]
            current_node = start_node
            while True:
                next_node = receivers[current_node]
                if next_node == current_node:
                    break  
                seg_WPb_nodes_ti.append(next_node)
                current_node = next_node
            seg_WPb_nodes_ti = np.flip(np.array(seg_WPb_nodes_ti))
            seg_WPb_distance_ti = seg_WPb_nodes_ti * 0
            for i in np.arange(1, len(seg_WPb_nodes_ti)):
                seg_WPb_distance_ti[i] = seg_WPb_distance_ti[i-1] + ( ((mg.x_of_node[seg_WPb_nodes_ti[i]] - mg.x_of_node[seg_WPb_nodes_ti[i-1]]) ** 2) + ((mg.y_of_node[seg_WPb_nodes_ti[i]] - mg.y_of_node[seg_WPb_nodes_ti[i-1]]) ** 2) ) ** 0.5
            #
            # Find overlapping nodes between current and initial profiles
            seg_WPb_nodes_use = []
            seg_WPb_distance_use = []
            for i in np.arange(0, len(seg_WPb_nodes)):
                if seg_WPb_nodes[i] in seg_WPb_nodes_ti:
                    seg_WPb_nodes_use = np.append(seg_WPb_nodes_use, seg_WPb_nodes[i])
                    seg_WPb_distance_use = np.append(seg_WPb_distance_use, seg_WPb_distance[i])
            seg_WPb_nodes_use = seg_WPb_nodes_use.astype(int)
            #
            # Find whether seg_WPb_nodes_use are depositing or eroding
            seg_WPb_nodes_use_ed = np.copy(seg_WPb_nodes_use).astype(float)
            for i in np.arange(0, len(seg_WPb_nodes_use)):
                if erosionrate[seg_WPb_nodes_use[i]] > 0:
                    seg_WPb_nodes_use_ed[i] = -1
                elif erosionrate[seg_WPb_nodes_use[i]] < 0:
                    seg_WPb_nodes_use_ed[i] = 1
                elif erosionrate[seg_WPb_nodes_use[i]] == 1:
                    seg_WPb_nodes_use_ed[i] = 0  
                    
            # Extract new seg_WPc
            start_node = seg_WPc_head
            seg_WPc_nodes_ti = [start_node]
            current_node = start_node
            while True:
                next_node = receivers[current_node]
                if next_node == current_node:
                    break  
                seg_WPc_nodes_ti.append(next_node)
                current_node = next_node
            seg_WPc_nodes_ti = np.flip(np.array(seg_WPc_nodes_ti))
            seg_WPc_distance_ti = seg_WPc_nodes_ti * 0
            for i in np.arange(1, len(seg_WPc_nodes_ti)):
                seg_WPc_distance_ti[i] = seg_WPc_distance_ti[i-1] + ( ((mg.x_of_node[seg_WPc_nodes_ti[i]] - mg.x_of_node[seg_WPc_nodes_ti[i-1]]) ** 2) + ((mg.y_of_node[seg_WPc_nodes_ti[i]] - mg.y_of_node[seg_WPc_nodes_ti[i-1]]) ** 2) ) ** 0.5
            #
            # Find overlapping nodes between current and initial profiles
            seg_WPc_nodes_use = []
            seg_WPc_distance_use = []
            for i in np.arange(0, len(seg_WPc_nodes)):
                if seg_WPc_nodes[i] in seg_WPc_nodes_ti:
                    seg_WPc_nodes_use = np.append(seg_WPc_nodes_use, seg_WPc_nodes[i])
                    seg_WPc_distance_use = np.append(seg_WPc_distance_use, seg_WPc_distance[i])
            seg_WPc_nodes_use = seg_WPc_nodes_use.astype(int)
            #
            # Find whether seg_WPc_nodes_use are depositing or eroding
            seg_WPc_nodes_use_ed = np.copy(seg_WPc_nodes_use).astype(float)
            for i in np.arange(0, len(seg_WPc_nodes_use)):
                if erosionrate[seg_WPc_nodes_use[i]] > 0:
                    seg_WPc_nodes_use_ed[i] = -1
                elif erosionrate[seg_WPc_nodes_use[i]] < 0:
                    seg_WPc_nodes_use_ed[i] = 1
                elif erosionrate[seg_WPc_nodes_use[i]] == 1:
                    seg_WPc_nodes_use_ed[i] = 0
                    
            # Extract new seg_WPd
            start_node = seg_WPd_head
            seg_WPd_nodes_ti = [start_node]
            current_node = start_node
            while True:
                next_node = receivers[current_node]
                if next_node == current_node:
                    break  
                seg_WPd_nodes_ti.append(next_node)
                current_node = next_node
            seg_WPd_nodes_ti = np.flip(np.array(seg_WPd_nodes_ti))
            seg_WPd_distance_ti = seg_WPd_nodes_ti * 0
            for i in np.arange(1, len(seg_WPd_nodes_ti)):
                seg_WPd_distance_ti[i] = seg_WPd_distance_ti[i-1] + ( ((mg.x_of_node[seg_WPd_nodes_ti[i]] - mg.x_of_node[seg_WPd_nodes_ti[i-1]]) ** 2) + ((mg.y_of_node[seg_WPd_nodes_ti[i]] - mg.y_of_node[seg_WPd_nodes_ti[i-1]]) ** 2) ) ** 0.5
            #
            # Find overlapping nodes between current and initial profiles
            seg_WPd_nodes_use = []
            seg_WPd_distance_use = []
            for i in np.arange(0, len(seg_WPd_nodes)):
                if seg_WPd_nodes[i] in seg_WPd_nodes_ti:
                    seg_WPd_nodes_use = np.append(seg_WPd_nodes_use, seg_WPd_nodes[i])
                    seg_WPd_distance_use = np.append(seg_WPd_distance_use, seg_WPd_distance[i])
            seg_WPd_nodes_use = seg_WPd_nodes_use.astype(int)
            #
            # Find whether seg_WPd_nodes_use are depositing or eroding
            seg_WPd_nodes_use_ed = np.copy(seg_WPd_nodes_use).astype(float)
            for i in np.arange(0, len(seg_WPd_nodes_use)):
                if erosionrate[seg_WPd_nodes_use[i]] > 0:
                    seg_WPd_nodes_use_ed[i] = -1
                elif erosionrate[seg_WPd_nodes_use[i]] < 0:
                    seg_WPd_nodes_use_ed[i] = 1
                elif erosionrate[seg_WPd_nodes_use[i]] == 1:
                    seg_WPd_nodes_use_ed[i] = 0
                    
            # Extract new seg_HDa
            start_node = seg_HDa_head
            seg_HDa_nodes_ti = [start_node]
            current_node = start_node
            while True:
                next_node = receivers[current_node]
                if next_node == current_node:
                    break  
                seg_HDa_nodes_ti.append(next_node)
                current_node = next_node
            seg_HDa_nodes_ti = np.flip(np.array(seg_HDa_nodes_ti))
            seg_HDa_distance_ti = seg_HDa_nodes_ti * 0
            for i in np.arange(1, len(seg_HDa_nodes_ti)):
                seg_HDa_distance_ti[i] = seg_HDa_distance_ti[i-1] + ( ((mg.x_of_node[seg_HDa_nodes_ti[i]] - mg.x_of_node[seg_HDa_nodes_ti[i-1]]) ** 2) + ((mg.y_of_node[seg_HDa_nodes_ti[i]] - mg.y_of_node[seg_HDa_nodes_ti[i-1]]) ** 2) ) ** 0.5
            #
            # Find overlapping nodes between current and initial profiles
            seg_HDa_nodes_use = []
            seg_HDa_distance_use = []
            for i in np.arange(0, len(seg_HDa_nodes)):
                if seg_HDa_nodes[i] in seg_HDa_nodes_ti:
                    seg_HDa_nodes_use = np.append(seg_HDa_nodes_use, seg_HDa_nodes[i])
                    seg_HDa_distance_use = np.append(seg_HDa_distance_use, seg_HDa_distance[i])
            seg_HDa_nodes_use = seg_HDa_nodes_use.astype(int)
            #
            # Find whether seg_HDa_nodes_use are depositing or eroding
            seg_HDa_nodes_use_ed = np.copy(seg_HDa_nodes_use).astype(float)
            for i in np.arange(0, len(seg_HDa_nodes_use)):
                if erosionrate[seg_HDa_nodes_use[i]] > 0:
                    seg_HDa_nodes_use_ed[i] = -1
                elif erosionrate[seg_HDa_nodes_use[i]] < 0:
                    seg_HDa_nodes_use_ed[i] = 1
                elif erosionrate[seg_HDa_nodes_use[i]] == 1:
                    seg_HDa_nodes_use_ed[i] = 0
                    
            # Extract new seg_HDb
            start_node = seg_HDb_head
            seg_HDb_nodes_ti = [start_node]
            current_node = start_node
            while True:
                next_node = receivers[current_node]
                if next_node == current_node:
                    break  
                seg_HDb_nodes_ti.append(next_node)
                current_node = next_node
            seg_HDb_nodes_ti = np.flip(np.array(seg_HDb_nodes_ti))
            seg_HDb_distance_ti = seg_HDb_nodes_ti * 0
            for i in np.arange(1, len(seg_HDb_nodes_ti)):
                seg_HDb_distance_ti[i] = seg_HDb_distance_ti[i-1] + ( ((mg.x_of_node[seg_HDb_nodes_ti[i]] - mg.x_of_node[seg_HDb_nodes_ti[i-1]]) ** 2) + ((mg.y_of_node[seg_HDb_nodes_ti[i]] - mg.y_of_node[seg_HDb_nodes_ti[i-1]]) ** 2) ) ** 0.5
            #
            # Find overlapping nodes between current and initial profiles
            seg_HDb_nodes_use = []
            seg_HDb_distance_use = []
            for i in np.arange(0, len(seg_HDb_nodes)):
                if seg_HDb_nodes[i] in seg_HDb_nodes_ti:
                    seg_HDb_nodes_use = np.append(seg_HDb_nodes_use, seg_HDb_nodes[i])
                    seg_HDb_distance_use = np.append(seg_HDb_distance_use, seg_HDb_distance[i])
            seg_HDb_nodes_use = seg_HDb_nodes_use.astype(int)
            #
            # Find whether seg_HDb_nodes_use are depositing or eroding
            seg_HDb_nodes_use_ed = np.copy(seg_HDb_nodes_use).astype(float)
            for i in np.arange(0, len(seg_HDb_nodes_use)):
                if erosionrate[seg_HDb_nodes_use[i]] > 0:
                    seg_HDb_nodes_use_ed[i] = -1
                elif erosionrate[seg_HDb_nodes_use[i]] < 0:
                    seg_HDb_nodes_use_ed[i] = 1
                elif erosionrate[seg_HDb_nodes_use[i]] == 1:
                    seg_HDb_nodes_use_ed[i] = 0
                    
            # Extract new seg_GRa
            start_node = seg_GRa_head
            seg_GRa_nodes_ti = [start_node]
            current_node = start_node
            while True:
                next_node = receivers[current_node]
                if next_node == current_node:
                    break  
                seg_GRa_nodes_ti.append(next_node)
                current_node = next_node
            seg_GRa_nodes_ti = np.flip(np.array(seg_GRa_nodes_ti))
            seg_GRa_distance_ti = seg_GRa_nodes_ti * 0
            for i in np.arange(1, len(seg_GRa_nodes_ti)):
                seg_GRa_distance_ti[i] = seg_GRa_distance_ti[i-1] + ( ((mg.x_of_node[seg_GRa_nodes_ti[i]] - mg.x_of_node[seg_GRa_nodes_ti[i-1]]) ** 2) + ((mg.y_of_node[seg_GRa_nodes_ti[i]] - mg.y_of_node[seg_GRa_nodes_ti[i-1]]) ** 2) ) ** 0.5
            #
            # Find overlapping nodes between current and initial profiles
            seg_GRa_nodes_use = []
            seg_GRa_distance_use = []
            for i in np.arange(0, len(seg_GRa_nodes)):
                if seg_GRa_nodes[i] in seg_GRa_nodes_ti:
                    seg_GRa_nodes_use = np.append(seg_GRa_nodes_use, seg_GRa_nodes[i])
                    seg_GRa_distance_use = np.append(seg_GRa_distance_use, seg_GRa_distance[i])
            seg_GRa_nodes_use = seg_GRa_nodes_use.astype(int)
            #
            # Find whether seg_GRa_nodes_use are depositing or eroding
            seg_GRa_nodes_use_ed = np.copy(seg_GRa_nodes_use).astype(float)
            for i in np.arange(0, len(seg_GRa_nodes_use)):
                if erosionrate[seg_GRa_nodes_use[i]] > 0:
                    seg_GRa_nodes_use_ed[i] = -1
                elif erosionrate[seg_GRa_nodes_use[i]] < 0:
                    seg_GRa_nodes_use_ed[i] = 1
                elif erosionrate[seg_GRa_nodes_use[i]] == 1:
                    seg_GRa_nodes_use_ed[i] = 0
                    
            # Extract new seg_OVa
            start_node = seg_OVa_head
            seg_OVa_nodes_ti = [start_node]
            current_node = start_node
            while True:
                next_node = receivers[current_node]
                if next_node == current_node:
                    break  
                seg_OVa_nodes_ti.append(next_node)
                current_node = next_node
            seg_OVa_nodes_ti = np.flip(np.array(seg_OVa_nodes_ti))
            seg_OVa_distance_ti = seg_OVa_nodes_ti * 0
            for i in np.arange(1, len(seg_OVa_nodes_ti)):
                seg_OVa_distance_ti[i] = seg_OVa_distance_ti[i-1] + ( ((mg.x_of_node[seg_OVa_nodes_ti[i]] - mg.x_of_node[seg_OVa_nodes_ti[i-1]]) ** 2) + ((mg.y_of_node[seg_OVa_nodes_ti[i]] - mg.y_of_node[seg_OVa_nodes_ti[i-1]]) ** 2) ) ** 0.5
            #
            # Find overlapping nodes between current and initial profiles
            seg_OVa_nodes_use = []
            seg_OVa_distance_use = []
            for i in np.arange(0, len(seg_OVa_nodes)):
                if seg_OVa_nodes[i] in seg_OVa_nodes_ti:
                    seg_OVa_nodes_use = np.append(seg_OVa_nodes_use, seg_OVa_nodes[i])
                    seg_OVa_distance_use = np.append(seg_OVa_distance_use, seg_OVa_distance[i])
            seg_OVa_nodes_use = seg_OVa_nodes_use.astype(int)
            #
            # Find whether seg_OVa_nodes_use are depositing or eroding
            seg_OVa_nodes_use_ed = np.copy(seg_OVa_nodes_use).astype(float)
            for i in np.arange(0, len(seg_OVa_nodes_use)):
                if erosionrate[seg_OVa_nodes_use[i]] > 0:
                    seg_OVa_nodes_use_ed[i] = -1
                elif erosionrate[seg_OVa_nodes_use[i]] < 0:
                    seg_OVa_nodes_use_ed[i] = 1
                elif erosionrate[seg_OVa_nodes_use[i]] == 1:
                    seg_OVa_nodes_use_ed[i] = 0
                    
            # Extract new seg_WGa
            start_node = seg_WGa_head
            seg_WGa_nodes_ti = [start_node]
            current_node = start_node
            while True:
                next_node = receivers[current_node]
                if next_node == current_node:
                    break  
                seg_WGa_nodes_ti.append(next_node)
                current_node = next_node
            seg_WGa_nodes_ti = np.flip(np.array(seg_WGa_nodes_ti))
            seg_WGa_distance_ti = seg_WGa_nodes_ti * 0
            for i in np.arange(1, len(seg_WGa_nodes_ti)):
                seg_WGa_distance_ti[i] = seg_WGa_distance_ti[i-1] + ( ((mg.x_of_node[seg_WGa_nodes_ti[i]] - mg.x_of_node[seg_WGa_nodes_ti[i-1]]) ** 2) + ((mg.y_of_node[seg_WGa_nodes_ti[i]] - mg.y_of_node[seg_WGa_nodes_ti[i-1]]) ** 2) ) ** 0.5
            #
            # Find overlapping nodes between current and initial profiles
            seg_WGa_nodes_use = []
            seg_WGa_distance_use = []
            for i in np.arange(0, len(seg_WGa_nodes)):
                if seg_WGa_nodes[i] in seg_WGa_nodes_ti:
                    seg_WGa_nodes_use = np.append(seg_WGa_nodes_use, seg_WGa_nodes[i])
                    seg_WGa_distance_use = np.append(seg_WGa_distance_use, seg_WGa_distance[i])
            seg_WGa_nodes_use = seg_WGa_nodes_use.astype(int)
            #
            # Find whether seg_WGa_nodes_use are depositing or eroding
            seg_WGa_nodes_use_ed = np.copy(seg_WGa_nodes_use).astype(float)
            for i in np.arange(0, len(seg_WGa_nodes_use)):
                if erosionrate[seg_WGa_nodes_use[i]] > 0:
                    seg_WGa_nodes_use_ed[i] = -1
                elif erosionrate[seg_WGa_nodes_use[i]] < 0:
                    seg_WGa_nodes_use_ed[i] = 1
                elif erosionrate[seg_WGa_nodes_use[i]] == 1:
                    seg_WGa_nodes_use_ed[i] = 0
                    
            # Extract new seg_WGb
            start_node = seg_WGb_head
            seg_WGb_nodes_ti = [start_node]
            current_node = start_node
            while True:
                next_node = receivers[current_node]
                if next_node == current_node:
                    break  
                seg_WGb_nodes_ti.append(next_node)
                current_node = next_node
            seg_WGb_nodes_ti = np.flip(np.array(seg_WGb_nodes_ti))
            seg_WGb_distance_ti = seg_WGb_nodes_ti * 0
            for i in np.arange(1, len(seg_WGb_nodes_ti)):
                seg_WGb_distance_ti[i] = seg_WGb_distance_ti[i-1] + ( ((mg.x_of_node[seg_WGb_nodes_ti[i]] - mg.x_of_node[seg_WGb_nodes_ti[i-1]]) ** 2) + ((mg.y_of_node[seg_WGb_nodes_ti[i]] - mg.y_of_node[seg_WGb_nodes_ti[i-1]]) ** 2) ) ** 0.5
            #
            # Find overlapping nodes between current and initial profiles
            seg_WGb_nodes_use = []
            seg_WGb_distance_use = []
            for i in np.arange(0, len(seg_WGb_nodes)):
                if seg_WGb_nodes[i] in seg_WGb_nodes_ti:
                    seg_WGb_nodes_use = np.append(seg_WGb_nodes_use, seg_WGb_nodes[i])
                    seg_WGb_distance_use = np.append(seg_WGb_distance_use, seg_WGb_distance[i])
            seg_WGb_nodes_use = seg_WGb_nodes_use.astype(int)
            #
            # Find whether seg_WGb_nodes_use are depositing or eroding
            seg_WGb_nodes_use_ed = np.copy(seg_WGb_nodes_use).astype(float)
            for i in np.arange(0, len(seg_WGb_nodes_use)):
                if erosionrate[seg_WGb_nodes_use[i]] > 0:
                    seg_WGb_nodes_use_ed[i] = -1
                elif erosionrate[seg_WGb_nodes_use[i]] < 0:
                    seg_WGb_nodes_use_ed[i] = 1
                elif erosionrate[seg_WGb_nodes_use[i]] == 1:
                    seg_WGb_nodes_use_ed[i] = 0
                    
            # Extract new seg_WGc
            start_node = seg_WGc_head
            seg_WGc_nodes_ti = [start_node]
            current_node = start_node
            while True:
                next_node = receivers[current_node]
                if next_node == current_node:
                    break  
                seg_WGc_nodes_ti.append(next_node)
                current_node = next_node
            seg_WGc_nodes_ti = np.flip(np.array(seg_WGc_nodes_ti))
            seg_WGc_distance_ti = seg_WGc_nodes_ti * 0
            for i in np.arange(1, len(seg_WGc_nodes_ti)):
                seg_WGc_distance_ti[i] = seg_WGc_distance_ti[i-1] + ( ((mg.x_of_node[seg_WGc_nodes_ti[i]] - mg.x_of_node[seg_WGc_nodes_ti[i-1]]) ** 2) + ((mg.y_of_node[seg_WGc_nodes_ti[i]] - mg.y_of_node[seg_WGc_nodes_ti[i-1]]) ** 2) ) ** 0.5
            #
            # Find overlapping nodes between current and initial profiles
            seg_WGc_nodes_use = []
            seg_WGc_distance_use = []
            for i in np.arange(0, len(seg_WGc_nodes)):
                if seg_WGc_nodes[i] in seg_WGc_nodes_ti:
                    seg_WGc_nodes_use = np.append(seg_WGc_nodes_use, seg_WGc_nodes[i])
                    seg_WGc_distance_use = np.append(seg_WGc_distance_use, seg_WGc_distance[i])
            seg_WGc_nodes_use = seg_WGc_nodes_use.astype(int)
            #
            # Find whether seg_WGc_nodes_use are depositing or eroding
            seg_WGc_nodes_use_ed = np.copy(seg_WGc_nodes_use).astype(float)
            for i in np.arange(0, len(seg_WGc_nodes_use)):
                if erosionrate[seg_WGc_nodes_use[i]] > 0:
                    seg_WGc_nodes_use_ed[i] = -1
                elif erosionrate[seg_WGc_nodes_use[i]] < 0:
                    seg_WGc_nodes_use_ed[i] = 1
                elif erosionrate[seg_WGc_nodes_use[i]] == 1:
                    seg_WGc_nodes_use_ed[i] = 0
                    
            # Extract new seg_WGd
            start_node = seg_WGd_head
            seg_WGd_nodes_ti = [start_node]
            current_node = start_node
            while True:
                next_node = receivers[current_node]
                if next_node == current_node:
                    break  
                seg_WGd_nodes_ti.append(next_node)
                current_node = next_node
            seg_WGd_nodes_ti = np.flip(np.array(seg_WGd_nodes_ti))
            seg_WGd_distance_ti = seg_WGd_nodes_ti * 0
            for i in np.arange(1, len(seg_WGd_nodes_ti)):
                seg_WGd_distance_ti[i] = seg_WGd_distance_ti[i-1] + ( ((mg.x_of_node[seg_WGd_nodes_ti[i]] - mg.x_of_node[seg_WGd_nodes_ti[i-1]]) ** 2) + ((mg.y_of_node[seg_WGd_nodes_ti[i]] - mg.y_of_node[seg_WGd_nodes_ti[i-1]]) ** 2) ) ** 0.5
            #
            # Find overlapping nodes between current and initial profiles
            seg_WGd_nodes_use = []
            seg_WGd_distance_use = []
            for i in np.arange(0, len(seg_WGd_nodes)):
                if seg_WGd_nodes[i] in seg_WGd_nodes_ti:
                    seg_WGd_nodes_use = np.append(seg_WGd_nodes_use, seg_WGd_nodes[i])
                    seg_WGd_distance_use = np.append(seg_WGd_distance_use, seg_WGd_distance[i])
            seg_WGd_nodes_use = seg_WGd_nodes_use.astype(int)
            #
            # Find whether seg_WGd_nodes_use are depositing or eroding
            seg_WGd_nodes_use_ed = np.copy(seg_WGd_nodes_use).astype(float)
            for i in np.arange(0, len(seg_WGd_nodes_use)):
                if erosionrate[seg_WGd_nodes_use[i]] > 0:
                    seg_WGd_nodes_use_ed[i] = -1
                elif erosionrate[seg_WGd_nodes_use[i]] < 0:
                    seg_WGd_nodes_use_ed[i] = 1
                elif erosionrate[seg_WGd_nodes_use[i]] == 1:
                    seg_WGd_nodes_use_ed[i] = 0
                    
            # Extract new seg_WGe
            start_node = seg_WGe_head
            seg_WGe_nodes_ti = [start_node]
            current_node = start_node
            while True:
                next_node = receivers[current_node]
                if next_node == current_node:
                    break  
                seg_WGe_nodes_ti.append(next_node)
                current_node = next_node
            seg_WGe_nodes_ti = np.flip(np.array(seg_WGe_nodes_ti))
            seg_WGe_distance_ti = seg_WGe_nodes_ti * 0
            for i in np.arange(1, len(seg_WGe_nodes_ti)):
                seg_WGe_distance_ti[i] = seg_WGe_distance_ti[i-1] + ( ((mg.x_of_node[seg_WGe_nodes_ti[i]] - mg.x_of_node[seg_WGe_nodes_ti[i-1]]) ** 2) + ((mg.y_of_node[seg_WGe_nodes_ti[i]] - mg.y_of_node[seg_WGe_nodes_ti[i-1]]) ** 2) ) ** 0.5
            #
            # Find overlapping nodes between current and initial profiles
            seg_WGe_nodes_use = []
            seg_WGe_distance_use = []
            for i in np.arange(0, len(seg_WGe_nodes)):
                if seg_WGe_nodes[i] in seg_WGe_nodes_ti:
                    seg_WGe_nodes_use = np.append(seg_WGe_nodes_use, seg_WGe_nodes[i])
                    seg_WGe_distance_use = np.append(seg_WGe_distance_use, seg_WGe_distance[i])
            seg_WGe_nodes_use = seg_WGe_nodes_use.astype(int)
            #
            # Find whether seg_WGe_nodes_use are depositing or eroding
            seg_WGe_nodes_use_ed = np.copy(seg_WGe_nodes_use).astype(float)
            for i in np.arange(0, len(seg_WGe_nodes_use)):
                if erosionrate[seg_WGe_nodes_use[i]] > 0:
                    seg_WGe_nodes_use_ed[i] = -1
                elif erosionrate[seg_WGe_nodes_use[i]] < 0:
                    seg_WGe_nodes_use_ed[i] = 1
                elif erosionrate[seg_WGe_nodes_use[i]] == 1:
                    seg_WGe_nodes_use_ed[i] = 0
                    
            # Extract new seg_WGf
            start_node = seg_WGf_head
            seg_WGf_nodes_ti = [start_node]
            current_node = start_node
            while True:
                next_node = receivers[current_node]
                if next_node == current_node:
                    break  
                seg_WGf_nodes_ti.append(next_node)
                current_node = next_node
            seg_WGf_nodes_ti = np.flip(np.array(seg_WGf_nodes_ti))
            seg_WGf_distance_ti = seg_WGf_nodes_ti * 0
            for i in np.arange(1, len(seg_WGf_nodes_ti)):
                seg_WGf_distance_ti[i] = seg_WGf_distance_ti[i-1] + ( ((mg.x_of_node[seg_WGf_nodes_ti[i]] - mg.x_of_node[seg_WGf_nodes_ti[i-1]]) ** 2) + ((mg.y_of_node[seg_WGf_nodes_ti[i]] - mg.y_of_node[seg_WGf_nodes_ti[i-1]]) ** 2) ) ** 0.5
            #
            # Find overlapping nodes between current and initial profiles
            seg_WGf_nodes_use = []
            seg_WGf_distance_use = []
            for i in np.arange(0, len(seg_WGf_nodes)):
                if seg_WGf_nodes[i] in seg_WGf_nodes_ti:
                    seg_WGf_nodes_use = np.append(seg_WGf_nodes_use, seg_WGf_nodes[i])
                    seg_WGf_distance_use = np.append(seg_WGf_distance_use, seg_WGf_distance[i])
            seg_WGf_nodes_use = seg_WGf_nodes_use.astype(int)
            #
            # Find whether seg_WGf_nodes_use are depositing or eroding
            seg_WGf_nodes_use_ed = np.copy(seg_WGf_nodes_use).astype(float)
            for i in np.arange(0, len(seg_WGf_nodes_use)):
                if erosionrate[seg_WGf_nodes_use[i]] > 0:
                    seg_WGf_nodes_use_ed[i] = -1
                elif erosionrate[seg_WGf_nodes_use[i]] < 0:
                    seg_WGf_nodes_use_ed[i] = 1
                elif erosionrate[seg_WGf_nodes_use[i]] == 1:
                    seg_WGf_nodes_use_ed[i] = 0
                    
            # Extract new seg_SMa
            start_node = seg_SMa_head
            seg_SMa_nodes_ti = [start_node]
            current_node = start_node
            while True:
                next_node = receivers[current_node]
                if next_node == current_node:
                    break  
                seg_SMa_nodes_ti.append(next_node)
                current_node = next_node
            seg_SMa_nodes_ti = np.flip(np.array(seg_SMa_nodes_ti))
            seg_SMa_distance_ti = seg_SMa_nodes_ti * 0
            for i in np.arange(1, len(seg_SMa_nodes_ti)):
                seg_SMa_distance_ti[i] = seg_SMa_distance_ti[i-1] + ( ((mg.x_of_node[seg_SMa_nodes_ti[i]] - mg.x_of_node[seg_SMa_nodes_ti[i-1]]) ** 2) + ((mg.y_of_node[seg_SMa_nodes_ti[i]] - mg.y_of_node[seg_SMa_nodes_ti[i-1]]) ** 2) ) ** 0.5
            #
            # Find overlapping nodes between current and initial profiles
            seg_SMa_nodes_use = []
            seg_SMa_distance_use = []
            for i in np.arange(0, len(seg_SMa_nodes)):
                if seg_SMa_nodes[i] in seg_SMa_nodes_ti:
                    seg_SMa_nodes_use = np.append(seg_SMa_nodes_use, seg_SMa_nodes[i])
                    seg_SMa_distance_use = np.append(seg_SMa_distance_use, seg_SMa_distance[i])
            seg_SMa_nodes_use = seg_SMa_nodes_use.astype(int)
            #
            # Find whether seg_SMa_nodes_use are depositing or eroding
            seg_SMa_nodes_use_ed = np.copy(seg_SMa_nodes_use).astype(float)
            for i in np.arange(0, len(seg_SMa_nodes_use)):
                if erosionrate[seg_SMa_nodes_use[i]] > 0:
                    seg_SMa_nodes_use_ed[i] = -1
                elif erosionrate[seg_SMa_nodes_use[i]] < 0:
                    seg_SMa_nodes_use_ed[i] = 1
                elif erosionrate[seg_SMa_nodes_use[i]] == 1:
                    seg_SMa_nodes_use_ed[i] = 0
                    
            # Extract new seg_SMb
            start_node = seg_SMb_head
            seg_SMb_nodes_ti = [start_node]
            current_node = start_node
            while True:
                next_node = receivers[current_node]
                if next_node == current_node:
                    break  
                seg_SMb_nodes_ti.append(next_node)
                current_node = next_node
            seg_SMb_nodes_ti = np.flip(np.array(seg_SMb_nodes_ti))
            seg_SMb_distance_ti = seg_SMb_nodes_ti * 0
            for i in np.arange(1, len(seg_SMb_nodes_ti)):
                seg_SMb_distance_ti[i] = seg_SMb_distance_ti[i-1] + ( ((mg.x_of_node[seg_SMb_nodes_ti[i]] - mg.x_of_node[seg_SMb_nodes_ti[i-1]]) ** 2) + ((mg.y_of_node[seg_SMb_nodes_ti[i]] - mg.y_of_node[seg_SMb_nodes_ti[i-1]]) ** 2) ) ** 0.5
            #
            # Find overlapping nodes between current and initial profiles
            seg_SMb_nodes_use = []
            seg_SMb_distance_use = []
            for i in np.arange(0, len(seg_SMb_nodes)):
                if seg_SMb_nodes[i] in seg_SMb_nodes_ti:
                    seg_SMb_nodes_use = np.append(seg_SMb_nodes_use, seg_SMb_nodes[i])
                    seg_SMb_distance_use = np.append(seg_SMb_distance_use, seg_SMb_distance[i])
            seg_SMb_nodes_use = seg_SMb_nodes_use.astype(int)
            #
            # Find whether seg_SMb_nodes_use are depositing or eroding
            seg_SMb_nodes_use_ed = np.copy(seg_SMb_nodes_use).astype(float)
            for i in np.arange(0, len(seg_SMb_nodes_use)):
                if erosionrate[seg_SMb_nodes_use[i]] > 0:
                    seg_SMb_nodes_use_ed[i] = -1
                elif erosionrate[seg_SMb_nodes_use[i]] < 0:
                    seg_SMb_nodes_use_ed[i] = 1
                elif erosionrate[seg_SMb_nodes_use[i]] == 1:
                    seg_SMb_nodes_use_ed[i] = 0
                    
            # Extract new seg_SMc
            start_node = seg_SMc_head
            seg_SMc_nodes_ti = [start_node]
            current_node = start_node
            while True:
                next_node = receivers[current_node]
                if next_node == current_node:
                    break  
                seg_SMc_nodes_ti.append(next_node)
                current_node = next_node
            seg_SMc_nodes_ti = np.flip(np.array(seg_SMc_nodes_ti))
            seg_SMc_distance_ti = seg_SMc_nodes_ti * 0
            for i in np.arange(1, len(seg_SMc_nodes_ti)):
                seg_SMc_distance_ti[i] = seg_SMc_distance_ti[i-1] + ( ((mg.x_of_node[seg_SMc_nodes_ti[i]] - mg.x_of_node[seg_SMc_nodes_ti[i-1]]) ** 2) + ((mg.y_of_node[seg_SMc_nodes_ti[i]] - mg.y_of_node[seg_SMc_nodes_ti[i-1]]) ** 2) ) ** 0.5
            #
            # Find overlapping nodes between current and initial profiles
            seg_SMc_nodes_use = []
            seg_SMc_distance_use = []
            for i in np.arange(0, len(seg_SMc_nodes)):
                if seg_SMc_nodes[i] in seg_SMc_nodes_ti:
                    seg_SMc_nodes_use = np.append(seg_SMc_nodes_use, seg_SMc_nodes[i])
                    seg_SMc_distance_use = np.append(seg_SMc_distance_use, seg_SMc_distance[i])
            seg_SMc_nodes_use = seg_SMc_nodes_use.astype(int)
            #
            # Find whether seg_SMc_nodes_use are depositing or eroding
            seg_SMc_nodes_use_ed = np.copy(seg_SMc_nodes_use).astype(float)
            for i in np.arange(0, len(seg_SMc_nodes_use)):
                if erosionrate[seg_SMc_nodes_use[i]] > 0:
                    seg_SMc_nodes_use_ed[i] = -1
                elif erosionrate[seg_SMc_nodes_use[i]] < 0:
                    seg_SMc_nodes_use_ed[i] = 1
                elif erosionrate[seg_SMc_nodes_use[i]] == 1:
                    seg_SMc_nodes_use_ed[i] = 0
                    
            # Extract new seg_SMd
            start_node = seg_SMd_head
            seg_SMd_nodes_ti = [start_node]
            current_node = start_node
            while True:
                next_node = receivers[current_node]
                if next_node == current_node:
                    break  
                seg_SMd_nodes_ti.append(next_node)
                current_node = next_node
            seg_SMd_nodes_ti = np.flip(np.array(seg_SMd_nodes_ti))
            seg_SMd_distance_ti = seg_SMd_nodes_ti * 0
            for i in np.arange(1, len(seg_SMd_nodes_ti)):
                seg_SMd_distance_ti[i] = seg_SMd_distance_ti[i-1] + ( ((mg.x_of_node[seg_SMd_nodes_ti[i]] - mg.x_of_node[seg_SMd_nodes_ti[i-1]]) ** 2) + ((mg.y_of_node[seg_SMd_nodes_ti[i]] - mg.y_of_node[seg_SMd_nodes_ti[i-1]]) ** 2) ) ** 0.5
            #
            # Find overlapping nodes between current and initial profiles
            seg_SMd_nodes_use = []
            seg_SMd_distance_use = []
            for i in np.arange(0, len(seg_SMd_nodes)):
                if seg_SMd_nodes[i] in seg_SMd_nodes_ti:
                    seg_SMd_nodes_use = np.append(seg_SMd_nodes_use, seg_SMd_nodes[i])
                    seg_SMd_distance_use = np.append(seg_SMd_distance_use, seg_SMd_distance[i])
            seg_SMd_nodes_use = seg_SMd_nodes_use.astype(int)
            #
            # Find whether seg_SMd_nodes_use are depositing or eroding
            seg_SMd_nodes_use_ed = np.copy(seg_SMd_nodes_use).astype(float)
            for i in np.arange(0, len(seg_SMd_nodes_use)):
                if erosionrate[seg_SMd_nodes_use[i]] > 0:
                    seg_SMd_nodes_use_ed[i] = -1
                elif erosionrate[seg_SMd_nodes_use[i]] < 0:
                    seg_SMd_nodes_use_ed[i] = 1
                elif erosionrate[seg_SMd_nodes_use[i]] == 1:
                    seg_SMd_nodes_use_ed[i] = 0
                       
            # Plot seg_MS
            fig = plt.figure()   
            plt.plot(seg_MS_distance_use / 1000, mg.at_node['topographic__elevation'][seg_MS_nodes_use], '.', linewidth = 0.5, color = 'orange')
            plt.plot(seg_MS_distance / 1000, zr0[seg_MS_nodes], '--', linewidth = 0.5, color = 'orange')
            plt.plot(seg_MS_distance_use / 1000, mg.at_node['bedrock__elevation'][seg_MS_nodes_use], 'k.', linewidth = 0.5)        
            plt.plot(seg_MS_distance / 1000, br0[seg_MS_nodes], 'k--', linewidth = 0.5)
            for i in np.arange(0, len(seg_MS_nodes_use_ed)):
                if seg_MS_nodes_use_ed[i] == 1:
                    plt.plot(seg_MS_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_MS_nodes_use[i]], '.', linewidth = 0.5, color = 'green')
                elif seg_MS_nodes_use_ed[i] == -1:
                    plt.plot(seg_MS_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_MS_nodes_use[i]], '.', linewidth = 0.5, color = 'red')
                if dbedelevdt[seg_MS_nodes_use[i]] < 0:
                    plt.plot(seg_MS_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_MS_nodes_use[i]], '.', linewidth = 0.5, color = 'purple')        
            plt.xlim(xlim_MS)
            plt.ylim(ylim_MS)
            plt.grid()
            plt.xlabel('Distance (km)')
            plt.ylabel('Elevation (m)')
            plt.title('$Year$='+str(total_time_r))
            plt.legend(['Current topographic elevation', 'Initial topographic elevation', 'Current bedrock elevation', 'Initial bedrock elevation'], loc = 'upper left', fontsize=6)
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/Segs/Individual/MS/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)
            plt.close(fig)                
                
            # Plot seg_WPa
            fig = plt.figure()   
            plt.plot(seg_WPa_distance_use / 1000, mg.at_node['topographic__elevation'][seg_WPa_nodes_use], '.', linewidth = 0.5, color = 'orange')
            plt.plot(seg_WPa_distance / 1000, zr0[seg_WPa_nodes], '--', linewidth = 0.5, color = 'orange')
            plt.plot(seg_WPa_distance_use / 1000, mg.at_node['bedrock__elevation'][seg_WPa_nodes_use], 'k.', linewidth = 0.5)        
            plt.plot(seg_WPa_distance / 1000, br0[seg_WPa_nodes], 'k--', linewidth = 0.5)
            for i in np.arange(0, len(seg_WPa_nodes_use_ed)):
                if seg_WPa_nodes_use_ed[i] == 1:
                    plt.plot(seg_WPa_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WPa_nodes_use[i]], '.', linewidth = 0.5, color = 'green')
                elif seg_WPa_nodes_use_ed[i] == -1:
                    plt.plot(seg_WPa_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WPa_nodes_use[i]], '.', linewidth = 0.5, color = 'red')
                if dbedelevdt[seg_WPa_nodes_use[i]] < 0:
                    plt.plot(seg_WPa_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WPa_nodes_use[i]], '.', linewidth = 0.5, color = 'purple')        
            plt.xlim(xlim_WPa)
            plt.ylim(ylim_WPa)
            plt.grid()
            plt.xlabel('Distance (km)')
            plt.ylabel('Elevation (m)')
            plt.title('$Year$='+str(total_time_r))
            plt.legend(['Current topographic elevation', 'Initial topographic elevation', 'Current bedrock elevation', 'Initial bedrock elevation'], loc = 'upper left', fontsize=6)
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/Segs/Individual/WPa/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)
            plt.close(fig)    
            
            # Plot seg_WPb
            fig = plt.figure()   
            plt.plot(seg_WPb_distance_use / 1000, mg.at_node['topographic__elevation'][seg_WPb_nodes_use], '.', linewidth = 0.5, color = 'orange')
            plt.plot(seg_WPb_distance / 1000, zr0[seg_WPb_nodes], '--', linewidth = 0.5, color = 'orange')
            plt.plot(seg_WPb_distance_use / 1000, mg.at_node['bedrock__elevation'][seg_WPb_nodes_use], 'k.', linewidth = 0.5)        
            plt.plot(seg_WPb_distance / 1000, br0[seg_WPb_nodes], 'k--', linewidth = 0.5)
            for i in np.arange(0, len(seg_WPb_nodes_use_ed)):
                if seg_WPb_nodes_use_ed[i] == 1:
                    plt.plot(seg_WPb_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WPb_nodes_use[i]], '.', linewidth = 0.5, color = 'green')
                elif seg_WPb_nodes_use_ed[i] == -1:
                    plt.plot(seg_WPb_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WPb_nodes_use[i]], '.', linewidth = 0.5, color = 'red')
                if dbedelevdt[seg_WPb_nodes_use[i]] < 0:
                    plt.plot(seg_WPb_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WPb_nodes_use[i]], '.', linewidth = 0.5, color = 'purple')        
            plt.xlim(xlim_WPb)
            plt.ylim(ylim_WPb)
            plt.grid()
            plt.xlabel('Distance (km)')
            plt.ylabel('Elevation (m)')
            plt.title('$Year$='+str(total_time_r))
            plt.legend(['Current topographic elevation', 'Initial topographic elevation', 'Current bedrock elevation', 'Initial bedrock elevation'], loc = 'upper left', fontsize=6)
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/Segs/Individual/WPb/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)
            plt.close(fig)              
            
            # Plot seg_WPb
            fig = plt.figure()   
            plt.plot(seg_WPb_distance_use / 1000, mg.at_node['topographic__elevation'][seg_WPb_nodes_use], '.', linewidth = 0.5, color = 'orange')
            plt.plot(seg_WPb_distance / 1000, zr0[seg_WPb_nodes], '--', linewidth = 0.5, color = 'orange')
            plt.plot(seg_WPb_distance_use / 1000, mg.at_node['bedrock__elevation'][seg_WPb_nodes_use], 'k.', linewidth = 0.5)        
            plt.plot(seg_WPb_distance / 1000, br0[seg_WPb_nodes], 'k--', linewidth = 0.5)
            for i in np.arange(0, len(seg_WPb_nodes_use_ed)):
                if seg_WPb_nodes_use_ed[i] == 1:
                    plt.plot(seg_WPb_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WPb_nodes_use[i]], '.', linewidth = 0.5, color = 'green')
                elif seg_WPb_nodes_use_ed[i] == -1:
                    plt.plot(seg_WPb_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WPb_nodes_use[i]], '.', linewidth = 0.5, color = 'red')
                if dbedelevdt[seg_WPb_nodes_use[i]] < 0:
                    plt.plot(seg_WPb_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WPb_nodes_use[i]], '.', linewidth = 0.5, color = 'purple')        
            plt.xlim(xlim_WPb)
            plt.ylim(ylim_WPb)
            plt.grid()
            plt.xlabel('Distance (km)')
            plt.ylabel('Elevation (m)')
            plt.title('$Year$='+str(total_time_r))
            plt.legend(['Current topographic elevation', 'Initial topographic elevation', 'Current bedrock elevation', 'Initial bedrock elevation'], loc = 'upper left', fontsize=6)
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/Segs/Individual/WPb/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)
            plt.close(fig)              
            
            # Plot seg_WPc
            fig = plt.figure()   
            plt.plot(seg_WPc_distance_use / 1000, mg.at_node['topographic__elevation'][seg_WPc_nodes_use], '.', linewidth = 0.5, color = 'orange')
            plt.plot(seg_WPc_distance / 1000, zr0[seg_WPc_nodes], '--', linewidth = 0.5, color = 'orange')
            plt.plot(seg_WPc_distance_use / 1000, mg.at_node['bedrock__elevation'][seg_WPc_nodes_use], 'k.', linewidth = 0.5)        
            plt.plot(seg_WPc_distance / 1000, br0[seg_WPc_nodes], 'k--', linewidth = 0.5)
            for i in np.arange(0, len(seg_WPc_nodes_use_ed)):
                if seg_WPc_nodes_use_ed[i] == 1:
                    plt.plot(seg_WPc_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WPc_nodes_use[i]], '.', linewidth = 0.5, color = 'green')
                elif seg_WPc_nodes_use_ed[i] == -1:
                    plt.plot(seg_WPc_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WPc_nodes_use[i]], '.', linewidth = 0.5, color = 'red')
                if dbedelevdt[seg_WPc_nodes_use[i]] < 0:
                    plt.plot(seg_WPc_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WPc_nodes_use[i]], '.', linewidth = 0.5, color = 'purple')        
            plt.xlim(xlim_WPc)
            plt.ylim(ylim_WPc)
            plt.grid()
            plt.xlabel('Distance (km)')
            plt.ylabel('Elevation (m)')
            plt.title('$Year$='+str(total_time_r))
            plt.legend(['Current topographic elevation', 'Initial topographic elevation', 'Current bedrock elevation', 'Initial bedrock elevation'], loc = 'upper left', fontsize=6)
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/Segs/Individual/WPc/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)
            plt.close(fig)            

            # Plot seg_WPd
            fig = plt.figure()   
            plt.plot(seg_WPd_distance_use / 1000, mg.at_node['topographic__elevation'][seg_WPd_nodes_use], '.', linewidth = 0.5, color = 'orange')
            plt.plot(seg_WPd_distance / 1000, zr0[seg_WPd_nodes], '--', linewidth = 0.5, color = 'orange')
            plt.plot(seg_WPd_distance_use / 1000, mg.at_node['bedrock__elevation'][seg_WPd_nodes_use], 'k.', linewidth = 0.5)        
            plt.plot(seg_WPd_distance / 1000, br0[seg_WPd_nodes], 'k--', linewidth = 0.5)
            for i in np.arange(0, len(seg_WPd_nodes_use_ed)):
                if seg_WPd_nodes_use_ed[i] == 1:
                    plt.plot(seg_WPd_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WPd_nodes_use[i]], '.', linewidth = 0.5, color = 'green')
                elif seg_WPd_nodes_use_ed[i] == -1:
                    plt.plot(seg_WPd_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WPd_nodes_use[i]], '.', linewidth = 0.5, color = 'red')
                if dbedelevdt[seg_WPd_nodes_use[i]] < 0:
                    plt.plot(seg_WPd_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WPd_nodes_use[i]], '.', linewidth = 0.5, color = 'purple')        
            plt.xlim(xlim_WPd)
            plt.ylim(ylim_WPd)
            plt.grid()
            plt.xlabel('Distance (km)')
            plt.ylabel('Elevation (m)')
            plt.title('$Year$='+str(total_time_r))
            plt.legend(['Current topographic elevation', 'Initial topographic elevation', 'Current bedrock elevation', 'Initial bedrock elevation'], loc = 'upper left', fontsize=6)
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/Segs/Individual/WPd/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)
            plt.close(fig) 
            
            # Plot seg_HDa
            fig = plt.figure()   
            plt.plot(seg_HDa_distance_use / 1000, mg.at_node['topographic__elevation'][seg_HDa_nodes_use], '.', linewidth = 0.5, color = 'orange')
            plt.plot(seg_HDa_distance / 1000, zr0[seg_HDa_nodes], '--', linewidth = 0.5, color = 'orange')
            plt.plot(seg_HDa_distance_use / 1000, mg.at_node['bedrock__elevation'][seg_HDa_nodes_use], 'k.', linewidth = 0.5)        
            plt.plot(seg_HDa_distance / 1000, br0[seg_HDa_nodes], 'k--', linewidth = 0.5)
            for i in np.arange(0, len(seg_HDa_nodes_use_ed)):
                if seg_HDa_nodes_use_ed[i] == 1:
                    plt.plot(seg_HDa_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_HDa_nodes_use[i]], '.', linewidth = 0.5, color = 'green')
                elif seg_HDa_nodes_use_ed[i] == -1:
                    plt.plot(seg_HDa_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_HDa_nodes_use[i]], '.', linewidth = 0.5, color = 'red')
                if dbedelevdt[seg_HDa_nodes_use[i]] < 0:
                    plt.plot(seg_HDa_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_HDa_nodes_use[i]], '.', linewidth = 0.5, color = 'purple')        
            plt.xlim(xlim_HDa)
            plt.ylim(ylim_HDa)
            plt.grid()
            plt.xlabel('Distance (km)')
            plt.ylabel('Elevation (m)')
            plt.title('$Year$='+str(total_time_r))
            plt.legend(['Current topographic elevation', 'Initial topographic elevation', 'Current bedrock elevation', 'Initial bedrock elevation'], loc = 'upper left', fontsize=6)
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/Segs/Individual/HDa/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)
            plt.close(fig)        
            
            # Plot seg_HDb
            fig = plt.figure()   
            plt.plot(seg_HDb_distance_use / 1000, mg.at_node['topographic__elevation'][seg_HDb_nodes_use], '.', linewidth = 0.5, color = 'orange')
            plt.plot(seg_HDb_distance / 1000, zr0[seg_HDb_nodes], '--', linewidth = 0.5, color = 'orange')
            plt.plot(seg_HDb_distance_use / 1000, mg.at_node['bedrock__elevation'][seg_HDb_nodes_use], 'k.', linewidth = 0.5)        
            plt.plot(seg_HDb_distance / 1000, br0[seg_HDb_nodes], 'k--', linewidth = 0.5)
            for i in np.arange(0, len(seg_HDb_nodes_use_ed)):
                if seg_HDb_nodes_use_ed[i] == 1:
                    plt.plot(seg_HDb_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_HDb_nodes_use[i]], '.', linewidth = 0.5, color = 'green')
                elif seg_HDb_nodes_use_ed[i] == -1:
                    plt.plot(seg_HDb_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_HDb_nodes_use[i]], '.', linewidth = 0.5, color = 'red')
                if dbedelevdt[seg_HDb_nodes_use[i]] < 0:
                    plt.plot(seg_HDb_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_HDb_nodes_use[i]], '.', linewidth = 0.5, color = 'purple')        
            plt.xlim(xlim_HDb)
            plt.ylim(ylim_HDb)
            plt.grid()
            plt.xlabel('Distance (km)')
            plt.ylabel('Elevation (m)')
            plt.title('$Year$='+str(total_time_r))
            plt.legend(['Current topographic elevation', 'Initial topographic elevation', 'Current bedrock elevation', 'Initial bedrock elevation'], loc = 'upper left', fontsize=6)
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/Segs/Individual/HDb/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)
            plt.close(fig)       
            
            # Plot seg_GRa
            fig = plt.figure()   
            plt.plot(seg_GRa_distance_use / 1000, mg.at_node['topographic__elevation'][seg_GRa_nodes_use], '.', linewidth = 0.5, color = 'orange')
            plt.plot(seg_GRa_distance / 1000, zr0[seg_GRa_nodes], '--', linewidth = 0.5, color = 'orange')
            plt.plot(seg_GRa_distance_use / 1000, mg.at_node['bedrock__elevation'][seg_GRa_nodes_use], 'k.', linewidth = 0.5)        
            plt.plot(seg_GRa_distance / 1000, br0[seg_GRa_nodes], 'k--', linewidth = 0.5)
            for i in np.arange(0, len(seg_GRa_nodes_use_ed)):
                if seg_GRa_nodes_use_ed[i] == 1:
                    plt.plot(seg_GRa_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_GRa_nodes_use[i]], '.', linewidth = 0.5, color = 'green')
                elif seg_GRa_nodes_use_ed[i] == -1:
                    plt.plot(seg_GRa_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_GRa_nodes_use[i]], '.', linewidth = 0.5, color = 'red')
                if dbedelevdt[seg_GRa_nodes_use[i]] < 0:
                    plt.plot(seg_GRa_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_GRa_nodes_use[i]], '.', linewidth = 0.5, color = 'purple')        
            plt.xlim(xlim_GRa)
            plt.ylim(ylim_GRa)
            plt.grid()
            plt.xlabel('Distance (km)')
            plt.ylabel('Elevation (m)')
            plt.title('$Year$='+str(total_time_r))
            plt.legend(['Current topographic elevation', 'Initial topographic elevation', 'Current bedrock elevation', 'Initial bedrock elevation'], loc = 'upper left', fontsize=6)
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/Segs/Individual/GRa/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)
            plt.close(fig)  
            
            # Plot seg_OVa
            fig = plt.figure()   
            plt.plot(seg_OVa_distance_use / 1000, mg.at_node['topographic__elevation'][seg_OVa_nodes_use], '.', linewidth = 0.5, color = 'orange')
            plt.plot(seg_OVa_distance / 1000, zr0[seg_OVa_nodes], '--', linewidth = 0.5, color = 'orange')
            plt.plot(seg_OVa_distance_use / 1000, mg.at_node['bedrock__elevation'][seg_OVa_nodes_use], 'k.', linewidth = 0.5)        
            plt.plot(seg_OVa_distance / 1000, br0[seg_OVa_nodes], 'k--', linewidth = 0.5)
            for i in np.arange(0, len(seg_OVa_nodes_use_ed)):
                if seg_OVa_nodes_use_ed[i] == 1:
                    plt.plot(seg_OVa_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_OVa_nodes_use[i]], '.', linewidth = 0.5, color = 'green')
                elif seg_OVa_nodes_use_ed[i] == -1:
                    plt.plot(seg_OVa_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_OVa_nodes_use[i]], '.', linewidth = 0.5, color = 'red')
                if dbedelevdt[seg_OVa_nodes_use[i]] < 0:
                    plt.plot(seg_OVa_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_OVa_nodes_use[i]], '.', linewidth = 0.5, color = 'purple')        
            plt.xlim(xlim_OVa)
            plt.ylim(ylim_OVa)
            plt.grid()
            plt.xlabel('Distance (km)')
            plt.ylabel('Elevation (m)')
            plt.title('$Year$='+str(total_time_r))
            plt.legend(['Current topographic elevation', 'Initial topographic elevation', 'Current bedrock elevation', 'Initial bedrock elevation'], loc = 'upper left', fontsize=6)
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/Segs/Individual/OVa/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)
            plt.close(fig) 
            
            # Plot seg_WGa
            fig = plt.figure()   
            plt.plot(seg_WGa_distance_use / 1000, mg.at_node['topographic__elevation'][seg_WGa_nodes_use], '.', linewidth = 0.5, color = 'orange')
            plt.plot(seg_WGa_distance / 1000, zr0[seg_WGa_nodes], '--', linewidth = 0.5, color = 'orange')
            plt.plot(seg_WGa_distance_use / 1000, mg.at_node['bedrock__elevation'][seg_WGa_nodes_use], 'k.', linewidth = 0.5)        
            plt.plot(seg_WGa_distance / 1000, br0[seg_WGa_nodes], 'k--', linewidth = 0.5)
            for i in np.arange(0, len(seg_WGa_nodes_use_ed)):
                if seg_WGa_nodes_use_ed[i] == 1:
                    plt.plot(seg_WGa_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WGa_nodes_use[i]], '.', linewidth = 0.5, color = 'green')
                elif seg_WGa_nodes_use_ed[i] == -1:
                    plt.plot(seg_WGa_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WGa_nodes_use[i]], '.', linewidth = 0.5, color = 'red')
                if dbedelevdt[seg_WGa_nodes_use[i]] < 0:
                    plt.plot(seg_WGa_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WGa_nodes_use[i]], '.', linewidth = 0.5, color = 'purple')        
            plt.xlim(xlim_WGa)
            plt.ylim(ylim_WGa)
            plt.grid()
            plt.xlabel('Distance (km)')
            plt.ylabel('Elevation (m)')
            plt.title('$Year$='+str(total_time_r))
            plt.legend(['Current topographic elevation', 'Initial topographic elevation', 'Current bedrock elevation', 'Initial bedrock elevation'], loc = 'upper left', fontsize=6)
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/Segs/Individual/WGa/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)
            plt.close(fig)    
            
            # Plot seg_WGb
            fig = plt.figure()   
            plt.plot(seg_WGb_distance_use / 1000, mg.at_node['topographic__elevation'][seg_WGb_nodes_use], '.', linewidth = 0.5, color = 'orange')
            plt.plot(seg_WGb_distance / 1000, zr0[seg_WGb_nodes], '--', linewidth = 0.5, color = 'orange')
            plt.plot(seg_WGb_distance_use / 1000, mg.at_node['bedrock__elevation'][seg_WGb_nodes_use], 'k.', linewidth = 0.5)        
            plt.plot(seg_WGb_distance / 1000, br0[seg_WGb_nodes], 'k--', linewidth = 0.5)
            for i in np.arange(0, len(seg_WGb_nodes_use_ed)):
                if seg_WGb_nodes_use_ed[i] == 1:
                    plt.plot(seg_WGb_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WGb_nodes_use[i]], '.', linewidth = 0.5, color = 'green')
                elif seg_WGb_nodes_use_ed[i] == -1:
                    plt.plot(seg_WGb_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WGb_nodes_use[i]], '.', linewidth = 0.5, color = 'red')
                if dbedelevdt[seg_WGb_nodes_use[i]] < 0:
                    plt.plot(seg_WGb_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WGb_nodes_use[i]], '.', linewidth = 0.5, color = 'purple')        
            plt.xlim(xlim_WGb)
            plt.ylim(ylim_WGb)
            plt.grid()
            plt.xlabel('Distance (km)')
            plt.ylabel('Elevation (m)')
            plt.title('$Year$='+str(total_time_r))
            plt.legend(['Current topographic elevation', 'Initial topographic elevation', 'Current bedrock elevation', 'Initial bedrock elevation'], loc = 'upper left', fontsize=6)
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/Segs/Individual/WGb/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)
            plt.close(fig) 
            
            # Plot seg_WGc
            fig = plt.figure()   
            plt.plot(seg_WGc_distance_use / 1000, mg.at_node['topographic__elevation'][seg_WGc_nodes_use], '.', linewidth = 0.5, color = 'orange')
            plt.plot(seg_WGc_distance / 1000, zr0[seg_WGc_nodes], '--', linewidth = 0.5, color = 'orange')
            plt.plot(seg_WGc_distance_use / 1000, mg.at_node['bedrock__elevation'][seg_WGc_nodes_use], 'k.', linewidth = 0.5)        
            plt.plot(seg_WGc_distance / 1000, br0[seg_WGc_nodes], 'k--', linewidth = 0.5)
            for i in np.arange(0, len(seg_WGc_nodes_use_ed)):
                if seg_WGc_nodes_use_ed[i] == 1:
                    plt.plot(seg_WGc_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WGc_nodes_use[i]], '.', linewidth = 0.5, color = 'green')
                elif seg_WGc_nodes_use_ed[i] == -1:
                    plt.plot(seg_WGc_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WGc_nodes_use[i]], '.', linewidth = 0.5, color = 'red')
                if dbedelevdt[seg_WGc_nodes_use[i]] < 0:
                    plt.plot(seg_WGc_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WGc_nodes_use[i]], '.', linewidth = 0.5, color = 'purple')        
            plt.xlim(xlim_WGc)
            plt.ylim(ylim_WGc)
            plt.grid()
            plt.xlabel('Distance (km)')
            plt.ylabel('Elevation (m)')
            plt.title('$Year$='+str(total_time_r))
            plt.legend(['Current topographic elevation', 'Initial topographic elevation', 'Current bedrock elevation', 'Initial bedrock elevation'], loc = 'upper left', fontsize=6)
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/Segs/Individual/WGc/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)
            plt.close(fig)   
            
            # Plot seg_WGd
            fig = plt.figure()   
            plt.plot(seg_WGd_distance_use / 1000, mg.at_node['topographic__elevation'][seg_WGd_nodes_use], '.', linewidth = 0.5, color = 'orange')
            plt.plot(seg_WGd_distance / 1000, zr0[seg_WGd_nodes], '--', linewidth = 0.5, color = 'orange')
            plt.plot(seg_WGd_distance_use / 1000, mg.at_node['bedrock__elevation'][seg_WGd_nodes_use], 'k.', linewidth = 0.5)        
            plt.plot(seg_WGd_distance / 1000, br0[seg_WGd_nodes], 'k--', linewidth = 0.5)
            for i in np.arange(0, len(seg_WGd_nodes_use_ed)):
                if seg_WGd_nodes_use_ed[i] == 1:
                    plt.plot(seg_WGd_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WGd_nodes_use[i]], '.', linewidth = 0.5, color = 'green')
                elif seg_WGd_nodes_use_ed[i] == -1:
                    plt.plot(seg_WGd_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WGd_nodes_use[i]], '.', linewidth = 0.5, color = 'red')
                if dbedelevdt[seg_WGd_nodes_use[i]] < 0:
                    plt.plot(seg_WGd_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WGd_nodes_use[i]], '.', linewidth = 0.5, color = 'purple')        
            plt.xlim(xlim_WGd)
            plt.ylim(ylim_WGd)
            plt.grid()
            plt.xlabel('Distance (km)')
            plt.ylabel('Elevation (m)')
            plt.title('$Year$='+str(total_time_r))
            plt.legend(['Current topographic elevation', 'Initial topographic elevation', 'Current bedrock elevation', 'Initial bedrock elevation'], loc = 'upper left', fontsize=6)
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/Segs/Individual/WGd/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)
            plt.close(fig)     
            
            # Plot seg_WGe
            fig = plt.figure()   
            plt.plot(seg_WGe_distance_use / 1000, mg.at_node['topographic__elevation'][seg_WGe_nodes_use], '.', linewidth = 0.5, color = 'orange')
            plt.plot(seg_WGe_distance / 1000, zr0[seg_WGe_nodes], '--', linewidth = 0.5, color = 'orange')
            plt.plot(seg_WGe_distance_use / 1000, mg.at_node['bedrock__elevation'][seg_WGe_nodes_use], 'k.', linewidth = 0.5)        
            plt.plot(seg_WGe_distance / 1000, br0[seg_WGe_nodes], 'k--', linewidth = 0.5)
            for i in np.arange(0, len(seg_WGe_nodes_use_ed)):
                if seg_WGe_nodes_use_ed[i] == 1:
                    plt.plot(seg_WGe_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WGe_nodes_use[i]], '.', linewidth = 0.5, color = 'green')
                elif seg_WGe_nodes_use_ed[i] == -1:
                    plt.plot(seg_WGe_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WGe_nodes_use[i]], '.', linewidth = 0.5, color = 'red')
                if dbedelevdt[seg_WGe_nodes_use[i]] < 0:
                    plt.plot(seg_WGe_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WGe_nodes_use[i]], '.', linewidth = 0.5, color = 'purple')        
            plt.xlim(xlim_WGe)
            plt.ylim(ylim_WGe)
            plt.grid()
            plt.xlabel('Distance (km)')
            plt.ylabel('Elevation (m)')
            plt.title('$Year$='+str(total_time_r))
            plt.legend(['Current topographic elevation', 'Initial topographic elevation', 'Current bedrock elevation', 'Initial bedrock elevation'], loc = 'upper left', fontsize=6)
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/Segs/Individual/WGe/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)
            plt.close(fig) 
            
            # Plot seg_WGf
            fig = plt.figure()   
            plt.plot(seg_WGf_distance_use / 1000, mg.at_node['topographic__elevation'][seg_WGf_nodes_use], '.', linewidth = 0.5, color = 'orange')
            plt.plot(seg_WGf_distance / 1000, zr0[seg_WGf_nodes], '--', linewidth = 0.5, color = 'orange')
            plt.plot(seg_WGf_distance_use / 1000, mg.at_node['bedrock__elevation'][seg_WGf_nodes_use], 'k.', linewidth = 0.5)        
            plt.plot(seg_WGf_distance / 1000, br0[seg_WGf_nodes], 'k--', linewidth = 0.5)
            for i in np.arange(0, len(seg_WGf_nodes_use_ed)):
                if seg_WGf_nodes_use_ed[i] == 1:
                    plt.plot(seg_WGf_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WGf_nodes_use[i]], '.', linewidth = 0.5, color = 'green')
                elif seg_WGf_nodes_use_ed[i] == -1:
                    plt.plot(seg_WGf_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WGf_nodes_use[i]], '.', linewidth = 0.5, color = 'red')
                if dbedelevdt[seg_WGf_nodes_use[i]] < 0:
                    plt.plot(seg_WGf_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WGf_nodes_use[i]], '.', linewidth = 0.5, color = 'purple')        
            plt.xlim(xlim_WGf)
            plt.ylim(ylim_WGf)
            plt.grid()
            plt.xlabel('Distance (km)')
            plt.ylabel('Elevation (m)')
            plt.title('$Year$='+str(total_time_r))
            plt.legend(['Current topographic elevation', 'Initial topographic elevation', 'Current bedrock elevation', 'Initial bedrock elevation'], loc = 'upper left', fontsize=6)
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/Segs/Individual/WGf/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)
            plt.close(fig)     
            
            # Plot seg_SMa
            fig = plt.figure()   
            plt.plot(seg_SMa_distance_use / 1000, mg.at_node['topographic__elevation'][seg_SMa_nodes_use], '.', linewidth = 0.5, color = 'orange')
            plt.plot(seg_SMa_distance / 1000, zr0[seg_SMa_nodes], '--', linewidth = 0.5, color = 'orange')
            plt.plot(seg_SMa_distance_use / 1000, mg.at_node['bedrock__elevation'][seg_SMa_nodes_use], 'k.', linewidth = 0.5)        
            plt.plot(seg_SMa_distance / 1000, br0[seg_SMa_nodes], 'k--', linewidth = 0.5)
            for i in np.arange(0, len(seg_SMa_nodes_use_ed)):
                if seg_SMa_nodes_use_ed[i] == 1:
                    plt.plot(seg_SMa_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_SMa_nodes_use[i]], '.', linewidth = 0.5, color = 'green')
                elif seg_SMa_nodes_use_ed[i] == -1:
                    plt.plot(seg_SMa_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_SMa_nodes_use[i]], '.', linewidth = 0.5, color = 'red')
                if dbedelevdt[seg_SMa_nodes_use[i]] < 0:
                    plt.plot(seg_SMa_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_SMa_nodes_use[i]], '.', linewidth = 0.5, color = 'purple')        
            plt.xlim(xlim_SMa)
            plt.ylim(ylim_SMa)
            plt.grid()
            plt.xlabel('Distance (km)')
            plt.ylabel('Elevation (m)')
            plt.title('$Year$='+str(total_time_r))
            plt.legend(['Current topographic elevation', 'Initial topographic elevation', 'Current bedrock elevation', 'Initial bedrock elevation'], loc = 'upper left', fontsize=6)
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/Segs/Individual/SMa/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)
            plt.close(fig)  
            
            # Plot seg_SMb
            fig = plt.figure()   
            plt.plot(seg_SMb_distance_use / 1000, mg.at_node['topographic__elevation'][seg_SMb_nodes_use], '.', linewidth = 0.5, color = 'orange')
            plt.plot(seg_SMb_distance / 1000, zr0[seg_SMb_nodes], '--', linewidth = 0.5, color = 'orange')
            plt.plot(seg_SMb_distance_use / 1000, mg.at_node['bedrock__elevation'][seg_SMb_nodes_use], 'k.', linewidth = 0.5)        
            plt.plot(seg_SMb_distance / 1000, br0[seg_SMb_nodes], 'k--', linewidth = 0.5)
            for i in np.arange(0, len(seg_SMb_nodes_use_ed)):
                if seg_SMb_nodes_use_ed[i] == 1:
                    plt.plot(seg_SMb_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_SMb_nodes_use[i]], '.', linewidth = 0.5, color = 'green')
                elif seg_SMb_nodes_use_ed[i] == -1:
                    plt.plot(seg_SMb_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_SMb_nodes_use[i]], '.', linewidth = 0.5, color = 'red')
                if dbedelevdt[seg_SMb_nodes_use[i]] < 0:
                    plt.plot(seg_SMb_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_SMb_nodes_use[i]], '.', linewidth = 0.5, color = 'purple')        
            plt.xlim(xlim_SMb)
            plt.ylim(ylim_SMb)
            plt.grid()
            plt.xlabel('Distance (km)')
            plt.ylabel('Elevation (m)')
            plt.title('$Year$='+str(total_time_r))
            plt.legend(['Current topographic elevation', 'Initial topographic elevation', 'Current bedrock elevation', 'Initial bedrock elevation'], loc = 'upper left', fontsize=6)
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/Segs/Individual/SMb/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)
            plt.close(fig)  
    
            # Plot seg_SMc
            fig = plt.figure()   
            plt.plot(seg_SMc_distance_use / 1000, mg.at_node['topographic__elevation'][seg_SMc_nodes_use], '.', linewidth = 0.5, color = 'orange')
            plt.plot(seg_SMc_distance / 1000, zr0[seg_SMc_nodes], '--', linewidth = 0.5, color = 'orange')
            plt.plot(seg_SMc_distance_use / 1000, mg.at_node['bedrock__elevation'][seg_SMc_nodes_use], 'k.', linewidth = 0.5)        
            plt.plot(seg_SMc_distance / 1000, br0[seg_SMc_nodes], 'k--', linewidth = 0.5)
            for i in np.arange(0, len(seg_SMc_nodes_use_ed)):
                if seg_SMc_nodes_use_ed[i] == 1:
                    plt.plot(seg_SMc_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_SMc_nodes_use[i]], '.', linewidth = 0.5, color = 'green')
                elif seg_SMc_nodes_use_ed[i] == -1:
                    plt.plot(seg_SMc_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_SMc_nodes_use[i]], '.', linewidth = 0.5, color = 'red')
                if dbedelevdt[seg_SMc_nodes_use[i]] < 0:
                    plt.plot(seg_SMc_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_SMc_nodes_use[i]], '.', linewidth = 0.5, color = 'purple')        
            plt.xlim(xlim_SMc)
            plt.ylim(ylim_SMc)
            plt.grid()
            plt.xlabel('Distance (km)')
            plt.ylabel('Elevation (m)')
            plt.title('$Year$='+str(total_time_r))
            plt.legend(['Current topographic elevation', 'Initial topographic elevation', 'Current bedrock elevation', 'Initial bedrock elevation'], loc = 'upper left', fontsize=6)
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/Segs/Individual/SMc/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)
            plt.close(fig)    
            
            # Plot seg_SMd
            fig = plt.figure()   
            plt.plot(seg_SMd_distance_use / 1000, mg.at_node['topographic__elevation'][seg_SMd_nodes_use], '.', linewidth = 0.5, color = 'orange')
            plt.plot(seg_SMd_distance / 1000, zr0[seg_SMd_nodes], '--', linewidth = 0.5, color = 'orange')
            plt.plot(seg_SMd_distance_use / 1000, mg.at_node['bedrock__elevation'][seg_SMd_nodes_use], 'k.', linewidth = 0.5)        
            plt.plot(seg_SMd_distance / 1000, br0[seg_SMd_nodes], 'k--', linewidth = 0.5)
            for i in np.arange(0, len(seg_SMd_nodes_use_ed)):
                if seg_SMd_nodes_use_ed[i] == 1:
                    plt.plot(seg_SMd_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_SMd_nodes_use[i]], '.', linewidth = 0.5, color = 'green')
                elif seg_SMd_nodes_use_ed[i] == -1:
                    plt.plot(seg_SMd_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_SMd_nodes_use[i]], '.', linewidth = 0.5, color = 'red')
                if dbedelevdt[seg_SMd_nodes_use[i]] < 0:
                    plt.plot(seg_SMd_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_SMd_nodes_use[i]], '.', linewidth = 0.5, color = 'purple')        
            plt.xlim(xlim_SMd)
            plt.ylim(ylim_SMd)
            plt.grid()
            plt.xlabel('Distance (km)')
            plt.ylabel('Elevation (m)')
            plt.title('$Year$='+str(total_time_r))
            plt.legend(['Current topographic elevation', 'Initial topographic elevation', 'Current bedrock elevation', 'Initial bedrock elevation'], loc = 'upper left', fontsize=6)
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/Segs/Individual/SMd/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)
            plt.close(fig)
            
            # Plot combined segments
            fig = plt.figure()
            #
            plt.plot(seg_MS_distance_use / 1000, mg.at_node['topographic__elevation'][seg_MS_nodes_use], '.', linewidth = 0.5, color = 'orange')
            plt.plot(seg_MS_distance / 1000, zr0[seg_MS_nodes], '--', linewidth = 0.5, color = 'orange')
            plt.plot(seg_MS_distance_use / 1000, mg.at_node['bedrock__elevation'][seg_MS_nodes_use], 'k--', linewidth = 0.5)
            plt.plot(seg_MS_distance / 1000, br0[seg_MS_nodes], 'k--', linewidth = 0.5)
            for i in np.arange(0, len(seg_MS_nodes_use_ed)):
                if seg_MS_nodes_use_ed[i] == 1:
                    plt.plot(seg_MS_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_MS_nodes_use[i]], '.', linewidth = 0.5, color = 'green')
                elif seg_MS_nodes_use_ed[i] == -1:
                    plt.plot(seg_MS_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_MS_nodes_use[i]], '.', linewidth = 0.5, color = 'red')
                if dbedelevdt[seg_MS_nodes_use[i]] < 0:
                    plt.plot(seg_MS_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_MS_nodes_use[i]], '.', linewidth = 0.5, color = 'purple')        
            #
            plt.plot(seg_WPa_distance_use / 1000, mg.at_node['topographic__elevation'][seg_WPa_nodes_use], '.', linewidth = 0.5, color = 'orange')
            plt.plot(seg_WPa_distance / 1000, zr0[seg_WPa_nodes], '--', linewidth = 0.5, color = 'orange')
            plt.plot(seg_WPa_distance_use / 1000, mg.at_node['bedrock__elevation'][seg_WPa_nodes_use], 'k--', linewidth = 0.5)
            plt.plot(seg_SMd_distance / 1000, br0[seg_SMd_nodes], 'k--', linewidth = 0.5)
            for i in np.arange(0, len(seg_WPa_nodes_use_ed)):
                if seg_WPa_nodes_use_ed[i] == 1:
                    plt.plot(seg_WPa_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WPa_nodes_use[i]], '.', linewidth = 0.5, color = 'green')
                elif seg_WPa_nodes_use_ed[i] == -1:
                    plt.plot(seg_WPa_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WPa_nodes_use[i]], '.', linewidth = 0.5, color = 'red')
                if dbedelevdt[seg_WPa_nodes_use[i]] < 0:
                    plt.plot(seg_WPa_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WPa_nodes_use[i]], '.', linewidth = 0.5, color = 'purple')        
            #            
            plt.plot(seg_WPb_distance_use / 1000, mg.at_node['topographic__elevation'][seg_WPb_nodes_use], '.', linewidth = 0.5, color = 'orange')
            plt.plot(seg_WPb_distance / 1000, zr0[seg_WPb_nodes], '--', linewidth = 0.5, color = 'orange')
            plt.plot(seg_WPb_distance_use / 1000, mg.at_node['bedrock__elevation'][seg_WPb_nodes_use], 'k--', linewidth = 0.5)
            plt.plot(seg_SMd_distance / 1000, br0[seg_SMd_nodes], 'k--', linewidth = 0.5)
            for i in np.arange(0, len(seg_WPb_nodes_use_ed)):
                if seg_WPb_nodes_use_ed[i] == 1:
                    plt.plot(seg_WPb_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WPb_nodes_use[i]], '.', linewidth = 0.5, color = 'green')
                elif seg_WPb_nodes_use_ed[i] == -1:
                    plt.plot(seg_WPb_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WPb_nodes_use[i]], '.', linewidth = 0.5, color = 'red')
                if dbedelevdt[seg_WPb_nodes_use[i]] < 0:
                    plt.plot(seg_WPb_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WPb_nodes_use[i]], '.', linewidth = 0.5, color = 'purple')        
            #
            plt.plot(seg_WPc_distance_use / 1000, mg.at_node['topographic__elevation'][seg_WPc_nodes_use], '.', linewidth = 0.5, color = 'orange')
            plt.plot(seg_WPc_distance / 1000, zr0[seg_WPc_nodes], '--', linewidth = 0.5, color = 'orange')
            plt.plot(seg_WPc_distance_use / 1000, mg.at_node['bedrock__elevation'][seg_WPc_nodes_use], 'k--', linewidth = 0.5)
            plt.plot(seg_SMd_distance / 1000, br0[seg_SMd_nodes], 'k--', linewidth = 0.5)
            for i in np.arange(0, len(seg_WPc_nodes_use_ed)):
                if seg_WPc_nodes_use_ed[i] == 1:
                    plt.plot(seg_WPc_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WPc_nodes_use[i]], '.', linewidth = 0.5, color = 'green')
                elif seg_WPc_nodes_use_ed[i] == -1:
                    plt.plot(seg_WPc_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WPc_nodes_use[i]], '.', linewidth = 0.5, color = 'red')
                if dbedelevdt[seg_WPc_nodes_use[i]] < 0:
                    plt.plot(seg_WPc_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WPc_nodes_use[i]], '.', linewidth = 0.5, color = 'purple')        
            #
            plt.plot(seg_WPd_distance_use / 1000, mg.at_node['topographic__elevation'][seg_WPd_nodes_use], '.', linewidth = 0.5, color = 'orange')
            plt.plot(seg_WPd_distance / 1000, zr0[seg_WPd_nodes], '--', linewidth = 0.5, color = 'orange')
            plt.plot(seg_WPd_distance_use / 1000, mg.at_node['bedrock__elevation'][seg_WPd_nodes_use], 'k--', linewidth = 0.5)
            plt.plot(seg_SMd_distance / 1000, br0[seg_SMd_nodes], 'k--', linewidth = 0.5)
            for i in np.arange(0, len(seg_WPd_nodes_use_ed)):
                if seg_WPd_nodes_use_ed[i] == 1:
                    plt.plot(seg_WPd_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WPd_nodes_use[i]], '.', linewidth = 0.5, color = 'green')
                elif seg_WPd_nodes_use_ed[i] == -1:
                    plt.plot(seg_WPd_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WPd_nodes_use[i]], '.', linewidth = 0.5, color = 'red')
                if dbedelevdt[seg_WPd_nodes_use[i]] < 0:
                    plt.plot(seg_WPd_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WPd_nodes_use[i]], '.', linewidth = 0.5, color = 'purple')        
            #
            plt.plot(seg_HDa_distance_use / 1000, mg.at_node['topographic__elevation'][seg_HDa_nodes_use], '.', linewidth = 0.5, color = 'orange')
            plt.plot(seg_HDa_distance / 1000, zr0[seg_HDa_nodes], '--', linewidth = 0.5, color = 'orange')
            plt.plot(seg_HDa_distance_use / 1000, mg.at_node['bedrock__elevation'][seg_HDa_nodes_use], 'k--', linewidth = 0.5)
            plt.plot(seg_HDa_distance / 1000, br0[seg_HDa_nodes], 'k--', linewidth = 0.5)
            for i in np.arange(0, len(seg_HDa_nodes_use_ed)):
                if seg_HDa_nodes_use_ed[i] == 1:
                    plt.plot(seg_HDa_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_HDa_nodes_use[i]], '.', linewidth = 0.5, color = 'green')
                elif seg_HDa_nodes_use_ed[i] == -1:
                    plt.plot(seg_HDa_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_HDa_nodes_use[i]], '.', linewidth = 0.5, color = 'red')
                if dbedelevdt[seg_HDa_nodes_use[i]] < 0:
                    plt.plot(seg_HDa_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_HDa_nodes_use[i]], '.', linewidth = 0.5, color = 'purple')        
            #
            plt.plot(seg_HDb_distance_use / 1000, mg.at_node['topographic__elevation'][seg_HDb_nodes_use], '.', linewidth = 0.5, color = 'orange')
            plt.plot(seg_HDb_distance / 1000, zr0[seg_HDb_nodes], '--', linewidth = 0.5, color = 'orange')
            plt.plot(seg_HDb_distance_use / 1000, mg.at_node['bedrock__elevation'][seg_HDb_nodes_use], 'k--', linewidth = 0.5)
            plt.plot(seg_HDb_distance / 1000, br0[seg_HDb_nodes], 'k--', linewidth = 0.5)
            for i in np.arange(0, len(seg_HDb_nodes_use_ed)):
                if seg_HDb_nodes_use_ed[i] == 1:
                    plt.plot(seg_HDb_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_HDb_nodes_use[i]], '.', linewidth = 0.5, color = 'green')
                elif seg_HDb_nodes_use_ed[i] == -1:
                    plt.plot(seg_HDb_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_HDb_nodes_use[i]], '.', linewidth = 0.5, color = 'red')
                if dbedelevdt[seg_HDb_nodes_use[i]] < 0:
                    plt.plot(seg_HDb_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_HDb_nodes_use[i]], '.', linewidth = 0.5, color = 'purple')        
            #
            plt.plot(seg_GRa_distance_use / 1000, mg.at_node['topographic__elevation'][seg_GRa_nodes_use], '.', linewidth = 0.5, color = 'orange')
            plt.plot(seg_GRa_distance / 1000, zr0[seg_GRa_nodes], '--', linewidth = 0.5, color = 'orange')
            plt.plot(seg_GRa_distance_use / 1000, mg.at_node['bedrock__elevation'][seg_GRa_nodes_use], 'k--', linewidth = 0.5)
            plt.plot(seg_GRa_distance / 1000, br0[seg_GRa_nodes], 'k--', linewidth = 0.5)
            for i in np.arange(0, len(seg_GRa_nodes_use_ed)):
                if seg_GRa_nodes_use_ed[i] == 1:
                    plt.plot(seg_GRa_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_GRa_nodes_use[i]], '.', linewidth = 0.5, color = 'green')
                elif seg_GRa_nodes_use_ed[i] == -1:
                    plt.plot(seg_GRa_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_GRa_nodes_use[i]], '.', linewidth = 0.5, color = 'red')
                if dbedelevdt[seg_GRa_nodes_use[i]] < 0:
                    plt.plot(seg_GRa_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_GRa_nodes_use[i]], '.', linewidth = 0.5, color = 'purple')        
            #
            plt.plot(seg_OVa_distance_use / 1000, mg.at_node['topographic__elevation'][seg_OVa_nodes_use], '.', linewidth = 0.5, color = 'orange')
            plt.plot(seg_OVa_distance / 1000, zr0[seg_OVa_nodes], '--', linewidth = 0.5, color = 'orange')
            plt.plot(seg_OVa_distance_use / 1000, mg.at_node['bedrock__elevation'][seg_OVa_nodes_use], 'k--', linewidth = 0.5)
            plt.plot(seg_OVa_distance / 1000, br0[seg_OVa_nodes], 'k--', linewidth = 0.5)
            for i in np.arange(0, len(seg_OVa_nodes_use_ed)):
                if seg_OVa_nodes_use_ed[i] == 1:
                    plt.plot(seg_OVa_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_OVa_nodes_use[i]], '.', linewidth = 0.5, color = 'green')
                elif seg_OVa_nodes_use_ed[i] == -1:
                    plt.plot(seg_OVa_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_OVa_nodes_use[i]], '.', linewidth = 0.5, color = 'red')
                if dbedelevdt[seg_OVa_nodes_use[i]] < 0:
                    plt.plot(seg_OVa_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_OVa_nodes_use[i]], '.', linewidth = 0.5, color = 'purple')        
            #
            plt.plot(seg_WGa_distance_use / 1000, mg.at_node['topographic__elevation'][seg_WGa_nodes_use], '.', linewidth = 0.5, color = 'orange')
            plt.plot(seg_WGa_distance / 1000, zr0[seg_WGa_nodes], '--', linewidth = 0.5, color = 'orange')
            plt.plot(seg_WGa_distance_use / 1000, mg.at_node['bedrock__elevation'][seg_WGa_nodes_use], 'k--', linewidth = 0.5)
            plt.plot(seg_WGa_distance / 1000, br0[seg_WGa_nodes], 'k--', linewidth = 0.5)
            for i in np.arange(0, len(seg_WGa_nodes_use_ed)):
                if seg_WGa_nodes_use_ed[i] == 1:
                    plt.plot(seg_WGa_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WGa_nodes_use[i]], '.', linewidth = 0.5, color = 'green')
                elif seg_WGa_nodes_use_ed[i] == -1:
                    plt.plot(seg_WGa_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WGa_nodes_use[i]], '.', linewidth = 0.5, color = 'red')
                if dbedelevdt[seg_WGa_nodes_use[i]] < 0:
                    plt.plot(seg_WGa_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WGa_nodes_use[i]], '.', linewidth = 0.5, color = 'purple')        
            #
            plt.plot(seg_WGb_distance_use / 1000, mg.at_node['topographic__elevation'][seg_WGb_nodes_use], '.', linewidth = 0.5, color = 'orange')
            plt.plot(seg_WGb_distance / 1000, zr0[seg_WGb_nodes], '--', linewidth = 0.5, color = 'orange')
            plt.plot(seg_WGb_distance_use / 1000, mg.at_node['bedrock__elevation'][seg_WGb_nodes_use], 'k--', linewidth = 0.5)
            plt.plot(seg_WGb_distance / 1000, br0[seg_WGb_nodes], 'k--', linewidth = 0.5)
            for i in np.arange(0, len(seg_WGb_nodes_use_ed)):
                if seg_WGb_nodes_use_ed[i] == 1:
                    plt.plot(seg_WGb_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WGb_nodes_use[i]], '.', linewidth = 0.5, color = 'green')
                elif seg_WGb_nodes_use_ed[i] == -1:
                    plt.plot(seg_WGb_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WGb_nodes_use[i]], '.', linewidth = 0.5, color = 'red')
                if dbedelevdt[seg_WGb_nodes_use[i]] < 0:
                    plt.plot(seg_WGb_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WGb_nodes_use[i]], '.', linewidth = 0.5, color = 'purple')        
            #
            plt.plot(seg_WGc_distance_use / 1000, mg.at_node['topographic__elevation'][seg_WGc_nodes_use], '.', linewidth = 0.5, color = 'orange')
            plt.plot(seg_WGc_distance / 1000, zr0[seg_WGc_nodes], '--', linewidth = 0.5, color = 'orange')
            plt.plot(seg_WGc_distance_use / 1000, mg.at_node['bedrock__elevation'][seg_WGc_nodes_use], 'k--', linewidth = 0.5)
            plt.plot(seg_WGc_distance / 1000, br0[seg_WGc_nodes], 'k--', linewidth = 0.5)
            for i in np.arange(0, len(seg_WGc_nodes_use_ed)):
                if seg_WGc_nodes_use_ed[i] == 1:
                    plt.plot(seg_WGc_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WGc_nodes_use[i]], '.', linewidth = 0.5, color = 'green')
                elif seg_WGc_nodes_use_ed[i] == -1:
                    plt.plot(seg_WGc_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WGc_nodes_use[i]], '.', linewidth = 0.5, color = 'red')
                if dbedelevdt[seg_WGc_nodes_use[i]] < 0:
                    plt.plot(seg_WGc_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WGc_nodes_use[i]], '.', linewidth = 0.5, color = 'purple')        
            #
            plt.plot(seg_WGd_distance_use / 1000, mg.at_node['topographic__elevation'][seg_WGd_nodes_use], '.', linewidth = 0.5, color = 'orange')
            plt.plot(seg_WGd_distance / 1000, zr0[seg_WGd_nodes], '--', linewidth = 0.5, color = 'orange')
            plt.plot(seg_WGd_distance_use / 1000, mg.at_node['bedrock__elevation'][seg_WGd_nodes_use], 'k--', linewidth = 0.5)
            plt.plot(seg_WGd_distance / 1000, br0[seg_WGd_nodes], 'k--', linewidth = 0.5)
            for i in np.arange(0, len(seg_WGd_nodes_use_ed)):
                if seg_WGd_nodes_use_ed[i] == 1:
                    plt.plot(seg_WGd_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WGd_nodes_use[i]], '.', linewidth = 0.5, color = 'green')
                elif seg_WGd_nodes_use_ed[i] == -1:
                    plt.plot(seg_WGd_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WGd_nodes_use[i]], '.', linewidth = 0.5, color = 'red')
                if dbedelevdt[seg_WGd_nodes_use[i]] < 0:
                    plt.plot(seg_WGd_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WGd_nodes_use[i]], '.', linewidth = 0.5, color = 'purple')        
            #
            plt.plot(seg_WGe_distance_use / 1000, mg.at_node['topographic__elevation'][seg_WGe_nodes_use], '.', linewidth = 0.5, color = 'orange')
            plt.plot(seg_WGe_distance / 1000, zr0[seg_WGe_nodes], '--', linewidth = 0.5, color = 'orange')
            plt.plot(seg_WGe_distance_use / 1000, mg.at_node['bedrock__elevation'][seg_WGe_nodes_use], 'k--', linewidth = 0.5)
            plt.plot(seg_WGe_distance / 1000, br0[seg_WGe_nodes], 'k--', linewidth = 0.5)
            for i in np.arange(0, len(seg_WGe_nodes_use_ed)):
                if seg_WGe_nodes_use_ed[i] == 1:
                    plt.plot(seg_WGe_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WGe_nodes_use[i]], '.', linewidth = 0.5, color = 'green')
                elif seg_WGe_nodes_use_ed[i] == -1:
                    plt.plot(seg_WGe_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WGe_nodes_use[i]], '.', linewidth = 0.5, color = 'red')
                if dbedelevdt[seg_WGe_nodes_use[i]] < 0:
                    plt.plot(seg_WGe_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WGe_nodes_use[i]], '.', linewidth = 0.5, color = 'purple')        
            #
            plt.plot(seg_WGf_distance_use / 1000, mg.at_node['topographic__elevation'][seg_WGf_nodes_use], '.', linewidth = 0.5, color = 'orange')
            plt.plot(seg_WGf_distance / 1000, zr0[seg_WGf_nodes], '--', linewidth = 0.5, color = 'orange')
            plt.plot(seg_WGf_distance_use / 1000, mg.at_node['bedrock__elevation'][seg_WGf_nodes_use], 'k--', linewidth = 0.5)
            plt.plot(seg_WGf_distance / 1000, br0[seg_WGf_nodes], 'k--', linewidth = 0.5)
            for i in np.arange(0, len(seg_WGf_nodes_use_ed)):
                if seg_WGf_nodes_use_ed[i] == 1:
                    plt.plot(seg_WGf_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WGf_nodes_use[i]], '.', linewidth = 0.5, color = 'green')
                elif seg_WGf_nodes_use_ed[i] == -1:
                    plt.plot(seg_WGf_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WGf_nodes_use[i]], '.', linewidth = 0.5, color = 'red')
                if dbedelevdt[seg_WGf_nodes_use[i]] < 0:
                    plt.plot(seg_WGf_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WGf_nodes_use[i]], '.', linewidth = 0.5, color = 'purple')        
            #
            plt.plot(seg_SMa_distance_use / 1000, mg.at_node['topographic__elevation'][seg_SMa_nodes_use], '.', linewidth = 0.5, color = 'orange')
            plt.plot(seg_SMa_distance / 1000, zr0[seg_SMa_nodes], '--', linewidth = 0.5, color = 'orange')
            plt.plot(seg_SMa_distance_use / 1000, mg.at_node['bedrock__elevation'][seg_SMa_nodes_use], 'k--', linewidth = 0.5)
            plt.plot(seg_SMa_distance / 1000, br0[seg_SMa_nodes], 'k--', linewidth = 0.5)
            for i in np.arange(0, len(seg_SMa_nodes_use_ed)):
                if seg_SMa_nodes_use_ed[i] == 1:
                    plt.plot(seg_SMa_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_SMa_nodes_use[i]], '.', linewidth = 0.5, color = 'green')
                elif seg_SMa_nodes_use_ed[i] == -1:
                    plt.plot(seg_SMa_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_SMa_nodes_use[i]], '.', linewidth = 0.5, color = 'red')
                if dbedelevdt[seg_SMa_nodes_use[i]] < 0:
                    plt.plot(seg_SMa_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_SMa_nodes_use[i]], '.', linewidth = 0.5, color = 'purple')        
            #
            plt.plot(seg_SMb_distance_use / 1000, mg.at_node['topographic__elevation'][seg_SMb_nodes_use], '.', linewidth = 0.5, color = 'orange')
            plt.plot(seg_SMb_distance / 1000, zr0[seg_SMb_nodes], '--', linewidth = 0.5, color = 'orange')
            plt.plot(seg_SMb_distance_use / 1000, mg.at_node['bedrock__elevation'][seg_SMb_nodes_use], 'k--', linewidth = 0.5)
            plt.plot(seg_SMb_distance / 1000, br0[seg_SMb_nodes], 'k--', linewidth = 0.5)
            for i in np.arange(0, len(seg_SMb_nodes_use_ed)):
                if seg_SMb_nodes_use_ed[i] == 1:
                    plt.plot(seg_SMb_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_SMb_nodes_use[i]], '.', linewidth = 0.5, color = 'green')
                elif seg_SMb_nodes_use_ed[i] == -1:
                    plt.plot(seg_SMb_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_SMb_nodes_use[i]], '.', linewidth = 0.5, color = 'red')
                if dbedelevdt[seg_SMb_nodes_use[i]] < 0:
                    plt.plot(seg_SMb_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_SMb_nodes_use[i]], '.', linewidth = 0.5, color = 'purple')        
            #
            plt.plot(seg_SMc_distance_use / 1000, mg.at_node['topographic__elevation'][seg_SMc_nodes_use], '.', linewidth = 0.5, color = 'orange')
            plt.plot(seg_SMc_distance / 1000, zr0[seg_SMc_nodes], '--', linewidth = 0.5, color = 'orange')
            plt.plot(seg_SMc_distance_use / 1000, mg.at_node['bedrock__elevation'][seg_SMc_nodes_use], 'k--', linewidth = 0.5)
            plt.plot(seg_SMc_distance / 1000, br0[seg_SMc_nodes], 'k--', linewidth = 0.5)
            for i in np.arange(0, len(seg_SMc_nodes_use_ed)):
                if seg_SMc_nodes_use_ed[i] == 1:
                    plt.plot(seg_SMc_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_SMc_nodes_use[i]], '.', linewidth = 0.5, color = 'green')
                elif seg_SMc_nodes_use_ed[i] == -1:
                    plt.plot(seg_SMc_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_SMc_nodes_use[i]], '.', linewidth = 0.5, color = 'red')
                if dbedelevdt[seg_SMc_nodes_use[i]] < 0:
                    plt.plot(seg_SMc_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_SMc_nodes_use[i]], '.', linewidth = 0.5, color = 'purple')        
            #
            plt.plot(seg_SMd_distance_use / 1000, mg.at_node['topographic__elevation'][seg_SMd_nodes_use], '.', linewidth = 0.5, color = 'orange')
            plt.plot(seg_SMd_distance / 1000, zr0[seg_SMd_nodes], '--', linewidth = 0.5, color = 'orange')
            plt.plot(seg_SMd_distance_use / 1000, mg.at_node['bedrock__elevation'][seg_SMd_nodes_use], 'k--', linewidth = 0.5)
            plt.plot(seg_SMd_distance / 1000, br0[seg_SMd_nodes], 'k--', linewidth = 0.5)
            for i in np.arange(0, len(seg_SMd_nodes_use_ed)):
                if seg_SMd_nodes_use_ed[i] == 1:
                    plt.plot(seg_SMd_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_SMd_nodes_use[i]], '.', linewidth = 0.5, color = 'green')
                elif seg_SMd_nodes_use_ed[i] == -1:
                    plt.plot(seg_SMd_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_SMd_nodes_use[i]], '.', linewidth = 0.5, color = 'red')
                if dbedelevdt[seg_SMd_nodes_use[i]] < 0:
                    plt.plot(seg_SMd_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_SMd_nodes_use[i]], '.', linewidth = 0.5, color = 'purple')        
            #
            plt.xlim(xlim_MS)
            plt.ylim(ylim_MS)
            plt.grid()
            plt.xlabel('Distance (km)')
            plt.ylabel('Elevation (m)')
            plt.title('$Year$='+str(total_time_r))
            plt.legend(['Current topographic elevation', 'Initial topographic elevation', 'Current bedrock elevation', 'Initial bedrock elevation'], loc = 'upper left', fontsize=6)
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/Segs/Combined/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)
            plt.close(fig)
            
            # Get longitudinal profile zone limits
            seg_MS_zone_1_nodes_use = seg_MS_nodes_use[(mg.y_of_node[seg_MS_nodes_use] > Zone_1_Y[0]) & (mg.y_of_node[seg_MS_nodes_use] < Zone_1_Y[1])]
            seg_MS_zone_1_distance_use = seg_MS_distance_use[(mg.y_of_node[seg_MS_nodes_use] > Zone_1_Y[0]) & (mg.y_of_node[seg_MS_nodes_use] < Zone_1_Y[1])]
            seg_MS_zone_1_nodes_use_ed = seg_MS_nodes_use_ed[(mg.y_of_node[seg_MS_nodes_use] > Zone_1_Y[0]) & (mg.y_of_node[seg_MS_nodes_use] < Zone_1_Y[1])]
            #
            seg_MS_zone_2_nodes_use = seg_MS_nodes_use[(mg.y_of_node[seg_MS_nodes_use] > Zone_2_Y[0]) & (mg.y_of_node[seg_MS_nodes_use] < Zone_2_Y[1])]
            seg_MS_zone_2_distance_use = seg_MS_distance_use[(mg.y_of_node[seg_MS_nodes_use] > Zone_2_Y[0]) & (mg.y_of_node[seg_MS_nodes_use] < Zone_2_Y[1])]
            seg_MS_zone_2_nodes_use_ed = seg_MS_nodes_use_ed[(mg.y_of_node[seg_MS_nodes_use] > Zone_2_Y[0]) & (mg.y_of_node[seg_MS_nodes_use] < Zone_2_Y[1])]
            #
            seg_MS_zone_3_nodes_use = seg_MS_nodes_use[(mg.y_of_node[seg_MS_nodes_use] > Zone_3_Y[0]) & (mg.y_of_node[seg_MS_nodes_use] < Zone_3_Y[1])]
            seg_MS_zone_3_distance_use = seg_MS_distance_use[(mg.y_of_node[seg_MS_nodes_use] > Zone_3_Y[0]) & (mg.y_of_node[seg_MS_nodes_use] < Zone_3_Y[1])]
            seg_MS_zone_3_nodes_use_ed = seg_MS_nodes_use_ed[(mg.y_of_node[seg_MS_nodes_use] > Zone_3_Y[0]) & (mg.y_of_node[seg_MS_nodes_use] < Zone_3_Y[1])]
            #
            seg_MS_zone_4_nodes_use = seg_MS_nodes_use[(mg.y_of_node[seg_MS_nodes_use] > Zone_4_Y[0]) & (mg.y_of_node[seg_MS_nodes_use] < Zone_4_Y[1])]
            seg_MS_zone_4_distance_use = seg_MS_distance_use[(mg.y_of_node[seg_MS_nodes_use] > Zone_4_Y[0]) & (mg.y_of_node[seg_MS_nodes_use] < Zone_4_Y[1])]
            seg_MS_zone_4_nodes_use_ed = seg_MS_nodes_use_ed[(mg.y_of_node[seg_MS_nodes_use] > Zone_4_Y[0]) & (mg.y_of_node[seg_MS_nodes_use] < Zone_4_Y[1])]
            #
            seg_MS_zone_5_nodes_use = seg_MS_nodes_use[(mg.y_of_node[seg_MS_nodes_use] > Zone_5_Y[0]) & (mg.y_of_node[seg_MS_nodes_use] < Zone_5_Y[1])]
            seg_MS_zone_5_distance_use = seg_MS_distance_use[(mg.y_of_node[seg_MS_nodes_use] > Zone_5_Y[0]) & (mg.y_of_node[seg_MS_nodes_use] < Zone_5_Y[1])]
            seg_MS_zone_5_nodes_use_ed = seg_MS_nodes_use_ed[(mg.y_of_node[seg_MS_nodes_use] > Zone_5_Y[0]) & (mg.y_of_node[seg_MS_nodes_use] < Zone_5_Y[1])]

            # Plot Zone 1
            fig = plt.figure()
            #
            plt.plot(seg_MS_zone_1_distance_use / 1000, mg.at_node['topographic__elevation'][seg_MS_zone_1_nodes_use], '.', linewidth = 0.5, color = 'orange')
            plt.plot(seg_MS_zone_1_distance / 1000, zr0[seg_MS_zone_1_nodes], '--', linewidth = 0.5, color = 'orange')
            plt.plot(seg_MS_zone_1_distance_use / 1000, mg.at_node['bedrock__elevation'][seg_MS_zone_1_nodes_use], 'k--', linewidth = 0.5)
            plt.plot(seg_MS_zone_1_distance / 1000, br0[seg_MS_zone_1_nodes], 'k--', linewidth = 0.5)
            for i in np.arange(0, len(seg_MS_zone_1_nodes_use_ed)):
                if seg_MS_zone_1_nodes_use_ed[i] == 1:
                    plt.plot(seg_MS_zone_1_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_MS_zone_1_nodes_use[i]], '.', linewidth = 0.5, color = 'green')
                elif seg_MS_zone_1_nodes_use_ed[i] == -1:
                    plt.plot(seg_MS_zone_1_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_MS_zone_1_nodes_use[i]], '.', linewidth = 0.5, color = 'red')
                if dbedelevdt[seg_MS_zone_1_nodes_use[i]] < 0:
                    plt.plot(seg_MS_zone_1_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_MS_zone_1_nodes_use[i]], '.', linewidth = 0.5, color = 'purple')        
            #
            plt.xlim(xlim_Zone_1)
            plt.ylim(ylim_Zone_1)
            plt.grid()
            plt.xlabel('Distance (km)')
            plt.ylabel('Elevation (m)')
            plt.title('$Year$='+str(total_time_r))
            plt.legend(['Topographic elevation', 'Bedrock elevation'], loc = 'upper left')
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/Segs/Zones/Zone_1/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)
            plt.close(fig)        

            # Plot Zone 2
            fig = plt.figure()
            #
            plt.plot(seg_MS_zone_2_distance_use / 1000, mg.at_node['topographic__elevation'][seg_MS_zone_2_nodes_use], '.', linewidth = 0.5, color = 'orange')
            plt.plot(seg_MS_zone_2_distance / 1000, zr0[seg_MS_zone_2_nodes], '--', linewidth = 0.5, color = 'orange')
            plt.plot(seg_MS_zone_2_distance_use / 1000, mg.at_node['bedrock__elevation'][seg_MS_zone_2_nodes_use], 'k--', linewidth = 0.5)
            plt.plot(seg_MS_zone_2_distance / 1000, br0[seg_MS_zone_2_nodes], 'k--', linewidth = 0.5)
            for i in np.arange(0, len(seg_MS_zone_2_nodes_use_ed)):
                if seg_MS_zone_2_nodes_use_ed[i] == 1:
                    plt.plot(seg_MS_zone_2_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_MS_zone_2_nodes_use[i]], '.', linewidth = 0.5, color = 'green')
                elif seg_MS_zone_2_nodes_use_ed[i] == -1:
                    plt.plot(seg_MS_zone_2_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_MS_zone_2_nodes_use[i]], '.', linewidth = 0.5, color = 'red')
                if dbedelevdt[seg_MS_zone_2_nodes_use[i]] < 0:
                    plt.plot(seg_MS_zone_2_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_MS_zone_2_nodes_use[i]], '.', linewidth = 0.5, color = 'purple')        
            #
            plt.plot(seg_WPa_distance_use / 1000, mg.at_node['topographic__elevation'][seg_WPa_nodes_use], '.', linewidth = 0.5, color = 'orange')
            plt.plot(seg_WPa_distance / 1000, zr0[seg_WPa_nodes], '--', linewidth = 0.5, color = 'orange')
            plt.plot(seg_WPa_distance_use / 1000, mg.at_node['bedrock__elevation'][seg_WPa_nodes_use], 'k--', linewidth = 0.5)
            plt.plot(seg_SMd_distance / 1000, br0[seg_SMd_nodes], 'k--', linewidth = 0.5)
            for i in np.arange(0, len(seg_WPa_nodes_use_ed)):
                if seg_WPa_nodes_use_ed[i] == 1:
                    plt.plot(seg_WPa_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WPa_nodes_use[i]], '.', linewidth = 0.5, color = 'green')
                elif seg_WPa_nodes_use_ed[i] == -1:
                    plt.plot(seg_WPa_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WPa_nodes_use[i]], '.', linewidth = 0.5, color = 'red')
                if dbedelevdt[seg_WPa_nodes_use[i]] < 0:
                    plt.plot(seg_WPa_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WPa_nodes_use[i]], '.', linewidth = 0.5, color = 'purple')        
            #            
            plt.plot(seg_WPb_distance_use / 1000, mg.at_node['topographic__elevation'][seg_WPb_nodes_use], '.', linewidth = 0.5, color = 'orange')
            plt.plot(seg_WPb_distance / 1000, zr0[seg_WPb_nodes], '--', linewidth = 0.5, color = 'orange')
            plt.plot(seg_WPb_distance_use / 1000, mg.at_node['bedrock__elevation'][seg_WPb_nodes_use], 'k--', linewidth = 0.5)
            plt.plot(seg_SMd_distance / 1000, br0[seg_SMd_nodes], 'k--', linewidth = 0.5)
            for i in np.arange(0, len(seg_WPb_nodes_use_ed)):
                if seg_WPb_nodes_use_ed[i] == 1:
                    plt.plot(seg_WPb_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WPb_nodes_use[i]], '.', linewidth = 0.5, color = 'green')
                elif seg_WPb_nodes_use_ed[i] == -1:
                    plt.plot(seg_WPb_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WPb_nodes_use[i]], '.', linewidth = 0.5, color = 'red')
                if dbedelevdt[seg_WPb_nodes_use[i]] < 0:
                    plt.plot(seg_WPb_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WPb_nodes_use[i]], '.', linewidth = 0.5, color = 'purple')        
            #
            plt.plot(seg_WPc_distance_use / 1000, mg.at_node['topographic__elevation'][seg_WPc_nodes_use], '.', linewidth = 0.5, color = 'orange')
            plt.plot(seg_WPc_distance / 1000, zr0[seg_WPc_nodes], '--', linewidth = 0.5, color = 'orange')
            plt.plot(seg_WPc_distance_use / 1000, mg.at_node['bedrock__elevation'][seg_WPc_nodes_use], 'k--', linewidth = 0.5)
            plt.plot(seg_SMd_distance / 1000, br0[seg_SMd_nodes], 'k--', linewidth = 0.5)
            for i in np.arange(0, len(seg_WPc_nodes_use_ed)):
                if seg_WPc_nodes_use_ed[i] == 1:
                    plt.plot(seg_WPc_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WPc_nodes_use[i]], '.', linewidth = 0.5, color = 'green')
                elif seg_WPc_nodes_use_ed[i] == -1:
                    plt.plot(seg_WPc_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WPc_nodes_use[i]], '.', linewidth = 0.5, color = 'red')
                if dbedelevdt[seg_WPc_nodes_use[i]] < 0:
                    plt.plot(seg_WPc_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WPc_nodes_use[i]], '.', linewidth = 0.5, color = 'purple')        
            #
            plt.plot(seg_WPd_distance_use / 1000, mg.at_node['topographic__elevation'][seg_WPd_nodes_use], '.', linewidth = 0.5, color = 'orange')
            plt.plot(seg_WPd_distance / 1000, zr0[seg_WPd_nodes], '--', linewidth = 0.5, color = 'orange')
            plt.plot(seg_WPd_distance_use / 1000, mg.at_node['bedrock__elevation'][seg_WPd_nodes_use], 'k--', linewidth = 0.5)
            plt.plot(seg_SMd_distance / 1000, br0[seg_SMd_nodes], 'k--', linewidth = 0.5)
            for i in np.arange(0, len(seg_WPd_nodes_use_ed)):
                if seg_WPd_nodes_use_ed[i] == 1:
                    plt.plot(seg_WPd_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WPd_nodes_use[i]], '.', linewidth = 0.5, color = 'green')
                elif seg_WPd_nodes_use_ed[i] == -1:
                    plt.plot(seg_WPd_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WPd_nodes_use[i]], '.', linewidth = 0.5, color = 'red')
                if dbedelevdt[seg_WPd_nodes_use[i]] < 0:
                    plt.plot(seg_WPd_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WPd_nodes_use[i]], '.', linewidth = 0.5, color = 'purple')        
            #
            plt.xlim(xlim_Zone_2)
            plt.ylim(ylim_Zone_2)
            plt.grid()
            plt.xlabel('Distance (km)')
            plt.ylabel('Elevation (m)')
            plt.title('$Year$='+str(total_time_r))
            plt.legend(['Topographic elevation', 'Bedrock elevation'], loc = 'upper left')
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/Segs/Zones/Zone_2/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)
            plt.close(fig) 

            # Plot Zone 3
            fig = plt.figure()
            #
            plt.plot(seg_MS_zone_3_distance_use / 1000, mg.at_node['topographic__elevation'][seg_MS_zone_3_nodes_use], '.', linewidth = 0.5, color = 'orange')
            plt.plot(seg_MS_zone_3_distance / 1000, zr0[seg_MS_zone_3_nodes], '--', linewidth = 0.5, color = 'orange')
            plt.plot(seg_MS_zone_3_distance_use / 1000, mg.at_node['bedrock__elevation'][seg_MS_zone_3_nodes_use], 'k--', linewidth = 0.5)
            plt.plot(seg_MS_zone_3_distance / 1000, br0[seg_MS_zone_3_nodes], 'k--', linewidth = 0.5)
            for i in np.arange(0, len(seg_MS_zone_3_nodes_use_ed)):
                if seg_MS_zone_3_nodes_use_ed[i] == 1:
                    plt.plot(seg_MS_zone_3_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_MS_zone_3_nodes_use[i]], '.', linewidth = 0.5, color = 'green')
                elif seg_MS_zone_3_nodes_use_ed[i] == -1:
                    plt.plot(seg_MS_zone_3_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_MS_zone_3_nodes_use[i]], '.', linewidth = 0.5, color = 'red')
                if dbedelevdt[seg_MS_zone_3_nodes_use[i]] < 0:
                    plt.plot(seg_MS_zone_3_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_MS_zone_3_nodes_use[i]], '.', linewidth = 0.5, color = 'purple')        
            #
            plt.plot(seg_HDa_distance_use / 1000, mg.at_node['topographic__elevation'][seg_HDa_nodes_use], '.', linewidth = 0.5, color = 'orange')
            plt.plot(seg_HDa_distance / 1000, zr0[seg_HDa_nodes], '--', linewidth = 0.5, color = 'orange')
            plt.plot(seg_HDa_distance_use / 1000, mg.at_node['bedrock__elevation'][seg_HDa_nodes_use], 'k--', linewidth = 0.5)
            plt.plot(seg_HDa_distance / 1000, br0[seg_HDa_nodes], 'k--', linewidth = 0.5)
            for i in np.arange(0, len(seg_HDa_nodes_use_ed)):
                if seg_HDa_nodes_use_ed[i] == 1:
                    plt.plot(seg_HDa_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_HDa_nodes_use[i]], '.', linewidth = 0.5, color = 'green')
                elif seg_HDa_nodes_use_ed[i] == -1:
                    plt.plot(seg_HDa_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_HDa_nodes_use[i]], '.', linewidth = 0.5, color = 'red')
                if dbedelevdt[seg_HDa_nodes_use[i]] < 0:
                    plt.plot(seg_HDa_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_HDa_nodes_use[i]], '.', linewidth = 0.5, color = 'purple')        
            #
            plt.plot(seg_HDb_distance_use / 1000, mg.at_node['topographic__elevation'][seg_HDb_nodes_use], '.', linewidth = 0.5, color = 'orange')
            plt.plot(seg_HDb_distance / 1000, zr0[seg_HDb_nodes], '--', linewidth = 0.5, color = 'orange')
            plt.plot(seg_HDb_distance_use / 1000, mg.at_node['bedrock__elevation'][seg_HDb_nodes_use], 'k--', linewidth = 0.5)
            plt.plot(seg_HDb_distance / 1000, br0[seg_HDb_nodes], 'k--', linewidth = 0.5)
            for i in np.arange(0, len(seg_HDb_nodes_use_ed)):
                if seg_HDb_nodes_use_ed[i] == 1:
                    plt.plot(seg_HDb_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_HDb_nodes_use[i]], '.', linewidth = 0.5, color = 'green')
                elif seg_HDb_nodes_use_ed[i] == -1:
                    plt.plot(seg_HDb_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_HDb_nodes_use[i]], '.', linewidth = 0.5, color = 'red')
                if dbedelevdt[seg_HDb_nodes_use[i]] < 0:
                    plt.plot(seg_HDb_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_HDb_nodes_use[i]], '.', linewidth = 0.5, color = 'purple')        
            #
            plt.plot(seg_GRa_distance_use / 1000, mg.at_node['topographic__elevation'][seg_GRa_nodes_use], '.', linewidth = 0.5, color = 'orange')
            plt.plot(seg_GRa_distance / 1000, zr0[seg_GRa_nodes], '--', linewidth = 0.5, color = 'orange')
            plt.plot(seg_GRa_distance_use / 1000, mg.at_node['bedrock__elevation'][seg_GRa_nodes_use], 'k--', linewidth = 0.5)
            plt.plot(seg_GRa_distance / 1000, br0[seg_GRa_nodes], 'k--', linewidth = 0.5)
            for i in np.arange(0, len(seg_GRa_nodes_use_ed)):
                if seg_GRa_nodes_use_ed[i] == 1:
                    plt.plot(seg_GRa_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_GRa_nodes_use[i]], '.', linewidth = 0.5, color = 'green')
                elif seg_GRa_nodes_use_ed[i] == -1:
                    plt.plot(seg_GRa_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_GRa_nodes_use[i]], '.', linewidth = 0.5, color = 'red')
                if dbedelevdt[seg_GRa_nodes_use[i]] < 0:
                    plt.plot(seg_GRa_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_GRa_nodes_use[i]], '.', linewidth = 0.5, color = 'purple')        
            #
            plt.plot(seg_OVa_distance_use / 1000, mg.at_node['topographic__elevation'][seg_OVa_nodes_use], '.', linewidth = 0.5, color = 'orange')
            plt.plot(seg_OVa_distance / 1000, zr0[seg_OVa_nodes], '--', linewidth = 0.5, color = 'orange')
            plt.plot(seg_OVa_distance_use / 1000, mg.at_node['bedrock__elevation'][seg_OVa_nodes_use], 'k--', linewidth = 0.5)
            plt.plot(seg_OVa_distance / 1000, br0[seg_OVa_nodes], 'k--', linewidth = 0.5)
            for i in np.arange(0, len(seg_OVa_nodes_use_ed)):
                if seg_OVa_nodes_use_ed[i] == 1:
                    plt.plot(seg_OVa_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_OVa_nodes_use[i]], '.', linewidth = 0.5, color = 'green')
                elif seg_OVa_nodes_use_ed[i] == -1:
                    plt.plot(seg_OVa_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_OVa_nodes_use[i]], '.', linewidth = 0.5, color = 'red')
                if dbedelevdt[seg_OVa_nodes_use[i]] < 0:
                    plt.plot(seg_OVa_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_OVa_nodes_use[i]], '.', linewidth = 0.5, color = 'purple')        
            #
            plt.xlim(xlim_Zone_3)
            plt.ylim(ylim_Zone_3)
            plt.grid()
            plt.xlabel('Distance (km)')
            plt.ylabel('Elevation (m)')
            plt.title('$Year$='+str(total_time_r))
            plt.legend(['Topographic elevation', 'Bedrock elevation'], loc = 'upper left')
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/Segs/Zones/Zone_3/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)
            plt.close(fig) 

            # Plot Zone 4
            fig = plt.figure()
            #
            plt.plot(seg_MS_zone_4_distance_use / 1000, mg.at_node['topographic__elevation'][seg_MS_zone_4_nodes_use], '.', linewidth = 0.5, color = 'orange')
            plt.plot(seg_MS_zone_4_distance / 1000, zr0[seg_MS_zone_4_nodes], '--', linewidth = 0.5, color = 'orange')
            plt.plot(seg_MS_zone_4_distance_use / 1000, mg.at_node['bedrock__elevation'][seg_MS_zone_4_nodes_use], 'k--', linewidth = 0.5)
            plt.plot(seg_MS_zone_4_distance / 1000, br0[seg_MS_zone_4_nodes], 'k--', linewidth = 0.5)
            for i in np.arange(0, len(seg_MS_zone_4_nodes_use_ed)):
                if seg_MS_zone_4_nodes_use_ed[i] == 1:
                    plt.plot(seg_MS_zone_4_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_MS_zone_4_nodes_use[i]], '.', linewidth = 0.5, color = 'green')
                elif seg_MS_zone_4_nodes_use_ed[i] == -1:
                    plt.plot(seg_MS_zone_4_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_MS_zone_4_nodes_use[i]], '.', linewidth = 0.5, color = 'red')
                if dbedelevdt[seg_MS_zone_4_nodes_use[i]] < 0:
                    plt.plot(seg_MS_zone_4_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_MS_zone_4_nodes_use[i]], '.', linewidth = 0.5, color = 'purple')        
            #
            plt.plot(seg_WGa_distance_use / 1000, mg.at_node['topographic__elevation'][seg_WGa_nodes_use], '.', linewidth = 0.5, color = 'orange')
            plt.plot(seg_WGa_distance / 1000, zr0[seg_WGa_nodes], '--', linewidth = 0.5, color = 'orange')
            plt.plot(seg_WGa_distance_use / 1000, mg.at_node['bedrock__elevation'][seg_WGa_nodes_use], 'k--', linewidth = 0.5)
            plt.plot(seg_WGa_distance / 1000, br0[seg_WGa_nodes], 'k--', linewidth = 0.5)
            for i in np.arange(0, len(seg_WGa_nodes_use_ed)):
                if seg_WGa_nodes_use_ed[i] == 1:
                    plt.plot(seg_WGa_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WGa_nodes_use[i]], '.', linewidth = 0.5, color = 'green')
                elif seg_WGa_nodes_use_ed[i] == -1:
                    plt.plot(seg_WGa_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WGa_nodes_use[i]], '.', linewidth = 0.5, color = 'red')
                if dbedelevdt[seg_WGa_nodes_use[i]] < 0:
                    plt.plot(seg_WGa_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WGa_nodes_use[i]], '.', linewidth = 0.5, color = 'purple')        
            #
            plt.plot(seg_WGb_distance_use / 1000, mg.at_node['topographic__elevation'][seg_WGb_nodes_use], '.', linewidth = 0.5, color = 'orange')
            plt.plot(seg_WGb_distance / 1000, zr0[seg_WGb_nodes], '--', linewidth = 0.5, color = 'orange')
            plt.plot(seg_WGb_distance_use / 1000, mg.at_node['bedrock__elevation'][seg_WGb_nodes_use], 'k--', linewidth = 0.5)
            plt.plot(seg_WGb_distance / 1000, br0[seg_WGb_nodes], 'k--', linewidth = 0.5)
            for i in np.arange(0, len(seg_WGb_nodes_use_ed)):
                if seg_WGb_nodes_use_ed[i] == 1:
                    plt.plot(seg_WGb_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WGb_nodes_use[i]], '.', linewidth = 0.5, color = 'green')
                elif seg_WGb_nodes_use_ed[i] == -1:
                    plt.plot(seg_WGb_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WGb_nodes_use[i]], '.', linewidth = 0.5, color = 'red')
                if dbedelevdt[seg_WGb_nodes_use[i]] < 0:
                    plt.plot(seg_WGb_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WGb_nodes_use[i]], '.', linewidth = 0.5, color = 'purple')        
            #
            plt.plot(seg_WGc_distance_use / 1000, mg.at_node['topographic__elevation'][seg_WGc_nodes_use], '.', linewidth = 0.5, color = 'orange')
            plt.plot(seg_WGc_distance / 1000, zr0[seg_WGc_nodes], '--', linewidth = 0.5, color = 'orange')
            plt.plot(seg_WGc_distance_use / 1000, mg.at_node['bedrock__elevation'][seg_WGc_nodes_use], 'k--', linewidth = 0.5)
            plt.plot(seg_WGc_distance / 1000, br0[seg_WGc_nodes], 'k--', linewidth = 0.5)
            for i in np.arange(0, len(seg_WGc_nodes_use_ed)):
                if seg_WGc_nodes_use_ed[i] == 1:
                    plt.plot(seg_WGc_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WGc_nodes_use[i]], '.', linewidth = 0.5, color = 'green')
                elif seg_WGc_nodes_use_ed[i] == -1:
                    plt.plot(seg_WGc_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WGc_nodes_use[i]], '.', linewidth = 0.5, color = 'red')
                if dbedelevdt[seg_WGc_nodes_use[i]] < 0:
                    plt.plot(seg_WGc_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WGc_nodes_use[i]], '.', linewidth = 0.5, color = 'purple')        
            #
            plt.plot(seg_WGd_distance_use / 1000, mg.at_node['topographic__elevation'][seg_WGd_nodes_use], '.', linewidth = 0.5, color = 'orange')
            plt.plot(seg_WGd_distance / 1000, zr0[seg_WGd_nodes], '--', linewidth = 0.5, color = 'orange')
            plt.plot(seg_WGd_distance_use / 1000, mg.at_node['bedrock__elevation'][seg_WGd_nodes_use], 'k--', linewidth = 0.5)
            plt.plot(seg_WGd_distance / 1000, br0[seg_WGd_nodes], 'k--', linewidth = 0.5)
            for i in np.arange(0, len(seg_WGd_nodes_use_ed)):
                if seg_WGd_nodes_use_ed[i] == 1:
                    plt.plot(seg_WGd_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WGd_nodes_use[i]], '.', linewidth = 0.5, color = 'green')
                elif seg_WGd_nodes_use_ed[i] == -1:
                    plt.plot(seg_WGd_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WGd_nodes_use[i]], '.', linewidth = 0.5, color = 'red')
                if dbedelevdt[seg_WGd_nodes_use[i]] < 0:
                    plt.plot(seg_WGd_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WGd_nodes_use[i]], '.', linewidth = 0.5, color = 'purple')        
            #
            plt.plot(seg_WGe_distance_use / 1000, mg.at_node['topographic__elevation'][seg_WGe_nodes_use], '.', linewidth = 0.5, color = 'orange')
            plt.plot(seg_WGe_distance / 1000, zr0[seg_WGe_nodes], '--', linewidth = 0.5, color = 'orange')
            plt.plot(seg_WGe_distance_use / 1000, mg.at_node['bedrock__elevation'][seg_WGe_nodes_use], 'k--', linewidth = 0.5)
            plt.plot(seg_WGe_distance / 1000, br0[seg_WGe_nodes], 'k--', linewidth = 0.5)
            for i in np.arange(0, len(seg_WGe_nodes_use_ed)):
                if seg_WGe_nodes_use_ed[i] == 1:
                    plt.plot(seg_WGe_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WGe_nodes_use[i]], '.', linewidth = 0.5, color = 'green')
                elif seg_WGe_nodes_use_ed[i] == -1:
                    plt.plot(seg_WGe_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WGe_nodes_use[i]], '.', linewidth = 0.5, color = 'red')
                if dbedelevdt[seg_WGe_nodes_use[i]] < 0:
                    plt.plot(seg_WGe_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WGe_nodes_use[i]], '.', linewidth = 0.5, color = 'purple')        
            #
            plt.plot(seg_WGf_distance_use / 1000, mg.at_node['topographic__elevation'][seg_WGf_nodes_use], '.', linewidth = 0.5, color = 'orange')
            plt.plot(seg_WGf_distance / 1000, zr0[seg_WGf_nodes], '--', linewidth = 0.5, color = 'orange')
            plt.plot(seg_WGf_distance_use / 1000, mg.at_node['bedrock__elevation'][seg_WGf_nodes_use], 'k--', linewidth = 0.5)
            plt.plot(seg_WGf_distance / 1000, br0[seg_WGf_nodes], 'k--', linewidth = 0.5)
            for i in np.arange(0, len(seg_WGf_nodes_use_ed)):
                if seg_WGf_nodes_use_ed[i] == 1:
                    plt.plot(seg_WGf_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WGf_nodes_use[i]], '.', linewidth = 0.5, color = 'green')
                elif seg_WGf_nodes_use_ed[i] == -1:
                    plt.plot(seg_WGf_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WGf_nodes_use[i]], '.', linewidth = 0.5, color = 'red')
                if dbedelevdt[seg_WGf_nodes_use[i]] < 0:
                    plt.plot(seg_WGf_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_WGf_nodes_use[i]], '.', linewidth = 0.5, color = 'purple')        
                    plt.plot(seg_OVa_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_OVa_nodes_use[i]], '.', linewidth = 0.5, color = 'purple')        
            #
            plt.xlim(xlim_Zone_4)
            plt.ylim(ylim_Zone_4)
            plt.grid()
            plt.xlabel('Distance (km)')
            plt.ylabel('Elevation (m)')
            plt.title('$Year$='+str(total_time_r))
            plt.legend(['Topographic elevation', 'Bedrock elevation'], loc = 'upper left')
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/Segs/Zones/Zone_4/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)
            plt.close(fig) 

            # Plot Zone 5
            fig = plt.figure()
            #
            plt.plot(seg_MS_zone_5_distance_use / 1000, mg.at_node['topographic__elevation'][seg_MS_zone_5_nodes_use], '.', linewidth = 0.5, color = 'orange')
            plt.plot(seg_MS_zone_5_distance / 1000, zr0[seg_MS_zone_5_nodes], '--', linewidth = 0.5, color = 'orange')
            plt.plot(seg_MS_zone_5_distance_use / 1000, mg.at_node['bedrock__elevation'][seg_MS_zone_5_nodes_use], 'k--', linewidth = 0.5)
            plt.plot(seg_MS_zone_5_distance / 1000, br0[seg_MS_zone_5_nodes], 'k--', linewidth = 0.5)
            for i in np.arange(0, len(seg_MS_zone_5_nodes_use_ed)):
                if seg_MS_zone_5_nodes_use_ed[i] == 1:
                    plt.plot(seg_MS_zone_5_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_MS_zone_5_nodes_use[i]], '.', linewidth = 0.5, color = 'green')
                elif seg_MS_zone_5_nodes_use_ed[i] == -1:
                    plt.plot(seg_MS_zone_5_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_MS_zone_5_nodes_use[i]], '.', linewidth = 0.5, color = 'red')
                if dbedelevdt[seg_MS_zone_5_nodes_use[i]] < 0:
                    plt.plot(seg_MS_zone_5_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_MS_zone_5_nodes_use[i]], '.', linewidth = 0.5, color = 'purple')        
            #
            plt.plot(seg_SMa_distance_use / 1000, mg.at_node['topographic__elevation'][seg_SMa_nodes_use], '.', linewidth = 0.5, color = 'orange')
            plt.plot(seg_SMa_distance / 1000, zr0[seg_SMa_nodes], '--', linewidth = 0.5, color = 'orange')
            plt.plot(seg_SMa_distance_use / 1000, mg.at_node['bedrock__elevation'][seg_SMa_nodes_use], 'k--', linewidth = 0.5)
            plt.plot(seg_SMa_distance / 1000, br0[seg_SMa_nodes], 'k--', linewidth = 0.5)
            for i in np.arange(0, len(seg_SMa_nodes_use_ed)):
                if seg_SMa_nodes_use_ed[i] == 1:
                    plt.plot(seg_SMa_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_SMa_nodes_use[i]], '.', linewidth = 0.5, color = 'green')
                elif seg_SMa_nodes_use_ed[i] == -1:
                    plt.plot(seg_SMa_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_SMa_nodes_use[i]], '.', linewidth = 0.5, color = 'red')
                if dbedelevdt[seg_SMa_nodes_use[i]] < 0:
                    plt.plot(seg_SMa_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_SMa_nodes_use[i]], '.', linewidth = 0.5, color = 'purple')        
            #
            plt.plot(seg_SMb_distance_use / 1000, mg.at_node['topographic__elevation'][seg_SMb_nodes_use], '.', linewidth = 0.5, color = 'orange')
            plt.plot(seg_SMb_distance / 1000, zr0[seg_SMb_nodes], '--', linewidth = 0.5, color = 'orange')
            plt.plot(seg_SMb_distance_use / 1000, mg.at_node['bedrock__elevation'][seg_SMb_nodes_use], 'k--', linewidth = 0.5)
            plt.plot(seg_SMb_distance / 1000, br0[seg_SMb_nodes], 'k--', linewidth = 0.5)
            for i in np.arange(0, len(seg_SMb_nodes_use_ed)):
                if seg_SMb_nodes_use_ed[i] == 1:
                    plt.plot(seg_SMb_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_SMb_nodes_use[i]], '.', linewidth = 0.5, color = 'green')
                elif seg_SMb_nodes_use_ed[i] == -1:
                    plt.plot(seg_SMb_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_SMb_nodes_use[i]], '.', linewidth = 0.5, color = 'red')
                if dbedelevdt[seg_SMb_nodes_use[i]] < 0:
                    plt.plot(seg_SMb_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_SMb_nodes_use[i]], '.', linewidth = 0.5, color = 'purple')        
            #
            plt.plot(seg_SMc_distance_use / 1000, mg.at_node['topographic__elevation'][seg_SMc_nodes_use], '.', linewidth = 0.5, color = 'orange')
            plt.plot(seg_SMc_distance / 1000, zr0[seg_SMc_nodes], '--', linewidth = 0.5, color = 'orange')
            plt.plot(seg_SMc_distance_use / 1000, mg.at_node['bedrock__elevation'][seg_SMc_nodes_use], 'k--', linewidth = 0.5)
            plt.plot(seg_SMc_distance / 1000, br0[seg_SMc_nodes], 'k--', linewidth = 0.5)
            for i in np.arange(0, len(seg_SMc_nodes_use_ed)):
                if seg_SMc_nodes_use_ed[i] == 1:
                    plt.plot(seg_SMc_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_SMc_nodes_use[i]], '.', linewidth = 0.5, color = 'green')
                elif seg_SMc_nodes_use_ed[i] == -1:
                    plt.plot(seg_SMc_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_SMc_nodes_use[i]], '.', linewidth = 0.5, color = 'red')
                if dbedelevdt[seg_SMc_nodes_use[i]] < 0:
                    plt.plot(seg_SMc_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_SMc_nodes_use[i]], '.', linewidth = 0.5, color = 'purple')        
            #
            plt.plot(seg_SMd_distance_use / 1000, mg.at_node['topographic__elevation'][seg_SMd_nodes_use], '.', linewidth = 0.5, color = 'orange')
            plt.plot(seg_SMd_distance / 1000, zr0[seg_SMd_nodes], '--', linewidth = 0.5, color = 'orange')
            plt.plot(seg_SMd_distance_use / 1000, mg.at_node['bedrock__elevation'][seg_SMd_nodes_use], 'k--', linewidth = 0.5)
            plt.plot(seg_SMd_distance / 1000, br0[seg_SMd_nodes], 'k--', linewidth = 0.5)
            for i in np.arange(0, len(seg_SMd_nodes_use_ed)):
                if seg_SMd_nodes_use_ed[i] == 1:
                    plt.plot(seg_SMd_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_SMd_nodes_use[i]], '.', linewidth = 0.5, color = 'green')
                elif seg_SMd_nodes_use_ed[i] == -1:
                    plt.plot(seg_SMd_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_SMd_nodes_use[i]], '.', linewidth = 0.5, color = 'red')
                if dbedelevdt[seg_SMd_nodes_use[i]] < 0:
                    plt.plot(seg_SMd_distance_use[i] / 1000, mg.at_node['topographic__elevation'][seg_SMd_nodes_use[i]], '.', linewidth = 0.5, color = 'purple')        
            #
            plt.xlim(xlim_Zone_5)
            plt.ylim(ylim_Zone_5)
            plt.grid()
            plt.xlabel('Distance (km)')
            plt.ylabel('Elevation (m)')
            plt.title('$Year$='+str(total_time_r))
            plt.legend(['Topographic elevation', 'Bedrock elevation'], loc = 'upper left')
            plt.tight_layout()
            fig.savefig('Output_Run_K1ldevelopcal/Segs/Zones/Zone_5/'+str(total_time_r)+'.'+Export_format,  format=Export_format, dpi=dpi)
            plt.close(fig) 
            
        # Export timeseries
        np.savetxt('Output_Run_K1ldevelopcal/CSV/timesteps.csv', timesteps, delimiter = ",")
        np.savetxt('Output_Run_K1ldevelopcal/CSV/times.csv', times, delimiter = ",")
        #
        np.savetxt('Output_Run_K1ldevelopcal/CSV/z_means.csv', z_means, delimiter = ",")
        np.savetxt('Output_Run_K1ldevelopcal/CSV/z_medians.csv', z_medians, delimiter = ",")
        np.savetxt('Output_Run_K1ldevelopcal/CSV/z_2s.csv', z_2s, delimiter = ",")
        np.savetxt('Output_Run_K1ldevelopcal/CSV/z_98s.csv', z_98s, delimiter = ",")
        np.savetxt('Output_Run_K1ldevelopcal/CSV/z_maxs.csv', z_maxs, delimiter = ",")
        #
        np.savetxt('Output_Run_K1ldevelopcal/CSV/dbedelevdt_means.csv', dbedelevdt_means, delimiter = ",")
        np.savetxt('Output_Run_K1ldevelopcal/CSV/dbedelevdt_medians.csv', dbedelevdt_medians, delimiter = ",")
        np.savetxt('Output_Run_K1ldevelopcal/CSV/dbedelevdt_2s.csv', dbedelevdt_2s, delimiter = ",")
        np.savetxt('Output_Run_K1ldevelopcal/CSV/dbedelevdt_98s.csv', dbedelevdt_98s, delimiter = ",")
        np.savetxt('Output_Run_K1ldevelopcal/CSV/dbedelevdt_maxs.csv', dbedelevdt_maxs, delimiter = ",")
        #
        np.savetxt('Output_Run_K1ldevelopcal/CSV/dsoildepthdt_means.csv', dsoildepthdt_means, delimiter = ",")
        np.savetxt('Output_Run_K1ldevelopcal/CSV/dsoildepthdt_medians.csv', dsoildepthdt_medians, delimiter = ",")
        np.savetxt('Output_Run_K1ldevelopcal/CSV/dsoildepthdt_2s.csv', dsoildepthdt_2s, delimiter = ",")
        np.savetxt('Output_Run_K1ldevelopcal/CSV/dsoildepthdt_98s.csv', dsoildepthdt_98s, delimiter = ",")
        np.savetxt('Output_Run_K1ldevelopcal/CSV/dsoildepthdt_maxs.csv', dsoildepthdt_maxs, delimiter = ",")
        #
        np.savetxt('Output_Run_K1ldevelopcal/CSV/dzdt_means.csv', dzdt_means, delimiter = ",")
        np.savetxt('Output_Run_K1ldevelopcal/CSV/dzdt_medians.csv', dzdt_medians, delimiter = ",")
        np.savetxt('Output_Run_K1ldevelopcal/CSV/dzdt_2s.csv', dzdt_2s, delimiter = ",")
        np.savetxt('Output_Run_K1ldevelopcal/CSV/dzdt_98s.csv', dzdt_98s, delimiter = ",")
        np.savetxt('Output_Run_K1ldevelopcal/CSV/dzdt_maxs.csv', dzdt_maxs, delimiter = ",")
        #
        np.savetxt('Output_Run_K1ldevelopcal/CSV/erosionrate_means.csv', erosionrate_means, delimiter = ",")
        np.savetxt('Output_Run_K1ldevelopcal/CSV/erosionrate_medians.csv', erosionrate_medians, delimiter = ",")
        np.savetxt('Output_Run_K1ldevelopcal/CSV/erosionrate_2s.csv', erosionrate_2s, delimiter = ",")
        np.savetxt('Output_Run_K1ldevelopcal/CSV/erosionrate_98s.csv', erosionrate_98s, delimiter = ",")
        np.savetxt('Output_Run_K1ldevelopcal/CSV/erosionrate_maxs.csv', erosionrate_maxs, delimiter = ",")
        #
        np.savetxt('Output_Run_K1ldevelopcal/CSV/netdz_means.csv', netdz_means, delimiter = ",")
        np.savetxt('Output_Run_K1ldevelopcal/CSV/netdz_medians.csv', netdz_medians, delimiter = ",")
        np.savetxt('Output_Run_K1ldevelopcal/CSV/netdz_2s.csv', netdz_2s, delimiter = ",")
        np.savetxt('Output_Run_K1ldevelopcal/CSV/netdz_98s.csv', netdz_98s, delimiter = ",")
        np.savetxt('Output_Run_K1ldevelopcal/CSV/netdz_maxs.csv', netdz_maxs, delimiter = ",")
        #
        np.savetxt('Output_Run_K1ldevelopcal/CSV/sediment_flux_gauge_A.csv', sediment_flux_gauge_A, delimiter = ",")
        np.savetxt('Output_Run_K1ldevelopcal/CSV/sediment_flux_gauge_B.csv', sediment_flux_gauge_B, delimiter = ",")
        np.savetxt('Output_Run_K1ldevelopcal/CSV/sediment_flux_gauge_C.csv', sediment_flux_gauge_C, delimiter = ",")
        np.savetxt('Output_Run_K1ldevelopcal/CSV/sediment_flux_gauge_D.csv', sediment_flux_gauge_D, delimiter = ",")
        np.savetxt('Output_Run_K1ldevelopcal/CSV/sediment_flux_gauge_E.csv', sediment_flux_gauge_E, delimiter = ",")
        np.savetxt('Output_Run_K1ldevelopcal/CSV/sediment_flux_gauge_F.csv', sediment_flux_gauge_F, delimiter = ",")
        np.savetxt('Output_Run_K1ldevelopcal/CSV/sediment_flux_gauge_G.csv', sediment_flux_gauge_G, delimiter = ",")
        np.savetxt('Output_Run_K1ldevelopcal/CSV/sediment_flux_gauge_H.csv', sediment_flux_gauge_H, delimiter = ",")
        np.savetxt('Output_Run_K1ldevelopcal/CSV/sediment_flux_outlet.csv', sediment_flux_outlet, delimiter = ",")
        #
        np.savetxt('Output_Run_K1ldevelopcal/CSV/D1_dvol.csv', D1_dvol, delimiter = ",")
        np.savetxt('Output_Run_K1ldevelopcal/CSV/D2_dvol.csv', D2_dvol, delimiter = ",")
        np.savetxt('Output_Run_K1ldevelopcal/CSV/D3_dvol.csv', D3_dvol, delimiter = ",")
        np.savetxt('Output_Run_K1ldevelopcal/CSV/D4_dvol.csv', D4_dvol, delimiter = ",")
        np.savetxt('Output_Run_K1ldevelopcal/CSV/D5_dvol.csv', D5_dvol, delimiter = ",")
        np.savetxt('Output_Run_K1ldevelopcal/CSV/D6_dvol.csv', D6_dvol, delimiter = ",")
        np.savetxt('Output_Run_K1ldevelopcal/CSV/D7_dvol.csv', D7_dvol, delimiter = ",")
        
        # Reset Plot_Ticker    
        Plot_Ticker = 0
        
    # Export_DEM    
    if Export_DEM == True:
        if Export_DEM_Ticker >= Export_DEM_Interval - 0.0000000001:
            write_esri_ascii('Output_Run_K1ldevelopcal/Export_DEM/'+str(total_time_r)+'.asc', mg, names='topographic__elevation', clobber = True)
            Export_DEM_Ticker = 0

# Section break
print('')

#%% Export final topography

# Print status
print('Exporting final topography...')

# Export final topography   
write_esri_ascii('Output_Run_K1ldevelopcal/Final_topography/Final_topography.asc', mg, names='topographic__elevation', clobber = True)

# Section break
print('')

#%% Finalize

# Print status
print('Finished!')