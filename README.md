# stress-test

# 查看端口数占用
`ss -nat | grep -i "7000" | wc -l`


# 测试1
此次瓶颈在爬虫代码 ,因为每次只返回一次请求

## 使用flask服务器
每分钟平均请求567
开一个scrapy, weblog速率52, 端口占用数量590
开两个scrapy, weblog速率26, 端口占用数量1120

##  使用uwsgi 
每分钟平均请求567
开一个scrapy, weblog速率55, 端口占用数量560
开两个scrapy, weblog速率27, 端口占用数量1120

# 测试2
每次响应处理返回两个请求(2的n次方)