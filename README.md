# 压力测试相关

[项目地址](https://github.com/eleksbai/stress-testing)

## 镜像使用
```bash
# 开启服务端
sudo docker run -p 5000:80 --rm --name server-temp eleksbai/simple-static-server:nginx
sudo docker run -p 5000:80 --rm --name server-temp eleksbai/simple-static-server:httpd
# 客户端命令测试
ab -n 100000 -c 1000 http://18.18.186.19:5000/

```

## 命令备注
```bash
docker exec -it httpd-temp /bin/bash
docker build static_server/ -t simple-static-server
```


## 说明

本机跑不存在网络io瓶颈, 可以把cpu跑满. 
局域网跑会存在网络io瓶颈.

并发


网络跑满情况下,并发支持到1700 apache

## 错误相关

当并发过多会引发错误
apr_socket_recv: Connection reset by peer (104)


apr_pollset_poll: The timeout specified has expired (70007)
