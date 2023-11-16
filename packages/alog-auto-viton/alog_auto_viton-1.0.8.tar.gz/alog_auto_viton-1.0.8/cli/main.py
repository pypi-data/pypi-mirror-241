from config.config import Config
from log.LOG import LOG


def main():
    LOG.L(Config().getconfig('spex_url', 'basic_login_url'))


if __name__ == '__main__':
    main()
