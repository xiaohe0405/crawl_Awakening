# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 17:18:02 2021

@author: Administrator
"""
import os
import xml.dom.minidom
from xml.dom.minidom import parse
import pandas as pd

# 创建文件夹，且每一集的弹幕数据，保存到CSV文件
class getData_Original(object):  
    # 创建文件夹，且每一集的弹幕数据，保存到CSV文件
    def getData_Original_CSV(self):
        for i in range(1,44):
            for dirpath,dirnames,filenames in os.walk(f'jxnd_XML/{i}'):
                file_count=1
                # 创建DataFrame
                df = pd.DataFrame(columns = ['uid','name','content','likeCount'])
                # 获取每一个集数文件夹下的 文件个数
                for file in filenames:
                    print("当前集数：",i)
                    print(file_count)
                    # 读取每一个文件夹下的 xml文件
                    DOMTree = xml.dom.minidom.parse(f'jxnd_XML/{i}/jxnd-{i}-{file_count}.xml')
                    collection = DOMTree.documentElement
                    bullets = collection.getElementsByTagName('bulletInfo')
                    for bullet in bullets:
                        line_list=[]
                        uid=bullet.getElementsByTagName('uid')[0].childNodes[0].data
                        name=bullet.getElementsByTagName('name')[0].childNodes[0].data
                        likeCount = bullet.getElementsByTagName('likeCount')[0].childNodes[0].data
                        content = bullet.getElementsByTagName('content')[0].childNodes[0].data
                        line_list.append(uid)
                        line_list.append(name)
                        line_list.append(content)
                        line_list.append(likeCount)
                        # print(line_list)
                        df.loc[len(df)] = line_list
                    file_count+=1
                print(df)
                df.to_csv(f"jxnd_CSV_Original/{i}_Original.csv",encoding="utf_8_sig")

                
if __name__=="__main__":
    s=getData_Original()
    s.getData_Original_CSV()
