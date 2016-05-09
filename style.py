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

    # Get command line arguments
    try:
        opts, args = getopt.getopt(sys.argv[1:], "i:t:m:l:h")
    except getopt.GetoptError as err:
        # print help information and exit:
        print str(err) # will print something like "option -a not recognized"
        sys.exit(2)

    for o, a in opts:
        if o in ('-h'):
            print 'highways.py -i <inputDataFolder> -o <outputDataFolder>'
            sys.exit(2)
        elif o in ("-t"):
            tablePrefix = a
            found_t = True
        elif o in ("-i"):
            inputDataFolder = a
            found_i = True
        elif o in ("-m"):
            toolMode = a
        elif o in ("-l"):
            loglevel = a
        else:
            assert False, "unhandled option"

    # Check required arguments
    if not found_i:
        print 'style.py -i <inputDataFolder> required'
        sys.exit(2)
    elif not found_t:
        print 'style.py -t <tablePrefix> required'
        sys.exit(2)
    elif toolMode == "":
        print 'style.py -m <toolMode> required "Add" or "Rem"'
        sys.exit(2)


    # assuming loglevel is bound to the string value obtained from the
    # command line argument. Convert to upper case to allow the user to
    # specify --log=DEBUG or --log=debug
    numeric_level = getattr(logging, loglevel.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError('Invalid log level: %s' % loglevel)

    logging.basicConfig(filename="style_debug.log", level=numeric_level, filemode="w")

    # create logger
    logger = logging.getLogger("style_debug")
    logger.setLevel(numeric_level)

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(numeric_level)

    # create file handler which logs even debug messages
    fh = logging.FileHandler('style_debug.log')
    fh.setLevel(numeric_level)

    # create formatter
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    # add formatter to ch
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(ch)
    logger.addHandler(fh)

    # Set the workspace
    logger.info("Opening GDB")
    env.workspace = inputDataFolder


    # Check tool mode
    # Add - calculate styles
    # Rem - remove style fields

    if toolMode.lower() == "rem":
        RemoveStyle(tablePrefix, logger)
    elif toolMode.lower(tablePrefix, logger) == "add":
        AddStyles(tablePrefix, logger)
    
#-------------------------------------------------------------------------------

# Remove any style fields already added
def RemoveStyle(tablePrefix, logger):
    try:
        utils.RemoveStyleFields(tablePrefix +"Anno", False)
        utils.RemoveStyleFields(tablePrefix +"Area", False)
        utils.RemoveStyleFields(tablePrefix +"Bnd", False)
        utils.RemoveStyleFields(tablePrefix +"Line", False)
        utils.RemoveStyleFields(tablePrefix +"Pnt", False)
        utils.RemoveStyleFields(tablePrefix +"Sym", False)
        utils.RemoveStyleFields(tablePrefix + "Anno", True)
    except Exception, e:
        logger.error("Error removing columns: "+ str(e));
#-------------------------------------------------------------------------------


# Adds the style fields and calculates the values
def AddStyles(tablePrefix, logger):
    rowCount = 0    
    
    # Add fields if needed
    try:
        utils.AddStyleFields(tablePrefix +"Anno")
        utils.AddStyleFields(tablePrefix +"Area")
        utils.AddStyleFields(tablePrefix +"Bnd")
        utils.AddStyleFields(tablePrefix +"Line")
        utils.AddStyleFields(tablePrefix +"Pnt")
        utils.AddStyleFields(tablePrefix +"Sym")
        utils.AddCartoTextFields(tablePrefix + "Anno")
    except Exception, e:
        logger.error("Error adding columns: "+ str(e));

    fields = ["OBJECTID", "style_description", "style_code", "DescTerm", "DescGroup", "Make", "PhysPres"]

    # Create the update cursor
    with arcpy.da.UpdateCursor(tablePrefix +"Line", fields) as cur:

        # Update the style description.
        for row in cur:
            logger.debug("Updating row: "+ str(row[0]))
            row[1] = line_style.CalculateStyleDescription(row)
            row[2] = line_style.CalculateStyleCode(row)
            cur.updateRow(row)

            # Increment row count
            rowCount += 1

    # Delete cursor and row objects
    del cur, row

    fields = ["OBJECTID", "style_description", "style_code", "DescTerm", "DescGroup", "Make"]

    with arcpy.da.UpdateCursor(tablePrefix +"Area", fields) as cur:

        # Update the style description.
        for row in cur:
            logger.debug("Updating row: "+ str(row[0]))
            row[1] = area_style.CalculateStyleDescription(row)
            row[2] = area_style.CalculateStyleCode(row)
            cur.updateRow(row)

            # Increment row count
            rowCount += 1

    # Delete cursor and row objects
    del cur, row

    fields = ["OBJECTID", "style_description", "style_code", "FeatCode"]

    with arcpy.da.UpdateCursor(tablePrefix +"Sym", fields) as cur:

        # Update the style description.
        for row in cur:
            logger.debug("Updating row: "+ str(row[0]))
            row[1] = sym_style.CalculateStyleDescription(row)
            row[2] = sym_style.CalculateStyleCode(row)
            cur.updateRow(row)

            # Increment row count
            rowCount += 1

    # Delete cursor and row objects
    del cur, row

    fields = ["OBJECTID", "style_description", "style_code", "FeatCode"]

    with arcpy.da.UpdateCursor(tablePrefix +"bnd", fields) as cur:

        # Update the style description.
        for row in cur:
            logger.debug("Updating row: "+ str(row[0]))
            row[1] = bnd_style.CalculateStyleDescription(row)
            row[2] = bnd_style.CalculateStyleCode(row)
            cur.updateRow(row)

            # Increment row count
            rowCount += 1

    # Delete cursor and row objects
    del cur, row

    fields = ["OBJECTID", "style_description", "style_code", "DescGroup", "DescTerm"]

    with arcpy.da.UpdateCursor(tablePrefix +"pnt", fields) as cur:

        # Update the style description.
        for row in cur:
            logger.debug("Updating row: "+ str(row[0]))
            row[1] = pnt_style.CalculateStyleDescription(row)
            row[2] = pnt_style.CalculateStyleCode(row)
            cur.updateRow(row)

            # Increment row count
            rowCount += 1

    # Delete cursor and row objects
    del cur, row

    fields = ["OBJECTID", "style_description", "style_code", "DescGroup", "DescTerm", "Make", "TextPos", "font_code", "color_code", "rotation", "geo_x", "geo_y", "anchor", "TextAngle"]

    with arcpy.da.UpdateCursor(tablePrefix +"anno", fields) as cur:

        # Update the style description.
        for row in cur:
            logger.debug("Updating row: "+ str(row[0]))
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

    # Delete cursor and row objects
    del cur, row

    logger.info("Updated "+ str(rowCount) +" rows");

#-----------------------------------------------------------------------------------------------------------------


if __name__ == '__main__':
    main()
