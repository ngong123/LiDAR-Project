import re

with open('OutData', 'r') as f:
    OutDataLine = f.readline()
    

Data2 = re.findall(r'\d+\.?\d*', OutDataLine)   
# print(Data2)
# 1 or more digits, 0 or 1 any character, 0 or more digits

# Data2中某些行的数据有些缺失，平赤经、平赤纬、视星数据某几项没有，是无效数据，需要剔除       
if len(Data2) == 3:
    # 判断视星等，Data2[2]对应视星等，将视星等，<=6(比6等星亮)的恒星数据进行输出
    if float(Data2[2])<= 3:
        # 此处pass没有意义，占位符，为了让代码运行起来
#                 pass    
        print(Data2)
        # 新建一个文件OutDataVT1，用来存放经过前两步筛选步骤的恒星数据Data2    
        OutDataVT = open('C:/Users/ngong/Desktop/LiDAR Visualization/OutDataVT2','a+')   # 改变筛选语句后，将OutDataVT1文件删除后再运行
        # Data2中平赤经、平赤纬、视星数据三个数字连着输出，为了看着方便，每个数字后加空格，写入新建的OutDataVT文件中
        OutDataVT.writelines(['  ']+list(Data2[0])+['  ']+list(Data2[1])+['  ']+list(Data2[2])+['\n'])
        OutDataVT.close()  
