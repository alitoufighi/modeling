import os
import arcpy
#import shapefile
import glob
from arcpy import env

    
# setting my source and target geodatabase 
base_dir = os.path.dirname(__file__)

#setting my clip feature (which is a polygon)
clippers_dir = r"C:\Users\Farzane\Desktop\Master97\Gnome modeling\Postprocessing\clipper"
clippers = glob.glob(clippers_dir + '/*.shp')

# Iterate in base path and work with folders
def list_files(base_dir):                                                                                                  
    r = []                                                                                                            
    subdirs = [x[0] for x in os.walk(base_dir)]                                                                            
    for subdir in subdirs:                                                                                            
        files = os.walk(subdir).next()[2]                                                                             
        src_dir = files
        des_dir = os.path.join (src_dir, "clipped")
        if not os.path.exists(des_dir):
            os.mkdir(des_dir)
                
        # set a workspace    
        arcpy.env.workspace = src_dir
        fclist = arcpy.ListFeatureClasses()
        
        # make list of Grids
        Grid_list = [0 for i in range(len(clippers))]   

        ###########################################
        for fc in fclist:
            src_file_dir, src_file_name = src_dir, fc
            for index, cfs in enumerate(clippers):
                clipper_dir, clipper_name = os.path.split(cfs)
                clipper_name = src_file_name.split('.')[0] + "_" + clipper_name 
                output_dir = os.path.join(des_dir , clipper_name)
                clipped = arcpy.Clip_analysis(fc,cfs,output_dir)
                  
                #Calculate zigmaFID for each Grid in a Scenario
                shps = glob.glob (des_dir + '/*.shp')
                  
                for shp in shps:
                    fid = set(row[0] for row in arcpy.da.SearchCursor(shp, "FID"))
                    count = len (fid)
                    #print (count)
                    Grid_list[index] += count
                    print (Grid_list[index])  

                                                                                         







    










                                                                                                                      
                              