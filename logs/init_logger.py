import logging
import sys

my_loger = logging.getLogger('my_loger')
#my_loger.setLevel(logging.DEBUG)

my_handler = logging.StreamHandler()
my_formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")

my_handler.setLevel(logging.DEBUG)
my_handler.setFormatter(my_formatter)
my_loger.addHandler(my_handler)

__all__ = [
    'my_loger'
]

