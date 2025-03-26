## 使用 API

使用Web APIWeb API是网站的一部分，用于与使用非常具体的URL请求特定信息的程序交互。这种请求称为API调用。请求的数据将以易于处理的格式（如JSON或CSV）返回。依赖于外部数据源的大多数应用程序都依赖于API调用，如集成社交媒体网站的应用程序。

- GitHub的API让你能够通过API调用来请求各种信息
  - https://api.github.com/search/repositories?q=language:python&sort=stars

- 监视API的速率限制
  - 大多数API都存在速率限制，即你在特定时间内可执行的请求数存在限制。要获悉你是否接近了GitHub的限制，在浏览器中输入https://api.github.com/rate_limit 可以看到限制信息