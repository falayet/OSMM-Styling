#-------------------------------------------------------------------------------
# Name:        OSMM Topography Style
# Purpose:
#
# Author:      sbatterby
#
# Created:     04/02/2016
# Copyright:   (c) sbatterby 2016
#-------------------------------------------------------------------------------
import arcpy
import os
import line_style
import area_style
import sym_style
import bnd_style
import pnt_style
import txt_style
import sys
import getopt
import logging
import utils

from arcpy import env



def main():
    loglevel = "DEBUG"
    found_i = False
    found_t = False
    inputDataFolder = ""
    rowCount = 0
    tablePrefix = ""
    toolMode = ""


    # Get tool arguments
    inputDataFolder = arcpy.GetParameterAsText(0)
    tablePrefix = arcpy.GetParameterAsText(1)
    toolMode = arcpy.GetParameterAsText(2)

    
    # Set the workspace
    arcpy.AddMessage("Opening GDB")
    env.workspace = inputDataFolder


    # Check tool mode
    # Add - calculate styles
    # Rem - remove style fields

    if toolMode.lower() == "remove columns":
        RemoveStyle(tablePrefix)
    elif toolMode.lower() == "add style":
        AddStyles(tablePrefix)
    
#-------------------------------------------------------------------------------

# Remove any style fields already added
def RemoveStyle(tablePrefix):
    try:
        arcpy.AddMessage("Removing style columns");
        utils.RemoveStyleFields(tablePrefix +"Anno", False)
        utils.RemoveStyleFields(tablePrefix +"Area", False)
        utils.RemoveStyleFields(tablePrefix +"Bnd", False)
        utils.RemoveStyleFields(tablePrefix +"Line", False)
        utils.RemoveStyleFields(tablePrefix +"Pnt", False)
        utils.RemoveStyleFields(tablePrefix +"Sym", False)
        utils.RemoveStyleFields(tablePrefix + "Anno", True)
        
        arcpy.AddMessage("Style columns removed.");

    except Exception, e:
        arcpy.AddMessage("Error removing columns: "+ str(e));
#-------------------------------------------------------------------------------


# Adds the style fields and calculates the values
def AddStyles(tablePrefix):
    rowCount = 0    
    
    # Add fields if needed
    try:
        arcpy.AddMessage("Adding style columns");
        utils.AddStyleFields(tablePrefix +"Anno")
        utils.AddStyleFields(tablePrefix +"Area")
        utils.AddStyleFields(tablePrefix +"Bnd")
        utils.AddStyleFields(tablePrefix +"Line")
        utils.AddStyleFields(tablePrefix +"Pnt")
        utils.AddStyleFields(tablePrefix +"Sym")
        utils.AddCartoTextFields(tablePrefix + "Anno")
    
        arcpy.AddMessage("Style columns added.");

    except Exception, e:
        arcpy.AddMessage("Error adding columns: "+ str(e));

    fields = ["OBJECTID", "style_description", "style_code", "DescTerm", "DescGroup", "Make", "PhysPres"]

    # Create the update cursor
    with arcpy.da.UpdateCursor(tablePrefix +"Line", fields) as cur:

        # Update the style description.
        arcpy.AddMessage("Updating table: "+ tablePrefix +"Line")

        for row in cur:
            
            row[1] = line_style.CalculateStyleDescription(row)
            row[2] = line_style.CalculateStyleCode(row)
            cur.updateRow(row)

            # Increment row count
            rowCount += 1
    
        arcpy.AddMessage("Updated "+ str(rowCount) +" rows in table: "+ tablePrefix +"Line")


    # Delete cursor and row objects
    del cur, row

    fields = ["OBJECTID", "style_description", "style_code", "DescTerm", "DescGroup", "Make"]

    rowCount = 0

    with arcpy.da.UpdateCursor(tablePrefix +"Area", fields) as cur:

        # Update the style description.
        arcpy.AddMessage("Updating table: "+ tablePrefix +"Area")

        for row in cur:
            row[1] = area_style.CalculateStyleDescription(row)
            row[2] = area_style.CalculateStyleCode(row)
            cur.updateRow(row)

            # Increment row count
            rowCount += 1

        arcpy.AddMessage("Updated "+ str(rowCount) +" rows in table: "+ tablePrefix +"Area")

    # Delete cursor and row objects
    del cur, row

    fields = ["OBJECTID", "style_description", "style_code", "FeatCode"]

    rowCount = 0

    with arcpy.da.UpdateCursor(tablePrefix +"Sym", fields) as cur:

        # Update the style description.
        arcpy.AddMessage("Updating table: "+ tablePrefix +"Sym")

        for row in cur:
            row[1] = sym_style.CalculateStyleDescription(row)
            row[2] = sym_style.CalculateStyleCode(row)
            cur.updateRow(row)

            # Increment row count
            rowCount += 1

        arcpy.AddMessage("Updated "+ str(rowCount) +" rows in table: "+ tablePrefix +"Sym")

    # Delete cursor and row objects
    del cur, row

    fields = ["OBJECTID", "style_description", "style_code", "FeatCode"]

    rowCount = 0

    with arcpy.da.UpdateCursor(tablePrefix +"bnd", fields) as cur:

        # Update the style description.
        arcpy.AddMessage("Updating table: "+ tablePrefix +"bnd")

        for row in cur:
            row[1] = bnd_style.CalculateStyleDescription(row)
            row[2] = bnd_style.CalculateStyleCode(row)
            cur.updateRow(row)

            # Increment row count
            rowCount += 1

        arcpy.AddMessage("Updated "+ str(rowCount) +" rows in table: "+ tablePrefix +"bnd")

    # Delete cursor and row objects
    del cur, row

    fields = ["OBJECTID", "style_description", "style_code", "DescGroup", "DescTerm"]

    rowCount = 0

    with arcpy.da.UpdateCursor(tablePrefix +"pnt", fields) as cur:

        # Update the style description.
        arcpy.AddMessage("Updating table: "+ tablePrefix +"pnt")

        for row in cur:
            row[1] = pnt_style.CalculateStyleDescription(row)
            row[2] = pnt_style.CalculateStyleCode(row)
            cur.updateRow(row)

            # Increment row count
            rowCount += 1

        arcpy.AddMessage("Updated "+ str(rowCount) +" rows in table: "+ tablePrefix +"pnt")

    # Delete cursor and row objects
    del cur, row

    fields = ["OBJECTID", "style_description", "style_code", "DescGroup", "DescTerm", "Make", "TextPos", "font_code", "color_code", "rotation", "geo_x", "geo_y", "anchor", "TextAngle"]

    rowCount = 0

    with arcpy.da.UpdateCursor(tablePrefix +"anno", fields) as cur:

        # Update the style description.
        arcpy.AddMessage("Updating table: "+ tablePrefix +"anno")

        for row in cur:
            row[1] = txt_style.CalculateStyleDescription(row)
            row[2] = txt_style.CalculateStyleCode(row)
            row[7] = txt_style.CalculateFontCode(row)
            row[8] = txt_style.CalculateColorCode(row)
            row[9] = txt_style.CalculateRotation(row)
            row[10] = txt_style.CalculateGeoX(row)
            row[11] = txt_style.CalculateGeoY(row)
            row[12] = txt_style.CalculateAnchor(row)

            cur.updateRow(row)

            # Increment row count
            rowCount += 1

        arcpy.AddMessage("Updated "+ str(rowCount) +" rows in table: "+ tablePrefix +"anno")

    # Delete cursor and row objects
    del cur, row

    arcpy.AddMessage("Finished updating style");

#-----------------------------------------------------------------------------------------------------------------


if __name__ == '__main__':
    main()
