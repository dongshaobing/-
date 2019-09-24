# coding:utf-8
#导入处理图片的工具
from PIL import Image
import os


#定义一个函数img_txt 将图片的像素信息转化成文本信息
def img_txt(img):
    #label存放img图片文件的名字
    label = img.split(".")[0]
    # Image.open()方法创建一个img对象，则该对象就具有size/format等属性，可调用show()方法展示图片对象
    img = Image.open("../images/"+img)
    # size属性包括两个值，分别是图片对象img的宽和高
    width = img.size[0]
    height = img.size[1]
    list = [] #创建一个空列表，用于存放图片的文本信息
    for x in range(height):
        for y in range(width):
            color = img.getpixel((y,x))
            #print(color) ,查看像素信息
            #求取像素点的像素和
            sum_of_color = color[0]+color[1]+color[2]
            #如果像素点是白色，求和结果为255+255+255=765 如果是其他颜色，代表是其他颜色，即为手写字迹
            if sum_of_color == 765:
                list.append("1")
            else:
                list.append("0")
        #每一行像素信息读取完之后，换行
        list.append("\n")
    return (list,label)

#定义一个函数write方法，将图片文本信息写入到文件中
def write(txt):
    #打开文本将要写入的文件
    label = txt[1]
    file = open("../numbers_txt/"+label+".txt","a")
    for i in txt[0]:
        file.write(i)

def main():
    # os.listdir()方法可以获取路径下所以文件名字
    documents = os.listdir("../images")
    # print(documents) 测试用
    for i in documents:
        if i == ".DS_Store":
            continue
        #调用img_txt方法
        txt = img_txt(i)
        #调用write方法，将图片文本信息写入到文件里
        write(txt)

if __name__ == "__main__":
    main()
    print("图片转换文本结束。。。。。。")