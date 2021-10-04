import os

dir = 'C:/Users/ngong/Desktop/LiDAR Visualization/RawData'

path, dirs, files = next(os.walk(dir))
fileCount = len(files)
# print(fileCount)



for i in range(20):
    print ("%02d" % (i))
    rawDataFileName = f'{dir}/tyc2.dat.{"%02d" % (i)}'
    
    with open(rawDataFileName,'r') as f:
        rawDataFileContent = f.readlines()
        with open(f'C:/Users/ngong/Desktop/LiDAR Visualization/LinedData/tyc2.dat.{"%02d" % (i)}', 'w') as f:
            f.writelines(rawDataFileContent)