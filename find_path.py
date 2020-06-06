import  os
def FindFile(file_path):
    listPath = os.listdir(file_path) #获取file_path路径下的所有文件夹
    for fileitem in listPath:
        full_path = os.path.join(file_path,fileitem) #获取完整路径名
        if os.path.isdir(full_path):#判断是否是文件夹
            FindFile(full_path)
        else:
            print(fileitem)
            pass
        pass
    else:
        return
    pass

if __name__ == '__main__':
    FindFile('/Users/weishichun')

