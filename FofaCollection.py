# encoding=utf-8
import requests
import base64
import json
import os

FOFA_EMAIL = ''
FOFA_KEY = ''

if os.path.exists('./info.txt')==False:
    open('./info.txt','w+',encoding='utf-8')

with open('./info.txt',encoding='utf-8') as infos:
    info_list = infos.readlines()
    try:
        FOFA_EMAIL = info_list[0].replace('\n','')
        FOFA_KEY = info_list[1].replace('\n','')
    except:
        print("【错误】/info.txt文件中没有找到正确的登录信息。")

size = 100


def checkError(FOFA_EMAIL,FOFA_KEY,size):
    if FOFA_EMAIL == '' :
        FOFA_EMAIL = input("【错误】!!未检测到EMAIL,请重新输入EMAIL：")
        with open('info.txt', 'w+',encoding='utf-8') as infos:
            infos.write(FOFA_EMAIL+"\n"+FOFA_KEY)
    if FOFA_KEY == '':
        FOFA_KEY = input("【错误】!!未检测到FOFA_KEY,请重新输入FOFA_KEY：")
        with open('info.txt', 'w+',encoding='utf-8') as infos:
            infos.write(FOFA_EMAIL+"\n"+FOFA_KEY)
    Query = input("【查询语句】请输入查询语句：")
    full = True
    if Query == '':
        Query= input("【错误】!!未检测到查询语句，请重新输入查询语句：")
    try:
        size = int(input("【数据数量】请输入查询数据量(默认100条数据)[可选项]："))
    except:
        size = input("【数据数量】输入类型有误或没有输入，是否重新输入(int类型)[可选项]:")
    if size == '':
        size = 100
    print("【提示】你的信息如下:\n    [1]FOFA_EMAIL:" + FOFA_EMAIL + "  [2]FOFA_KEY:" + FOFA_KEY + "  [3]Query:" + Query+"  [4]size:"+str(size))
    correctInfo = [FOFA_EMAIL,FOFA_KEY,Query,size,full]
    return correctInfo


def collectionData(infos):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1', }
    QBASE64 = base64.b64encode(infos[2].encode('utf-8'))
    url = f"https://fofa.info/api/v1/search/all?email={infos[0]}&key={infos[1]}&qbase64={str(QBASE64,encoding='utf-8')}&size={infos[3]}&full={infos[4]}"
    print("\n【请求URL】"+url)
    resp = requests.get(url=url)
    ip_dir = resp.json()
    ip_lists = ip_dir['results']
    ip_list = []
    for i in range(len(ip_lists)):
        ip_list.append(ip_lists[i][0].replace('https://','').replace('http://',''))
    return ip_list


def fileWrite(ip_list):
    with open('ip.txt','w+', encoding='utf-8') as f:
        for ip in ip_list:
            f.write(ip+"\n")
    with open('ip_http.txt','w+', encoding='utf-8') as f:
        for ip in ip_list:
            f.write("http://"+ip+"\n")
    print('\n【提示】ip收集完成，生成文件：ip.txt，ip_http.txt')

if __name__ == '__main__':
    infos = checkError(FOFA_EMAIL,FOFA_KEY,size)
    ip_list = collectionData(infos)
    fileWrite(ip_list)
