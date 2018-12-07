# stress-test

# 查看端口数占用
`ss -nat | grep -i "7000" | wc -l`


# 测试1
此次瓶颈在爬虫代码 ,因为每次只返回一次请求

## 使用flask服务器
每分钟平均请求567
开一个scrapy, weblog速率52s/500, 端口占用数量590
开两个scrapy, weblog速率26s/500, 端口占用数量1120

##  使用uwsgi 
每分钟平均请求567
开一个scrapy, weblog速率55, 端口占用数量560
开两个scrapy, weblog速率27, 端口占用数量1120

# 测试2
每次响应处理返回两个请求(2的n次方)

## 本机跑 uwsgi scrapy
观察uwsig日志会时不时卡住,可能是爬虫瓶颈
平均每分钟请求6220
本机开一个scrapy , weblog速率 4.6/500 端口占用数量6676
本机开一个scrapy , weblog速率 26.56/3000 端口占用数量6676

## 本机跑 uwsgi 远程跑scrapy
time()-engine.start_time                        : 3098.428231716156
engine.has_capacity()                           : False
len(engine.downloader.active)                   : 9998
engine.scraper.is_idle()                        : False
engine.spider.name                              : simple
engine.spider_is_idle(engine.spider)            : False
engine.slot.closing                             : False
len(engine.slot.inprogress)                     : 10032
len(engine.slot.scheduler.dqs or [])            : 0
len(engine.slot.scheduler.mqs)                  : 314033
len(engine.scraper.slot.queue)                  : 0
len(engine.scraper.slot.active)                 : 34
engine.scraper.slot.active_size                 : 34816
engine.scraper.slot.itemproc_size               : 0
engine.scraper.slot.needs_backout()             : False
平均每分钟请求6000, weblog速率30/3000 ,端口占用数量5657

## 本机和远程同时开scrapy, 本机跑uwsgi 1.1

weblog速率15s/3000 ,端口占用数量11770
本机平均每分钟请求6550,虚机(12.233)平均每分钟请求5860


## 本机和远程同时开scrapy, 本机跑flask run

weblog速率13s/3000 ,端口占用数量14000
本机平均每分钟请求6550,虚机(12.233)平均每分钟请求7500


## 本机和远程同时开scrapy, 本机跑uwsgi 4.8
感觉瓶颈在爬虫代码, 服务代码简单响应过快
不均匀,各进程性能不均, 
weblog速率 56.2423198223114s/3000req,5个进程 ,端口占用数量12835
本机平均每分钟请求6258,虚机(12.233)平均每分钟请求6649 

## 本机跑flask 
weblog速率13s/3000req, 端口占用数量13271
跑2worker, 远程 平均每分钟7231,本地平均6862


weblog速率27s/3000req, 端口占用数量6482
跑1worker, 远程平均没分钟6437


## 爬虫无法突破瓶颈
**增加scrapy的下载并发,仅在解析处理时间较长时有作用,否则无效
增加web代码复杂度,使其达到峰值

服务端代码瓶颈, 增加爬虫无法速度
weblog速率35s/1000req, 端口占用数量1790
跑2worker, 本地860 pages/min, 远程(12.233) 860 pages/min

weblog速率35s/1000req, 端口占用数量1770
跑1worker, 远程(12.233) 1640 pages/min


# 测试3 爬虫代码固定, 测试web服务器性能

## 本地跑uwsgi
web.log速率35 s/1000req 打开端口数1749 网络流量 2.9Mib(lo)
本地采集代码速率1702 pages/min

## 本地跑uwsgi
web.log速率34.7 s/1000req 打开端口数1742 网络流量 1.5Mib(enp0s31f6),1.5Mib(lo)
远程采集代码速率1723 pages/min

## 本地跑flask run
web.log速率24.8 s/1000req 打开端口数1908 网络流量 2.21Mib(enp0s31f6)
远程采集代码速率2426 pages/min

## 本地跑uwsgi 2,2
web.log速率37 s/1000req * 2 打开端口数3228 网络流量 2.94Mib(enp0s31f6)
远程采集代码速率3226 pages/min

## 本地跑uwsgi 3,3
web.log速率40 s/1000req * 3 打开端口数4190 网络流量 3.39Mib(enp0s31f6)
远程采集代码速率4466 pages/min

# flask web 和 uwsgi的比较结果
当单线程单进程的时候,flask web性能比uwsgi性能高
uwsgi 可通过配置多进程进行性能扩充, 但无法达到1:1的增幅,会存在一定损耗.



#




 



