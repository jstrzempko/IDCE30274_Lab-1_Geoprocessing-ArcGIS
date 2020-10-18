# Lab 1: Goeprocessing in ArcGIS
Due: 23rd October 2020

This repo was created to submit files for Lab 1 for IDCE 30274 Computer Programming for GIS taught by Professor Shadrock Roberts. It contains: 
•	`flooding.py` from part 2
•	`my_clip.py` from part 3
•	an image of the `lakes_myClip.shp` layer from part 3

This lab was split into 3 parts. In Part 1, students examined tools and toolboxes in ArcGIS to get familiar with the software interface and capabilities. In Part 2, students used the ModelBuilder in ArcMap to create a model that clipped and selected hazardous flood zones in a particular basin. The model was exported as a python script and uploaded to this repo as `flooding.py`. In `flooding.py`, the inputs are `floodzones.shp` and `basin.shp` and the output is `flooding.shp`. In Part 3, the Python window in ArcMap was used to perform geoprocessing methods as practice. In addition, the python script `my_clip.py` was created separately in the Python IDLE on this computer. It clips a lakes layer to the same basin boundary as in Part 2 and was run to demonstrate how geoprocessing outputs can be created independent of the ArcDesktop software using the arcpy library. In the python script `my_clip.py`, the inputs are `lakes.shp` and `basin.shp` and the output is `lakes_myClip.shp`. Once the script was run, the output was opened in ArcMap to see the visual output given below: 



# The Code
The two scripts are meant to be run using shapefiles provided for this class with file paths and names specific to the student submission. If questions arise, users can contact Jess Strzempko at JeStrzempko@clarku.edu for more help and further information.


- an image of the lakes_myClip layer from part 3. If you don't know how to add an image to your Github readme you can [view this video](https://www.youtube.com/watch?reload=9&v=hHbWF1Bvgf4) or [see the instructions at the bottom of this readme](https://github.com/Shadrock/code-snippets).
