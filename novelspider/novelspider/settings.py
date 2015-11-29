BOT_NAME = 'novelspider'

SPIDER_MODULES = ['novelspider.spiders']
NEWSPIDER_MODULE = 'novelspider.spiders'

ITEM_PIPELINES = ['novelspider.pipelines.NovelspiderPipeline']

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.54 Safari/536.5'
COOKIES_ENABLED = True

MONGODB_HOST = '127.0.0.1'
MONGODB_PORT = 27017
MONGODB_DBNAME = 'jikexueyuan'
MONGODB_DOCNAME = 'daomubiji2'