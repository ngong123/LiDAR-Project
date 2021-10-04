import os
import re

def RDataFileSelect():
    
    Path = 'C:/Users/ngong/Desktop/LiDAR Visualization/RawData/'
    # Path = 'C:/Users/ngong/Desktop/LiDAR Visualization/LinedData/'
    list_Path = []
    
    for DataAll in os.walk(Path):
    #     pass
         
        for line in DataAll[2]:
            
            list_f = (line.strip()).split()     # .strip将字符串string转换为列表list
            str_f = ''.join(list_f)
            PathF = Path + str_f
            list_Path.append(PathF)
    #     print(list_Path)
    
    for FilePath in list_Path[1:]:
#         open语句打开文件，文件打开模式为只读模式，避免改变原始数据
        FileID = open(FilePath,'r')
        
            # 使用readlines语句读取文件，需要循环访问文件返回读到的内容
        for line in FileID.readlines():
            
            # 在读到的数据中进行筛选，获得平赤经、平赤纬、视星等数据
            OutDataLine = line[15:28] + line[28:41] + line[123:129] 
            # right ascension (RA), mean declination (DC), and apparent magnitude (VT)
    #         print (OutDataLine) 
                  
            # 将数据存入本地 
            # open语句打开文件，a+表示追加写模式，若文件不存在则创建，存在则在文件最后追加内容  
            OutData = open('C:/Users/ngong/Desktop/LiDAR Visualization/OutData','a+')
            # writelines()语句将多行字符串写入指定文件      
            OutData.writelines(OutDataLine)
            # 完成后将打开的文件关闭，释放文件占用的内存        
            OutData.close()  
                    
    
            ## 对数据进行筛选
            # 利用正则表达式re模块实现正则匹配，利用re模块的findall函数获取OutDataLine文件中所有符合匹配的字符串，并返回一个列表
            # \d匹配数字，\d+匹配一个或多个数字，\.匹配小数点，\d*匹配小数点之后的数字，实现数字匹配输出
            Data2 = re.findall(r'\d+\.?\d*', OutDataLine)   
#             print(Data2)
        
            # Data2中某些行的数据有些缺失，平赤经、平赤纬、视星数据某几项没有，是无效数据，需要剔除       
            if len(Data2) == 3:
                # 判断视星等，Data2[2]对应视星等，将视星等，<=6(比6等星亮)的恒星数据进行输出
                if float(Data2[2])<= 3:
                    # 此处pass没有意义，占位符，为了让代码运行起来
    #                 pass    
                    print(Data2)
                    # 新建一个文件OutDataVT1，用来存放经过前两步筛选步骤的恒星数据Data2    
                    OutDataVT = open('C:/Users/ngong/Desktop/LiDAR Visualization/OutDataVT','a+')   # 改变筛选语句后，将OutDataVT1文件删除后再运行
                    # Data2中平赤经、平赤纬、视星数据三个数字连着输出，为了看着方便，每个数字后加空格，写入新建的OutDataVT文件中
                    OutDataVT.writelines(['  ']+list(Data2[0])+['  ']+list(Data2[1])+['  ']+list(Data2[2])+['\n'])
                    OutDataVT.close()  
            
        
        
        
        
        
        
        FileID.close() 
    
def main():
    
    RDataFileSelect()


if __name__ == '__main__':
    main()













