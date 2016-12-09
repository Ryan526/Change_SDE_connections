# Change_SDE_connections
python script to change SDE connections in ArcGIS when changing server instances (eg., OLDSERVER NEWSERVER)
How to change thousands of temporary SDE connection files on hundreds of individual machines when a server name changes?
Script will find the existing .MXD files that use existing .SDE connections stored on a user's drive (generally C:\USER\USERNAME\APPDTA\ESRI\ARCMAPVERSION\ARCCATALOG\CONNECTIONFILE.SDE) 
Script will find existing connections and replace with new connection files
Will add functionality to create connections using arcpy.CreateArcSDEConnectionFile_management at start of script to ensure new connections will be uniform
Add print statements 
Add else statements for files with no .SDE connections
Add else statements for errors
list connections that were not changed
