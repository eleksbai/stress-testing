
# 单server测试, httpd docker 服务
简单返回字符串 "It is work"
`sudo docker run --rm  -v /tmp/www/html:/usr/local/apache2/htdocs/   --name httpd-temp -p 5000:80 -d  httpd`

## 单客户端, 
```
hyman@white-18-18-18-21:~$ ab -n 1000000 -c 700 http://18.18.186.19:5000/
This is ApacheBench, Version 2.3 <$Revision: 1706008 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 18.18.186.19 (be patient)
Completed 100000 requests
Completed 200000 requests
Completed 300000 requests
Completed 400000 requests
Completed 500000 requests
Completed 600000 requests
Completed 700000 requests
Completed 800000 requests
Completed 900000 requests
Completed 1000000 requests
Finished 1000000 requests


Server Software:        Apache/2.4.37
Server Hostname:        18.18.186.19
Server Port:            5000

Document Path:          /
Document Length:        45 bytes

Concurrency Level:      700
Time taken for tests:   55.150 seconds
Complete requests:      1000000
Failed requests:        0
Total transferred:      289000000 bytes
HTML transferred:       45000000 bytes
Requests per second:    18132.51 [#/sec] (mean)
Time per request:       38.605 [ms] (mean)
Time per request:       0.055 [ms] (mean, across all concurrent requests)
Transfer rate:          5117.48 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        4   30 140.0     12    3060
Processing:     3    8  21.2      6    2490
Waiting:        3    8  21.2      6    2490
Total:          8   38 142.0     18    3529

Percentage of the requests served within a certain time (ms)
  50%     18
  66%     19
  75%     19
  80%     19
  90%     20
  95%     20
  98%    238
  99%   1030
 100%   3529 (longest request)


```


## 本地单机请求
```
hyman@hyman-work:~$ ab -n 1000000 -c 700 http://127.0.0.1:5000/
This is ApacheBench, Version 2.3 <$Revision: 1807734 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient)
Completed 100000 requests
Completed 200000 requests
Completed 300000 requests
Completed 400000 requests
Completed 500000 requests
Completed 600000 requests
Completed 700000 requests
Completed 800000 requests
Completed 900000 requests
Completed 1000000 requests
Finished 1000000 requests


Server Software:        Apache/2.4.37
Server Hostname:        127.0.0.1
Server Port:            5000

Document Path:          /
Document Length:        45 bytes

Concurrency Level:      700
Time taken for tests:   62.451 seconds
Complete requests:      1000000
Failed requests:        0
Total transferred:      289000000 bytes
HTML transferred:       45000000 bytes
Requests per second:    16012.59 [#/sec] (mean)
Time per request:       43.716 [ms] (mean)
Time per request:       0.062 [ms] (mean, across all concurrent requests)
Transfer rate:          4519.18 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0   30 169.1      2    3050
Processing:     0   13  23.8     11    1047
Waiting:        0   12  23.7     10    1047
Total:          0   43 172.7     14    3074

Percentage of the requests served within a certain time (ms)
  50%     14
  66%     16
  75%     18
  80%     19
  90%     24
  95%     29
  98%   1027
  99%   1040
 100%   3074 (longest request)

```


## 

```

hyman@hyman-work:/tmp/z2$ ab -n 500000 -c 100 -s 3 http://127.0.0.1:5000/
This is ApacheBench, Version 2.3 <$Revision: 1807734 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient)
Completed 50000 requests
Completed 100000 requests
Completed 150000 requests
Completed 200000 requests
Completed 250000 requests
Completed 300000 requests
Completed 350000 requests
Completed 400000 requests
Completed 450000 requests
Completed 500000 requests
Finished 500000 requests


Server Software:        Apache/2.4.37
Server Hostname:        127.0.0.1
Server Port:            5000

Document Path:          /
Document Length:        45 bytes

Concurrency Level:      100
Time taken for tests:   60.348 seconds
Complete requests:      500000
Failed requests:        0
Total transferred:      144500000 bytes
HTML transferred:       22500000 bytes
Requests per second:    8285.29 [#/sec] (mean)
Time per request:       12.070 [ms] (mean)
Time per request:       0.121 [ms] (mean, across all concurrent requests)
Transfer rate:          2338.33 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    3  52.4      0    1039
Processing:     0    9   5.2      8    1047
Waiting:        0    9   5.2      8    1047
Total:          0   12  52.8      9    1240

Percentage of the requests served within a certain time (ms)
  50%      9
  66%     10
  75%     11
  80%     12
  90%     14
  95%     16
  98%     19
  99%     22
 100%   1240 (longest request)

----------------------------------------------------------------------------

----------------------------------------------------------------------------

hyman@hyman-work:~$ ab -n 500000 -c 100 http://127.0.0.1:5000/
This is ApacheBench, Version 2.3 <$Revision: 1807734 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient)
Completed 50000 requests
Completed 100000 requests
Completed 150000 requests
Completed 200000 requests
Completed 250000 requests
Completed 300000 requests
Completed 350000 requests
Completed 400000 requests
Completed 450000 requests
Completed 500000 requests
Finished 500000 requests


Server Software:        Apache/2.4.37
Server Hostname:        127.0.0.1
Server Port:            5000

Document Path:          /
Document Length:        45 bytes

Concurrency Level:      100
Time taken for tests:   59.476 seconds
Complete requests:      500000
Failed requests:        0
Total transferred:      144500000 bytes
HTML transferred:       22500000 bytes
Requests per second:    8406.71 [#/sec] (mean)
Time per request:       11.895 [ms] (mean)
Time per request:       0.119 [ms] (mean, across all concurrent requests)
Transfer rate:          2372.60 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    3  50.6      0    1036
Processing:     0    9   5.7      8    1048
Waiting:        0    9   5.6      8    1048
Total:          0   12  51.0      9    1237

Percentage of the requests served within a certain time (ms)
  50%      9
  66%     10
  75%     11
  80%     12
  90%     14
  95%     16
  98%     19
  99%     22
 100%   1237 (longest request)


```

# 一代网页测试

网页来源: http://www.linuxvirtualserver.org/zh/lvs2.html
本地单机测试

```bash

hyman@hyman-work:/tmp/www$ ab -n 1000000 -c 700 http://127.0.0.1:5000/
This is ApacheBench, Version 2.3 <$Revision: 1807734 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient)
Completed 100000 requests
Completed 200000 requests
Completed 300000 requests
Completed 400000 requests
Completed 500000 requests
Completed 600000 requests
Completed 700000 requests
Completed 800000 requests
Completed 900000 requests
Completed 1000000 requests
Finished 1000000 requests


Server Software:        Apache/2.4.37
Server Hostname:        127.0.0.1
Server Port:            5000

Document Path:          /
Document Length:        37361 bytes

Concurrency Level:      700
Time taken for tests:   71.006 seconds
Complete requests:      1000000
Failed requests:        0
Total transferred:      37610000000 bytes
HTML transferred:       37361000000 bytes
Requests per second:    14083.35 [#/sec] (mean)
Time per request:       49.704 [ms] (mean)
Time per request:       0.071 [ms] (mean, across all concurrent requests)
Transfer rate:          517260.54 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0   23 141.3      4    3051
Processing:     1   26  67.7     20    1263
Waiting:        0   17  67.6     10    1262
Total:          1   49 159.3     24    3083

Percentage of the requests served within a certain time (ms)
  50%     24
  66%     28
  75%     32
  80%     34
  90%     39
  95%     46
  98%   1029
  99%   1050
 100%   3083 (longest request)

```
局域网客户端单机测试
网卡跑满, 网络瓶颈
```bash
hyman@white-18-18-18-21:~$ ab -n 1000000 -c 700 http://18.18.186.19:5000/
This is ApacheBench, Version 2.3 <$Revision: 1706008 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 18.18.186.19 (be patient)
Completed 100000 requests
Completed 200000 requests
Completed 300000 requests
Completed 400000 requests
Completed 500000 requests
Completed 600000 requests
Completed 700000 requests
Completed 800000 requests
Completed 900000 requests
Completed 1000000 requests
Finished 1000000 requests


Server Software:        Apache/2.4.37
Server Hostname:        18.18.186.19
Server Port:            5000

Document Path:          /
Document Length:        37361 bytes

Concurrency Level:      700
Time taken for tests:   327.610 seconds
Complete requests:      1000000
Failed requests:        0
Total transferred:      37610000000 bytes
HTML transferred:       37361000000 bytes
Requests per second:    3052.41 [#/sec] (mean)
Time per request:       229.327 [ms] (mean)
Time per request:       0.328 [ms] (mean, across all concurrent requests)
Transfer rate:          112110.32 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        1   47 178.0      1    4127
Processing:    65  182 125.4    122    3276
Waiting:        0   14  22.7      5     709
Total:         66  229 224.3    124    4757

Percentage of the requests served within a certain time (ms)
  50%    124
  66%    195
  75%    248
  80%    289
  90%    452
  95%    595
  98%   1132
  99%   1191
 100%   4757 (longest request)


```

单机极限测试  并发约1800

```bash
root@hyman-dev:~# ab -n 100000 -c 1800 http://18.18.186.19:5000/
This is ApacheBench, Version 2.3 <$Revision: 1706008 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 18.18.186.19 (be patient)
Completed 10000 requests
Completed 20000 requests
Completed 30000 requests
Completed 40000 requests
Completed 50000 requests
Completed 60000 requests
Completed 70000 requests
Completed 80000 requests
Completed 90000 requests
apr_socket_recv: Connection reset by peer (104)
Total of 99995 requests completed
root@hyman-dev:~# ab -n 100000 -c 1700 http://18.18.186.19:5000/
This is ApacheBench, Version 2.3 <$Revision: 1706008 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 18.18.186.19 (be patient)
Completed 10000 requests
Completed 20000 requests
Completed 30000 requests
Completed 40000 requests
Completed 50000 requests
Completed 60000 requests
Completed 70000 requests
Completed 80000 requests
Completed 90000 requests
Completed 100000 requests
Finished 100000 requests


Server Software:        Apache/2.4.37
Server Hostname:        18.18.186.19
Server Port:            5000

Document Path:          /
Document Length:        37361 bytes

Concurrency Level:      1700
Time taken for tests:   33.433 seconds
Complete requests:      100000
Failed requests:        0
Total transferred:      3761000000 bytes
HTML transferred:       3736100000 bytes
Requests per second:    2991.04 [#/sec] (mean)
Time per request:       568.365 [ms] (mean)
Time per request:       0.334 [ms] (mean, across all concurrent requests)
Transfer rate:          109856.34 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        1  136 376.8     15   15067
Processing:   114  414 345.4    286   16433
Waiting:        0   41  62.1      8    2188
Total:        117  550 515.8    367   16506

Percentage of the requests served within a certain time (ms)
  50%    367
  66%    545
  75%    691
  80%    814
  90%   1208
  95%   1476
  98%   1923
  99%   2355
 100%  16506 (longest request)

```

httpd 和 nginx 比对测试 本地

```bash
# test nginx 
root@hyman-work:/opt/case/surgery-scheduling# ab -n 100000 -c 1000 http://127.0.0.1:5000/
This is ApacheBench, Version 2.3 <$Revision: 1807734 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient)
Completed 10000 requests
Completed 20000 requests
Completed 30000 requests
Completed 40000 requests
Completed 50000 requests
Completed 60000 requests
Completed 70000 requests
Completed 80000 requests
Completed 90000 requests
Completed 100000 requests
Finished 100000 requests


Server Software:        nginx/1.15.8
Server Hostname:        127.0.0.1
Server Port:            5000

Document Path:          /
Document Length:        37361 bytes

Concurrency Level:      1000
Time taken for tests:   55.124 seconds
Complete requests:      100000
Failed requests:        43
   (Connect: 0, Receive: 0, Length: 43, Exceptions: 0)
Total transferred:      3758083329 bytes
HTML transferred:       3734493477 bytes
Requests per second:    1814.09 [#/sec] (mean)
Time per request:       551.241 [ms] (mean)
Time per request:       0.551 [ms] (mean, across all concurrent requests)
Transfer rate:          66577.05 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   4.2      0    1003
Processing:     1  142 1563.6     10   55031
Waiting:        0  135 1535.7     10   55031
Total:          3  142 1563.7     10   55032

Percentage of the requests served within a certain time (ms)
  50%     10
  66%     11
  75%     11
  80%     11
  90%     11
  95%     12
  98%     70
  99%   1441
 100%  55032 (longest request)
 
# test apache
root@hyman-work:/opt/case/surgery-scheduling# ab -n 100000 -c 1000 http://127.0.0.1:5000/
This is ApacheBench, Version 2.3 <$Revision: 1807734 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient)
Completed 10000 requests
Completed 20000 requests
Completed 30000 requests
Completed 40000 requests
Completed 50000 requests
Completed 60000 requests
Completed 70000 requests
Completed 80000 requests
Completed 90000 requests
Completed 100000 requests
Finished 100000 requests


Server Software:        Apache/2.4.37
Server Hostname:        127.0.0.1
Server Port:            5000

Document Path:          /
Document Length:        37361 bytes

Concurrency Level:      1000
Time taken for tests:   7.255 seconds
Complete requests:      100000
Failed requests:        0
Total transferred:      3761000000 bytes
HTML transferred:       3736100000 bytes
Requests per second:    13782.85 [#/sec] (mean)
Time per request:       72.554 [ms] (mean)
Time per request:       0.073 [ms] (mean, across all concurrent requests)
Transfer rate:          506223.45 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0   36 186.4      2    3031
Processing:     1   34 116.6     18    3063
Waiting:        0   27 116.7     12    3053
Total:          1   69 237.9     19    3078

Percentage of the requests served within a certain time (ms)
  50%     19
  66%     26
  75%     31
  80%     37
  90%     46
  95%     61
  98%   1048
  99%   1067
 100%   3078 (longest request)

```


局域网做客户端测试

```bash
# test httpd
root@hyman-dev:~# ab -n 100000 -c 1000 http://18.18.186.19:5000/
This is ApacheBench, Version 2.3 <$Revision: 1706008 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 18.18.186.19 (be patient)
Completed 10000 requests
Completed 20000 requests
Completed 30000 requests
Completed 40000 requests
Completed 50000 requests
Completed 60000 requests
Completed 70000 requests
Completed 80000 requests
Completed 90000 requests
Completed 100000 requests
Finished 100000 requests


Server Software:        Apache/2.4.37
Server Hostname:        18.18.186.19
Server Port:            5000

Document Path:          /
Document Length:        37361 bytes

Concurrency Level:      1000
Time taken for tests:   33.583 seconds
Complete requests:      100000
Failed requests:        0
Total transferred:      3761000000 bytes
HTML transferred:       3736100000 bytes
Requests per second:    2977.73 [#/sec] (mean)
Time per request:       335.826 [ms] (mean)
Time per request:       0.336 [ms] (mean, across all concurrent requests)
Transfer rate:          109367.76 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        1   70 234.4      2    3144
Processing:    73  255 171.8    190    5280
Waiting:        0   21  34.5      5    1451
Total:         75  325 293.2    226    6331

Percentage of the requests served within a certain time (ms)
  50%    226
  66%    319
  75%    380
  80%    433
  90%    588
  95%   1120
  98%   1273
  99%   1421
 100%   6331 (longest request)
root@hyman-dev:~# ab -n 100000 -c 3000 http://18.18.186.19:5000/
This is ApacheBench, Version 2.3 <$Revision: 1706008 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 18.18.186.19 (be patient)
Completed 10000 requests
Completed 20000 requests
Completed 30000 requests
Completed 40000 requests
Completed 50000 requests
Completed 60000 requests
Completed 70000 requests
Completed 80000 requests
Completed 90000 requests
apr_socket_recv: Connection reset by peer (104)
Total of 99944 requests completed

# test nginx

root@hyman-dev:~# ab -n 100000 -c 1000 http://18.18.186.19:5000/
This is ApacheBench, Version 2.3 <$Revision: 1706008 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 18.18.186.19 (be patient)
Completed 10000 requests
Completed 20000 requests
Completed 30000 requests
Completed 40000 requests
Completed 50000 requests
Completed 60000 requests
Completed 70000 requests
Completed 80000 requests
Completed 90000 requests
Completed 100000 requests
Finished 100000 requests


Server Software:        nginx/1.15.8
Server Hostname:        18.18.186.19
Server Port:            5000

Document Path:          /
Document Length:        37361 bytes

Concurrency Level:      1000
Time taken for tests:   33.295 seconds
Complete requests:      100000
Failed requests:        0
Total transferred:      3759700000 bytes
HTML transferred:       3736100000 bytes
Requests per second:    3003.44 [#/sec] (mean)
Time per request:       332.951 [ms] (mean)
Time per request:       0.333 [ms] (mean, across all concurrent requests)
Transfer rate:          110273.93 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        1   69 224.9      2    5017
Processing:    75  257 184.6    181    8487
Waiting:        0   25  41.3      6     722
Total:         79  326 296.0    214    8508

Percentage of the requests served within a certain time (ms)
  50%    214
  66%    289
  75%    379
  80%    428
  90%    627
  95%   1083
  98%   1260
  99%   1434
 100%   8508 (longest request)
 
root@hyman-dev:~# ab -n 100000 -c 3000 http://18.18.186.19:5000/
This is ApacheBench, Version 2.3 <$Revision: 1706008 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 18.18.186.19 (be patient)
Completed 10000 requests
Completed 20000 requests
Completed 30000 requests
Completed 40000 requests
Completed 50000 requests
Completed 60000 requests
Completed 70000 requests
Completed 80000 requests
Completed 90000 requests
Completed 100000 requests
Finished 100000 requests


Server Software:        
Server Hostname:        18.18.186.19
Server Port:            5000

Document Path:          /
Document Length:        0 bytes

Concurrency Level:      3000
Time taken for tests:   36.338 seconds
Complete requests:      100000
Failed requests:        100000
   (Connect: 0, Receive: 0, Length: 98400, Exceptions: 1600)
Total transferred:      3699544800 bytes
HTML transferred:       3676322400 bytes
Requests per second:    2751.95 [#/sec] (mean)
Time per request:       1090.136 [ms] (mean)
Time per request:       0.363 [ms] (mean, across all concurrent requests)
Transfer rate:          99423.44 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        1  266 663.8     46   31134
Processing:    21  684 622.2    524   20303
Waiting:        0   56  89.6     35    5202
Total:         78  950 921.6    673   31722

Percentage of the requests served within a certain time (ms)
  50%    673
  66%   1024
  75%   1270
  80%   1416
  90%   1919
  95%   2521
  98%   3540
  99%   4109
 100%  31722 (longest request)


```

重启后的测试 , 两个比较测试
```bash
root@hyman-dev:~# ab -n 100000 -c 1000 http://18.18.186.19:5000/
This is ApacheBench, Version 2.3 <$Revision: 1706008 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 18.18.186.19 (be patient)
Completed 10000 requests
Completed 20000 requests
Completed 30000 requests
Completed 40000 requests
Completed 50000 requests
Completed 60000 requests
Completed 70000 requests
Completed 80000 requests
Completed 90000 requests
Completed 100000 requests
Finished 100000 requests


Server Software:        nginx/1.15.8
Server Hostname:        18.18.186.19
Server Port:            5000

Document Path:          /
Document Length:        37361 bytes

Concurrency Level:      1000
Time taken for tests:   33.116 seconds
Complete requests:      100000
Failed requests:        0
Total transferred:      3759700000 bytes
HTML transferred:       3736100000 bytes
Requests per second:    3019.67 [#/sec] (mean)
Time per request:       331.162 [ms] (mean)
Time per request:       0.331 [ms] (mean, across all concurrent requests)
Transfer rate:          110869.67 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        1   68 221.7      1    7012
Processing:    46  257 178.7    185    4000
Waiting:        0   23  37.8      6    1923
Total:         77  325 288.8    217    7499

Percentage of the requests served within a certain time (ms)
  50%    217
  66%    296
  75%    379
  80%    428
  90%    623
  95%   1056
  98%   1250
  99%   1407
 100%   7499 (longest request)
root@hyman-dev:~# ab -n 100000 -c 3000 http://18.18.186.19:5000/
This is ApacheBench, Version 2.3 <$Revision: 1706008 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 18.18.186.19 (be patient)
Completed 10000 requests
Completed 20000 requests
Completed 30000 requests
Completed 40000 requests
Completed 50000 requests
Completed 60000 requests
Completed 70000 requests
Completed 80000 requests
Completed 90000 requests
Completed 100000 requests
Finished 100000 requests


Server Software:        
Server Hostname:        18.18.186.19
Server Port:            5000

Document Path:          /
Document Length:        0 bytes

Concurrency Level:      3000
Time taken for tests:   40.025 seconds
Complete requests:      100000
Failed requests:        100000
   (Connect: 0, Receive: 0, Length: 98016, Exceptions: 1984)
Total transferred:      3685107552 bytes
HTML transferred:       3661975776 bytes
Requests per second:    2498.45 [#/sec] (mean)
Time per request:       1200.747 [ms] (mean)
Time per request:       0.400 [ms] (mean, across all concurrent requests)
Transfer rate:          89912.50 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        1  254 649.4     44   31039
Processing:    27  693 635.2    532   23719
Waiting:        0   65 116.0     34    5097
Total:         84  947 915.3    684   31503

Percentage of the requests served within a certain time (ms)
  50%    684
  66%   1031
  75%   1265
  80%   1409
  90%   1888
  95%   2479
  98%   3481
  99%   4110
 100%  31503 (longest request)


```