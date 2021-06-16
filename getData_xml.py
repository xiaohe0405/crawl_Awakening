# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 15:30:34 2021

@author: Administrator
"""
import requests
import zlib
import os
class getData(object):
    def __init__(self):
        # 请求头 
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate'
        }
        # 各集弹幕所在的url
        self.bullet_url_list=['79/00/6190815200917900','78/00/7013837360657800','40/00/1304823022584000','71/00/4390755038687100','57/00/5502556903585700',
                         '57/00/6112202947855700','51/00/6734683645675100','38/00/4886493532573800','19/00/1491727665111900','94/00/6261405795529400',
                         '70/00/1826230823597000','52/00/6396169657945200','93/00/6057655670229300','65/00/4819111601376500','71/00/1295999198277100',
                         '08/00/1706708112310800','90/00/8940639726879000','39/00/5471272435593900','31/00/8036598816533100','73/00/1239847588977300',
                         '09/00/4520705906060900','06/00/7828035696150600','73/00/3909455530127300','79/00/3889401383937900','23/00/5030883385212300',
                         '06/00/7454226411130600','04/00/4785420635830400','28/00/2634813998142800','30/00/4937832146893000','64/00/8863631805536400',
                         '32/00/3364784919543200','45/00/8344630502084500','51/00/7410107289505100','08/00/2283465356860800','58/00/3873358067005800',         
                         '64/00/4660282763616400','92/00/3886994886419200','44/00/6044018850884400','48/00/4191015742704800','70/00/3027073097687000',
                         '84/00/8501855008248400','44/00/5021257395074400','54/00/3777098165275400']
    # 构造每一集的URL
    def get_urls(self):
        urls_list=[]
        for i in self.bullet_url_list:
            urls=[]
            for x in range(1,11):
                url=f'https://cmts.iqiyi.com/bullet/{i}_300_{x}.z'
                urls.append(url)
            urls_list.append(urls)
        return urls_list
    # 保存弹幕每一集的xml  创建文件夹
    def createDir(self):
        cur_dir = 'D:/pythonFiles/Era_Of_ Awakening/jxnd_XML'
        for i in range(1,44):
            if os.path.isdir(cur_dir):
                os.mkdir(os.path.join(cur_dir,str(i)))
                
                
    # 保存为xml文件
    def get_xml(self):
        urls_list=self.get_urls()
        count=1
        for urls in urls_list:
            cnt=1
            for url in urls:
                code=requests.get(url, headers=self.headers).status_code
                # print(type(code))
                print("正在请求......")
                if(code==200):
                    content = requests.get(url, headers=self.headers).content
                    decode=zlib.decompress(bytearray(content),15+32).decode('utf-8')
                    with open(f'jxnd_XML/{count}/jxnd-{count}-{cnt}.xml','a',encoding='utf-8') as f:
                        f.write(decode)
                else:
                    print("失败...")
                cnt+=1
            count+=1

if __name__=="__main__":
    s=getData()
    # 创建文件夹
    # s.createDir()
    # 获得觉醒年代 43集 所有弹幕的xml文件
    s.get_xml()