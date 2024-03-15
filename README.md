# JD自动评价

> 支持评价晒单（带两张图），追评，服务评价，支持AI生成评价内容

浏览器登录抓取CK（PC端CK）www的那个地址抓CK，登录后F12点到network，不要用命令document.cookie抓，会不完整，找带cookie的请求复制（其实只复制thor=xxx这串就行）


### 运行

+ 将获取到的cookie复制到cookie.txt (多账号用换行隔开)

+ `spark_config.json` 为讯飞模型ai评价参数 请根据需求更改

> 讯飞模型参数获取地址 [https://console.xfyun.cn/services/bm3](https://console.xfyun.cn/services/bm3)

| key | Value | 说明 |
|-----|-----|-----|
| on | false | 是否开启AI评价默认`false` |
| appid | fdxx9a | APPID |
| api_key | 705xxxxxeef1a | APIKey |
| api_secret | NDRkZTdxxxxxRkNmE0N2Fm | APISecret |
| Spark_url | wss://spark-api.xf-yun.com/v3.1/chat |  |
| domain | generalv3 |  |


+ 运行

```shell
pip install -r requirements.txt

python main.py

```




### 感谢

> 本脚本修改自 [6dylan6/auto_comment](https://github.com/6dylan6/auto_comment)




