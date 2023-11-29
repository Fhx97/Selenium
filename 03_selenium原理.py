# 首先启动WebDriver并绑定特定端口开启Web服务，当做Remote Server
# Client首次请求会创建一个Session，并向remote server发送HTTP请求启动浏览器，Remote Server解析请求
# 启动浏览器后，Client Cookie携带session id，再次给Remote Server发送HTTP请求，操作浏览器，定位页面元素等等
# 解析response，判断脚本是否继续还是结束
