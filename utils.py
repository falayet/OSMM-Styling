#-------------------------------------------------------------------------------
# Name:        utils
# Purpose:
#
# Author:      sbatterby
#
# Created:     05/02/2016
# Copyright:   (c) sbatterby 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import arcpy

# Finds a field in a feature class.
# Returns true if found, false if not
def FindField(featureClass, fieldName):
    found = False

    # Get the list of fields
    fieldList = arcpy.ListFields(featureClass)

    # Loop through and find the field
    for field in fieldList:
        if str.lower(str(field.name)) == str.lower(fieldName):
            found = True
            break

    return found
#-------------------------------------------------------------------------------


# Adds the two style fields to a feature class
def AddStyleFields(featureClass):

    if not FindField(featureClass, "style_description"):
        arcpy.AddField_management(featureClass, "style_description", "TEXT", "", "", 255)

    if not FindField(featureClass, "style_code"):
        arcpy.AddField_management(featureClass, "style_code", "DOUBLE")
#-------------------------------------------------------------------------------


# Deletes the style fields from a feature class
def RemoveStyleFields(featureClass, deleteTextFields):
    fieldList = ["style_description", "style_code"]

    textFieldList = ["font_code", "color_code", "rotation", "geo_x", "geo_y", "anchor"]

    # Execute DeleteField
    arcpy.DeleteField_management(featureClass, fieldList)

    if(deleteTextFields):
        arcpy.DeleteField_management(featureClass, textFieldList)

#-------------------------------------------------------------------------------

# Adds the fields for the carto text table
def AddCartoTextFields(featureClass):
    if not FindField(featureClass, "font_code"):
        arcpy.AddField_management(featureClass, "font_code", "SHORT")

    if not FindField(featureClass, "color_code"):
        arcpy.AddField_management(featureClass, "color_code", "SHORT")

    if not FindField(featureClass, "rotation"):
        arcpy.AddField_management(featureClass, "rotation", "FLOAT")

    if not FindField(featureClass, "geo_x"):
        arcpy.AddField_management(featureClass, "geo_x", "LONG")

    if not FindField(featureClass, "geo_y"):
        arcpy.AddField_management(featureClass, "geo_y", "LONG")

    if not FindField(featureClass, "anchor"):
        arcpy.AddField_management(featureClass, "anchor", "TEXT", "", "", 255)
#-------------------------------------------------------------------------------
