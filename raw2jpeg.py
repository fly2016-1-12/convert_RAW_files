import numpy
import rawpy
import cv2
import datetime
import imageio
import os

'''
author: sue.li
this is offer to convert raw files to other image format
'''

# a message to remind of time doing or done 
def message(file, bool):
    if bool:
        print(datetime.datetime.now().strftime("%Y-%M-%D %H:%M:%S") + "Converted: " + file)
    else:
        print(datetime.datetime.now().strftime("%Y-%M-%D %H:%M:%S") + "Converting: " + file)
    
# the function to convert file to raw
def batch_convert_raw(in_dir, out_dir, srcType, desType):

    # 判断输出输出的文件夹是否存在
    if not os.path.exists(out_dir):
        print(out_dir, "is not existed.")
        os.mkdir(out_dir)
        print(out_dir, "has been created")
    
    if not os.path.exists(in_dir):
        print(in_dir, "is not existed, please to check it ~~")
        return -1

    # 遍历文件夹并筛选出对应的RAW图，然后进行转换
    list = os.listdir(in_dir)
    try:
        for file in list:
            print(file)
            # format = checkFormat(file)
            for i in srcType:
                if file.lower().endswith(i):
                    message(file, False)
                    path = in_dir + "\\" + file
                    print(path)
                    with rawpy.imread(path) as raw:
                        rgb = raw.postprocess()
                    imageio.imsave(out_dir + "\\"+ file + "." + desType, rgb)
                    message(file, True)
                else:
                    continue
                    # print(file + " is no RAW pic ~~")
    except Exception as e:
        print(e)

if __name__ == "__main__":

    all_format = ['.dng','.raw','.cr2','.crw','.erf','.raf','.tif','.kdc','.dcr','.mos',
		'.mef','.nef','.orf','.rw2','.pef','.x3f','.srw','.srf','.sr2','.arw','.mdc','.mrw']
    convertType = "png"
    batch_convert_raw("E:\\01_Demo\\00_hello\\picture", "E:\\01_Demo\\00_hello\\convert", all_format, convertType)