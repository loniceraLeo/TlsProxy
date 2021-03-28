# TlsProxys

基于TLS协议的http流量代理

***

## 安装

※ **需要python3.7+**

```console
linux: python3.9 -m pip install TlsProxys
windows: pip install TlsProxys
```

## 基本用法

服务器端:

$ tpserver [command] [filename1[, filename2]]

客户端:

$ tpclient [command] [filename1[, filename2]]

### 命令行参数含义

+ -c : 手动指定配置文件
+ -g : 生成私钥-证书
+ -r : 递归文件搜索
+ -v : 版本信息
+ -h : 帮助信息

举例:

读取config.json作为配置文件:

```console
tpclient -c config.json
```

生成 app.key app.crt 私钥-证书对:

```console
tpclient -g app.key app.crt
```

在本目录下递归查找config.json:

```console
tpclient -r config.json
```

### 无参数调用

若不带参数地调用`tpclient/tpserver`且当前目录下不存在`config.json`, TlsProxys会交互式地读取用户的输入并在本目录下生成一个`config.json`文件。

注意:**客户端和服务器的配置文件略有不同**

## 一般用法

本条目将给出一个比较完整的提示，一般用户可以参考本流程使用TlsProxys。

在本节所有示例中，tpclient运行在本地 ; tpserver运行在服务器端。

### 准备工作

首先，用户需要确保机器上安装有openssl库。可用如下命令测试:

```console
openssl version
```

若打印版本信息，则openssl已经安装。

TlsProxys使用Tls协议传输数据, 服务器上需要私钥-证书对, 首先在本地生成一个私钥，并用它生成自签名证书:

```console
tpclient -g app.key app.crt
```

TlsProxys会自动调用openssl, 按照提示输入信息。如果调用成功，本目录下会生成
`app.key`, `app.crt`两个文件。

在本地，把`app.crt`导入浏览器根证书列表;把`app.key`和`app.crt`传输到远程服务器。

### 启动服务

在服务器上, cd到`app.key`和`app.crt`的目录下, 执行:

```console
tpserver
```

这会启动一个交互式的读取器, 输入示例如下:

server: 255.255.255.255  
port: 8000  
password: my_password  
certificate: app.crt  
private-key: app.key  

若解释器没有抛出异常, 命令行应该打印:  
255.255.255.255:8000 is serving

在本地, 执行:

```console
tpclient
```

在交互式读取器内输入:

server: 255.255.255.255  
port: 8000  
password: my_password  
local_port: 8080  

若解释器没有抛出异常, 命令行应该打印:  
127.0.0.1:8080 is serving

最后修改浏览器代理配置:
地址: 127.0.0.1  
端口: 8080

Done.

## LICENSE

GPLv3
