# Name: Jess Strzempko
# Python Version: 2.7.15
# Lab 1 Geoprocessing in ArcGIS
# Description: This script clips the lakes layer to the basin boundaries.
# It was created as Exercise 2 in Lab 1 Geoprocessing in ArcGIS for IDCE 30274 Computer Programming for GIS. 
# Inputs: lakes.shp [layer of lakes], basin.shp [basin boundary]
# Outputs: lakes_myClip.shp [final layer of lakes within basin boundary]

import arcpy

arcpy.env.workspace = "C:/Users/JeStrzempko/Documents/Comp_Prog/Lab1/Data_Lab_1_Geoprocessing_ArcGIS"

arcpy.Clip_analysis("Data_Lab_1_Geoprocessing_ArcGIS/lakes.shp","Data_Lab_1_Geoprocessing_ArcGIS/basin.shp","Results/lakes_myClip.shp")
