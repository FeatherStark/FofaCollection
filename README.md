# FofaCollection - FOFA—IP采集工具
**一个基于FoFa Api 的PY脚本，用于收集url，简单操作解决你的困难**



## 环境和使用

版本：Python 3.+

这里需要安装requests库

`
pip install requests
`

**如何使用：**

```
双击FofaCollection.bat

或者python3 FofaCollection.py
```
**运行样例：**
```
【查询语句】请输入查询语句：title="hello"
【数据数量】请输入查询数据量(默认100条数据)[可选项]：20
【提示】你的信息如下:
    [1]FOFA_EMAIL:  [2]FOFA_KEY:  [3]Query:title="hello"  [4]size:20

【请求URL】https://fofa.info/api/v1/search/all?email=&key=&qbase64=aGVsbG8==&size=20&full=True

【提示】ip收集完成，生成文件：ip.txt，ip_http.txt

Process finished with exit code 0
```

## 说明

第一次运行脚本时，脚本会自动检测email和key，如果不存在，则需要输入email和fofakey，并自动保存到info.txt，之后就不用再次输入了

脚本运行完后，会生成两个文件ip.txt(不带有http:// 的ip或域名)和ip_http.txt(带有http:// 的ip或域名)

如果脚本运行报错，检查一下是否开了代理，如果开了代理，需要关闭代理后再运行脚本

**声明：本程序仅用于日常编程学习，请使用者遵守《中华人民共和国网络安全法》，开发者与使用者在使用中产生的任何责任均与本作者无关。下载使用即代表使用者同意上述观点。**
