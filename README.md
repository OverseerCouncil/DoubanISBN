# 豆瓣ISBN查询爬虫



## 程序结构

### 设计方式

由于豆瓣已经关闭查询用API，并且将搜索页返回结果采用javascript进行了加密。

所以本项目采用查询site的方式通过谷歌获取相应豆瓣图书详情页链接。



### 第三方库

Scrapy ：https://github.com/scrapy/scrapy

GoogleSearch ：https://github.com/MarioVilas/googlesearch



## 使用方式

### 运行环境

要求Python3、scrapy库、GoogleSearch库



### 使用方式

#### 输入查询目标

在spiders目录下的book.txt中输入书名，每行一本

#### 运行爬虫

命令行执行``` scrapy crawl doubanISBN -o data.csv```

#### 查看结果

在同目录data.csv查看输出结果

*注意：data.csv可能有编码差异，请自行将utf-8转换为ansi*