import configparser
import os.path

from log.LOG import LOG


class Config:
    def __init__(self):
        """Constructor"""
        self.cf = configparser.RawConfigParser()
        self.execdir = os.getcwd()
        self.confdir = os.path.abspath(os.path.join(self.execdir, '.'))
        self.cf.read(self.confdir + '/config.ini')  # 读取配置文件，如果写文件的绝对路径，就可以不用os模块

    def getconfig(self, section, key):
        try:
            if not section or not key:
                raise Exception('参数不对')
            return self.cf.get(section, key)
        except configparser.NoSectionError as e:
            LOG.L(e.message)
        except configparser.NoOptionError as e:
            LOG.L(e.message)

    @staticmethod
    def get_section(section):
        try:
            if not section:
                raise Exception('参数不对')
            return Config().cf.options(section)
        except configparser.NoSectionError as e:
            LOG.L(e.message)
        except configparser.NoOptionError as e:
            LOG.L(e.message)


if __name__ == '__main__':
    print(Config().get_section('spex_url'))
