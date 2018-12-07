# stress-test

# 查看端口数占用
`ss -nat | grep -i "7000" | wc -l`

# 使用flask服务器
开一个scrapy, weblog速率52, 端口占用数量590
开两个scrapy, weblog速率26, 端口占用数量1120

# 使用uwsgi 