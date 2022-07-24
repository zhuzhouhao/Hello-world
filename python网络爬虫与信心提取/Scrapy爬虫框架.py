'''
5+2结构
一共七个结构，五个主体，两个中间件
五个主体：SPIDERS,ENGINE,DOWNLOADER,ITEM PIPELINES,SCHEDULER
两个中间件:SPIDERS和ENGINES中间，ENGINE和DOWNLOADER中间
三条主要数据流:
    1.  SPIDERS (REQUESTS) -> ENGINE -> SCHEDULER
    2.  SCHEDULER (REQUESTS) -> ENGINE (REQUESTS) -> DOWNLOADER (RESPONSE) -> ENGINE (RESPONSE) -> SPIDERS
    3.  SPIDERS (ITEMS/REQUESTS) -> ENGINE (ITEMS)    -> ITEM PIPELINES
                                           (REQUESTS) -> SCHEDULER
在ENGINE和DOWNLOADER中间有一个中间件Downloader Middleware
    目的：实施Engine,Scheduler和Downloader之间进行用户可配置的控制
    功能：修改，丢弃，新增请求或响应

Spider
    解析Downloader返回的响应(Response)
    产生爬取项(scraped item)
    产生额外的爬取请求(Request)

Item Pipelines
    以流水线方式处理Spider产生的爬取项
    有一组操作顺序组成，类似流水线，每个操作是一个Item Pipeline类型
    可能操作包括:清洗，检验和查重爬取项中的HTML数据，将数据存储到数据库

在SPIDERS和ENGINE中间有一个中间件Spider Middleware
    目的：对请求和爬取项的再处理
    功能：修改，丢弃，新增请求和爬取项

常用命令

    startproject创建一个新工程
    scrapy startproject <name>[dir]

    genspider创建一个爬虫
    scrapy genspider [options]<name><domain>

    settings获得爬虫配置信息
    scrapy settings [options]

    srawl运行一个爬虫
    scrapy crawl <spider>

    list列出工程中所有爬虫
    scrapy list

    shell启动URL调试命令行
    scrapy shell [url]

'''