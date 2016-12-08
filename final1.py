import arcpy, os
Workspace = r"Y:\Hold\pytest"
arcpy.env.workspace = Workspace
mxdList = arcpy.ListFiles("*.mxd")
newServer = "NEWSERVER"
print "Map Documents in %r: %r" % (Workspace, mxdList)
for file in mxdList:
    filePath = os.path.join(Workspace, file)
    mxd = arcpy.mapping.MapDocument(filePath)
    print "In %r" % file
    for lyr in arcpy.mapping.ListLayers(mxd):
        if lyr.supports("SERVICEPROPERTIES"):
            if lyr.serviceProperties['Server'] == u'OLDSERVER':
                # print "%r is being updated." %lyr.serviceProperties['Server']
                if lyr.serviceProperties['ServiceType'] == u'SDE':
                    serverName = lyr.serviceProperties[u'Server']
                    databaseName = lyr.serviceProperties[u'Database']
                    if not databaseName.endswith('.sde'):
                        databaseName += '.sde'
                    print "Updating: %r, %r:" %(lyr.serviceProperties['Server'], lyr.serviceProperties['Database'])
                    print "%r has been updated successfully" % lyr.datasetName
                    layerName = lyr.datasetName
                    print layerName
                    
                    print "Service Type: %r" % lyr.serviceProperties['ServiceType']
                    find = lyr.workspacePath
                    print "Current path: %r" % find
                    print "old server %r:" % serverName
                    ##                    # INSERT for statement: for each current databaseName print the layers being used
                    replacePath = os.path.join(os.path.dirname(find),os.path.os.path.basename(newServer)+databaseName)
                    print "New Path: %r" % replacePath
                    mxd.replaceWorkspaces(find,"SDE_WORKSPACE",replacePath,"SDE_WORKSPACE",False)
                    
                    
                    
    #arcpy.RefreshTOC()
    mxd.save()
