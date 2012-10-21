import os,shutil

def CopyFolderOs(sFolder,tFolder):
    sourcePath = sFolder
    destPath = tFolder
    for root, dirs, files in os.walk(sourcePath):

        #figure out where we're going
        dest = destPath + root.replace(sourcePath, '')

        #if we're in a directory that doesn't exist in the destination folder
        #then create a new folder
        if not os.path.isdir(dest):
            os.mkdir(dest)
            print 'Directory created at: ' + dest

        #loop through all files in the directory
        for f in files:

            #compute current (old) & new file locations
            oldLoc = root + '\\' + f
            newLoc = dest + '\\' + f

            if not os.path.isfile(newLoc):
                try:
                    shutil.copy2(oldLoc, newLoc)
                    print 'File ' + f + ' copied.'
                except IOError:
                    print 'file "' + f + '" already exists'

def RemoveFolderOs(sourceDir):
    for root, dirs, files in os.walk(sourceDir):
        for f in files:
            os.unlink(os.path.join(root, f))
        for d in dirs:
            shutil.rmtree(os.path.join(root, d))

RemoveFolderOs("D:/apache-tomcat-6.0.26-2/webapps/testCluster");
CopyFolderOs("D:/apache-tomcat-6.0.26-1/webapps/testCluster","D:/apache-tomcat-6.0.26-2/webapps/testCluster");

