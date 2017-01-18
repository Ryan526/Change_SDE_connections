import arcpy, os, getpass
newServer = "NEWSERVER"
user = getpass.getuser()
#user_dir = os.path.join(u'C:\\Users\\', user) ### used for local machine
user_dir = u'Y:\\Networked_Directories\\'
os.chdir(user_dir)
################create logfile################
logfile = open("logfile_for_vulture_upgrade_Lambert1.txt", "w")  ## please add the directory name that you are testing (Projects, Hold, etc.)

print>>logfile, "User's home directory: %r" % user_dir

################create mxdList################
mxdList = []
for dirpath,_,filenames in os.walk(user_dir):  ##would love to know what this means
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
    mxd = arcpy.mapping.MapDocument(filePat
	for lyr in arcpy.mapping.ListLayers(mxd):
		try:
			if lyr.supports("dataSource"):
				try:
					if lyr.supports("SERVICEPROPERTIES") and lyr.serviceProperties['ServiceType'] == u'SDE' and lyr.serviceProperties['Server'] == u'vulture':
						try:
							serverName = lyr.serviceProperties[u'Server']
                            databaseName = lyr.serviceProperties[u'Database']
                            if not databaseName.endswith('.sde'):
                                databaseName += '.sde'
                            layerName = lyr.datasetName
                            print>>logfile, "Layer name: %r" % layerName
                            print>>logfile, "Updating: %r, %r:" %(lyr.serviceProperties['Server'], lyr.serviceProperties['Database'])
                            if lyr.supports("workspacePath"):
								find = lyr.workspacePath  ## herein lies the problem, some lyr.workspacePath do not exist
                                print>>logfile, "Current path: %r" % find
                                replacePath = os.path.join("Y:\\AppData\\Roaming\\ESRI\\Desktop10.4\\ArcCatalog\\",os.path.os.path.basename(newServer)+"_"+databaseName)
                                print>>logfile, "New Path: %r" % replacePath
                                mxd.replaceWorkspaces(find,"SDE_WORKSPACE",replacePath,"SDE_WORKSPACE",False)
                                print>>logfile, "****************%r has been updated successfully****************" % lyr.datasetName
							else:
								print>>logfile, "!!!!!!!!Connection path not vaild, layer not updated!!!!!!!!"
						except:
							print>>logfile, "Error: Find path not valid, not default user."
				except:
					print>>logfile, "Unknown error occurred (level 1)."
		except:
			print>>logfile, "Unknown error occurred (level 2)."
	#mxd.save() ##testing without, also need to save as older version (10.2) for some users.
logfile.close()
print "Completed."
