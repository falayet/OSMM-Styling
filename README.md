OSMM-Styling
============

## About
This style tool can be run against your OS MasterMap Topography data to create and calculate the fields and values for applying the correct styles.

Once you have run the tool there will be two new columns in your data which can be used in conjunction with the layer files supplied by the Ordance Survey in their [GitHub Repository](https://github.com/OrdnanceSurvey/OSMM-Topography-Layer-stylesheets/tree/master/Schema%20version%209/Stylesheets/ESRI%20stylesheets%20(LYR)).

When running a COU on the data you will need to remove these columns so they do not interfere with the load, the toolbox provides you with a tool to do this.

## Quickstart

A toolbox is included in this repository and can be used to run the tool. Download the repository zip file and extract it to disk. Then add the toolbox to the ArcTollbox list so it can be run.  

The style tool takes 3 parameters:

- The geodatabase containing the data
- The table prefix used when loading the data
- The tool mode. This will be either "Add Style" to add and creatw the required styles or "Remove Columns" to delete any style columns already added.

The python scripts can also be run using the batch file included in the repository. 

## Issues

Find a bug or want to request a new feature?  Please let us know by submitting an issue.

## Contributing

Anyone and everyone is welcome to contribute.
