# coding : utf-8

from numpy import *
from PIL import Image
import os
import operator

def K(dict,k):
    sort =sorted(dict.items(),key=operator.itemgetter(1),reverse=False)
    return sort[0:k]

def knn(k,traindata,testdata,lables):
    dict = {}
    for label, list in traindata.items():
        sum_diferrent = 0
        for i in range(len(list)):
            different = int(list[i]) - int(testdata[i])
            different = different ** 2
            sum_diferrent += different
        sum_diferrent = sum_diferrent ** 0.5
        dict[label] = sum_diferrent
    results = K(dict,k)
    for i in results:
        label = i[0].split("_")[0]
        lables[label]+=1
    sort = sorted(lables.items(), key=operator.itemgetter(1), reverse=True)
    print(sort)
    return sort[0][0]

#定义函数test_to_txt，将需要识别的图片转化成文本信息
def test_to_data():
    list = []
    img = Image.open("/Users/dongshaobing/Desktop/3.png")
    width = img.size[0]
    height = img.size[1]
    for y in range(height):
        for x in range(width):
            color = img.getpixel((x,y))
            sum_of_pixel = color[0]+color[1]+color[2]
            if sum_of_pixel == 765:
                list.append("1")
            else:
                list.append("0")
    return list

#定义函数 train_data,将用于识别图片的图片模版信息转化成数字信息
def train_data(txt):
    label = txt.split(".")[0]
    list =[]
    file = open("../numbers_txt/"+txt,"r")
    for i in range(32):
        line = file.readline()
        for j in line:
            if j =="\n":
                continue
            list.append(j)
    return (list,label)

#声明变量testdata存放需要识别的图片的数字信息
testdata = []
#声明字典，用于存储图片模版信息的标签和数字信息
dict_train = {}
def main():
    #调用test_to_data()，将图片信息转化成数字信息赋值给变量
    testdata = test_to_data()
    list = os.listdir("../numbers_txt")
    for i in list:
        data = train_data(i)
        dict_train[data[1]]=data[0]
    print(dict_train.keys())
    labels = {str(i):0 for i in range(10)}
    result = knn(3,dict_train,testdata,labels)
    print("您手写输入的图片是：",result)




if __name__ == "__main__":
    main()
