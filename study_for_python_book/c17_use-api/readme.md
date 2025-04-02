## 使用 API

使用Web APIWeb API是网站的一部分，用于与使用非常具体的URL请求特定信息的程序交互。这种请求称为API调用。请求的数据将以易于处理的格式（如JSON或CSV）返回。依赖于外部数据源的大多数应用程序都依赖于API调用，如集成社交媒体网站的应用程序。

- GitHub的API让你能够通过API调用来请求各种信息
  - https://api.github.com/search/repositories?q=language:python&sort=stars

- 监视API的速率限制
  - 大多数API都存在速率限制，即你在特定时间内可执行的请求数存在限制。要获悉你是否接近了GitHub的限制，在浏览器中输入https://api.github.com/rate_limit 可以看到限制信息


### 17.3 Hacker News API

Hacker News 网站，用户分析变成和技术方面的文章. 可以访问该网站的所有文章和评论信息，不需要通过注册获取密钥.

- 这个调用返回最热门文章信息: https://hacker-news.firebaseio.com/v0/item/9884165.json