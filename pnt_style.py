#-------------------------------------------------------------------------------
# Name:        Point Style
# Purpose:
#
# Author:      sbatterby
#
# Created:     09/02/2016
# Copyright:   (c) sbatterby 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import arcpy
import os
import logging

logger = logging.getLogger("style_debug")



#-------------------------------------------------------------------------------
# Calculates the style code value
def CalculateStyleCode(row):
    descGroup = row[3]
    descTerm = row[4]
    returnVal = 99

    if descTerm is None:
        descTerm = ""

    if descGroup is None:
        descGroup = ""

    if (descTerm == "Spot Height"):
        returnVal = 1
    elif (descTerm == "Emergency Telephone"):
        returnVal = 2
    elif (descTerm.find("Site Of Heritage")):
        returnVal = 3
    elif (descTerm.find("Culvert")):
        returnVal = 4
    elif (descTerm == "Positioned Nonconiferous Tree"):
        returnVal = 5
    elif (descGroup.find("Inland Water")):
        returnVal = 6
    elif (descGroup.find("Roadside")):
        returnVal = 7
    elif (descTerm.find("Overhead Construction")):
        returnVal = 8
    elif (descGroup.find("Rail")):
        returnVal = 9
    elif (descTerm == "Positioned Coniferous Tree"):
        returnVal = 10
    elif (descTerm == "Boundary Post Or Stone"):
        returnVal = 11
    elif (descTerm == "Triangulation Point Or Pillar"):
        returnVal = 12
    elif (descGroup == "Historic Interest"):
        returnVal = 13
    elif (descGroup == "Landform"):
        returnVal = 14
    elif (descGroup.find("Tidal Water")):
        returnVal = 15
    elif (descGroup.find("Structure")):
        returnVal = 16
    else:
        returnVal = 99

    logger.debug("Style Code:"+ str(returnVal))

    return returnVal
#-------------------------------------------------------------------------------


#-------------------------------------------------------------------------------
# Calculates the style description value
def CalculateStyleDescription(row):
    descGroup = row[3]
    descTerm = row[4]
    returnVal = "Unclassified"

    if descTerm is None:
        descTerm = ""

    if descGroup is None:
        descGroup = ""

    if (descTerm == "Spot Height"):
        returnVal = "Spot Height Point"
    elif (descTerm == "Emergency Telephone"):
        returnVal = "Emergency Telephone Point"
    elif (descTerm.find("Site Of Heritage")):
        returnVal = "Site Of Heritage Point"
    elif (descTerm.find("Culvert")):
        returnVal = "Culvert Point"
    elif (descTerm == "Positioned Nonconiferous Tree"):
        returnVal = "Positioned Nonconiferous Tree Point"
    elif (descGroup.find("Inland Water")):
        returnVal = "Inland Water Point"
    elif (descGroup.find("Roadside")):
        returnVal = "Roadside Point"
    elif (descTerm.find("Overhead Construction")):
        returnVal = "Overhead Construction Point"
    elif (descGroup.find("Rail")):
        returnVal = "Rail Point"
    elif (descTerm == "Positioned Coniferous Tree"):
        returnVal = "Positioned Coniferous Tree Point"
    elif (descTerm == "Boundary Post Or Stone"):
        returnVal = "Boundary Post Point"
    elif (descTerm == "Triangulation Point Or Pillar"):
        returnVal = "Triangulation Point Or Pillar Point"
    elif (descGroup == "Historic Interest"):
        returnVal = "Historic Point"
    elif (descGroup == "Landform"):
        returnVal = "Landform Point"
    elif (descGroup.find("Tidal Water")):
        returnVal = "Tidal Water Point"
    elif (descGroup.find("Structure")):
        returnVal = "Structure Point"
    else:
        returnVal = "Unclassified"


    logger.debug("Style Description:"+ returnVal)

    return returnVal;
#-------------------------------------------------------------------------------




