# Flask-Request-Logging
Flask Request Logging


## TODO
    1. 项目内可用自定义格式
    2. 支持`request_id`
    3. 添加配置项，同时兼容Flask配置项
    4. 文档输出
5. 制定规范
6. 中间件开发
7. 后续规划
8. 拉会收集需求
-----------------------
9. 测试用例
10. 为各个项目添加
11. 分享稿


## 如何使用
```
from flask import Flask
import flask_request_logging as log


app = Flask(__name__)
log.init_app(app)
```

## 支持变量
```
    REQUEST_LOGGING_OPEN = True
    REQUEST_LOGGING_HEADER_ID_NAME = 'track-id'
```