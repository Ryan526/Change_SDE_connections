# Change_SDE_connections

Python 2.7 script to change SDE connections in ArcGIS when changing server instances (eg., OLDSERVER NEWSERVER)

We encountered this problem when a server was being upgraded and we needed to change thousands of temporary SDE connection files on all our users maps on the shared drive or on an individual computer. 

This script was composed to find the existing .MXD files that use existing "OLDSERVER.SDE" connections stored on a user's drive (generally C:\USER\USERNAME\APPDTA\ESRI\ARCMAPVERSION\ARCCATALOG\CONNECTIONFILE.SDE) and replace with a the new server name in Connection Properties.

LIMITATIONS: This script works for OSA and when the DEFAULT user added the original .SDE data to the map.

NEEDS: 
Create connections using arcpy.CreateArcSDEConnectionFile_management up front to ensure new connections will be uniform
Add else statements for files with no .SDE connections
Add else statements for errors
list connections that were not changed
