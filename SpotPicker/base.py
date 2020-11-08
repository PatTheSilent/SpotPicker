"""
Basic stuff that we want available accross all classes goes here.
"""


import logging


class Base:
    def __init__(self):
        self.logger = self.get_logger()

    @staticmethod
    def get_logger():
        return logging.getLogger()
