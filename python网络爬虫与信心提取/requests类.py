'''
request类的属性或方法
    .url:Request对应的请求URL地址
    .method:对应的请求方法，'GET''POST'等
    .headers:字典类型风格的请求头
    .body:请求内容主体，字符串类型
    .meta:用户添加的拓展信息，在Scrapy内部模块间传递信息使用
    .copy:复制该请求

response类
    .url:Response对应的URL地址
    .status:HTTP状态码，默认是200
    .headers:Response对应的头部信息
    .body:Response对应的内容信息，字符串类型
    .flags:一组标记
    .request:产生Response类型对应的Request对象
    .copy:复制该响应
'''