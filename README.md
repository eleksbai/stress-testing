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

