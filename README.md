# FofaCollection
**一个基于Fofa Api 的命令行脚本，用于收集url，JB小子式操作解决你的困难**

**目的：**我们是JB小子，别跟我谈什么学编程写代码，爷就要拿JB日完宇宙所有站(狗头)

## 使用

JB小子式操作

什么？还不会？
```
python.exe fofaScript.py
【数据数量】请输入查询数据量(默认100条数据)[可选项]：100
【查询语句】请输入查询语句：title="hello"
【提示】你的信息如下:
    [1]FOFA_EMAIL: [2]FOFA_KEY:  [3]Query:title="hello"  [4]size:100
['', '', 'title="hello"', 100, True]
https://fofa.so/api/v1/search/all?email=&key=&qbase64=dGl0bGU9ImhlbGxvIg==&size=100&full=True
【提示】ip收集完成，生成文件：ip.txt，ip_http.txt
```

## 说明

第一次运行脚本时，输入的email和fofakey会自动保存到info.txt，之后就不用再次输入了

脚本运行完后，会生成两个文件ip.txt(不带有http://的ip或域名)和ip_http.txt(带有http://的ip或域名)

如果脚本运行报错，检查一下是否开了代理，如果开了代理，需要关闭代理后再运行脚本

