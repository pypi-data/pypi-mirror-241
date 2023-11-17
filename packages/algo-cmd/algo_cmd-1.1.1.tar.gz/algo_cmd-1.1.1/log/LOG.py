import logging


class LOG:
    def __init__(self):
        self.logger = logging.getLogger("deploy cmd")
        self.logger.setLevel(logging.INFO)
        if not self.logger.handlers:
            self.console_handlr = logging.StreamHandler()
            self.console_handlr.setFormatter(
                logging.Formatter('%(asctime)s - %(name)s - %(filename)s - %(funcName)s  - %(message)s'))
            self.logger.addHandler(self.console_handlr)

    @staticmethod
    def L(*msg):
        LOG().logger.info(msg)

    @staticmethod
    def LS(msg):
        LOG().logger.info(msg)


if __name__ == '__main__':
    LOG.L("zzz", "232")
