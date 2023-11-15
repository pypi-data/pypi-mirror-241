from config.config import Config
from log.LOG import LOG

if __name__ == '__main__':
    print("begin")
    LOG.L(Config().getconfig('spex_url', 'basic_login_url'))
