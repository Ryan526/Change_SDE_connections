import arcpy, os, getpass
newServer = "NEWSERVERNAME"
user = getpass.getuser()
#user_dir = os.path.join(u'C:\\Users\\', user) ### used for local machine
user_dir = u'Input path to directory here'
os.chdir(user_dir)
################create logfile################
logfile = open("logfile_for_server_upgrade.txt", "w")  
## We did this in batches due to limitations (see readme) and so appended filename with starting directory name 
## (Projects, Department, etc.)

print>>logfile, "User's home directory: %r" % user_dir

################create mxdList################
mxdList = []
for dirpath,_,filenames in os.walk(user_dir):
    for name in filenames:
        if name.endswith('.mxd'):
            mapdoc= os.path.join(dirpath, name)
            mxdList.append(mapdoc)
print>>logfile, "----------------MXD List:----------------"
for mapdoc in mxdList:
	print>>, logfile, mapdoc

################Searching through .mxd documents for SDE connections################
for file in mxdList:
	print>>logfile, "----------------Searching for SDE connections in: %r----------------" % file
	filePath = os.path.join(user_dir, file)
	mxd = arcpy.mapping.MapDocument(filePath)
	for lyr in arcpy.mapping.ListLayers(mxd):
		try:
			if lyr.supports("dataSource"):
				try:
					if lyr.supports("SERVICEPROPERTIES") and lyr.serviceProperties['ServiceType'] == u'SDE' and lyr.serviceProperties['Server'] == u'OLDSERVERNAME':
						try:
							serverName = lyr.serviceProperties[u'Server']
							databaseName = lyr.serviceProperties[u'Database']
							if not databaseName.endswith('.sde'):
								databaseName += '.sde'
							layerName = lyr.datasetName
							print>>logfile, "Layer name: %r" % layerName
							if lyr.supports("workspacePath"):
								find = lyr.workspacePath
								print>>logfile, "Current path: %r" % find
								replacePath = os.path.join("Y:\\AppData\\Roaming\\ESRI\\Desktop10.4\\ArcCatalog\\",os.path.os.path.basename(newServer)+"_"+databaseName) ##  I made up this file structure and put all of the necessary SDE connection files herei
								print>>logfile, "New Path: %r" % replacePath
								mxd.replaceWorkspaces(find,"SDE_WORKSPACE",replacePath,"SDE_WORKSPACE",False) ##False forces the connection
								print>>logfile, "****************%r has been updated successfully****************" % lyr.datasetName
							else:
								print>>logfile, "!!!!!!!!Service Connection Properties not vaild, layer not updated!!!!!!!!"
						except:
							print>>logfile, "Error level 0"
				except:
					print>>logfile, "Error level 1"
		except:
			print>>logfile, "Error level 2"
	## mxd.save() ## test this script first without, then uncomment this line. Also can be modified to save as older version (10.2) for some users.
logfile.close()
print "Completed."
