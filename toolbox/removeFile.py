import os
rootdir = os.getcwd()

safeList = ["py", "pdf"]
removeList = []
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if file.split(".")[1] not in safeList:
            removeList.append(os.path.join(subdir, file))


for removeFile in removeList:
    os.remove(removeFile)
