# xiaohongshuSpider

scrapy环境安装及入门见  http://scrapy-chs.readthedocs.io/zh_CN/0.24/

scrapy shell http://m.xiaohongshu.com 在命令行模式下匹配所需各元素的xpath，方便后续爬取数据。 可参考 [在spider中启动shell来查看response](http://scrapy-chs.readthedocs.io/zh_CN/0.24/topics/shell.html#topics-shell-inspect-response)

首页顶部banner图：
response.xpath('//div[contains(@class, "banner")]//img/@src').extract()

文章封面图：
response.xpath('//div[contains(@class, "dual-column-layout")]//div[contains(@class, "note-item")]//div[contains(@class, "note-cover")]//img/@src').extract()     前缀需要处理

调整链接：
response.xpath('//div[contains(@class, "dual-column-layout")]//div[contains(@class, "note-item")]/a/@href').extract()  需要拼接前缀

标题：
response.xpath('//div[contains(@class, "dual-column-layout")]//div[contains(@class, "note-item")]//h3[contains(@class, "note-title")]/text()').extract()

简介：
response.xpath('//div[contains(@class, "dual-column-layout")]//div[contains(@class, "note-item")]//p[contains(@class, "note-desc")]/text()').extract()

作者：
response.xpath('//div[contains(@class, "dual-column-layout")]//div[contains(@class, "note-item")]//div[contains(@class, "note-author")]//a[contains(@class, "note-author-nickname")]/text()').extract()

头像：
response.xpath('//div[contains(@class, "dual-column-layout")]//div[contains(@class, "note-item")]//div[contains(@class, "note-author")]//img[contains(@class, "avatar-img")]/@src').extract()

点赞数：
response.xpath('//div[contains(@class, "dual-column-layout")]//div[contains(@class, "note-item")]//span[contains(@class, "note-likes")]//text()').extract()   前后有回车符号


爬虫代码写完后，执行 scrapy crawl xiaohongshu -o items_index.json 即可将结果保存到 json 文件内。
