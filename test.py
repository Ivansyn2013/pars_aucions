from config.config import DeployConfig
import logging
from logs import my_loger

ls1  = [1,2,3]
ls2 = ['a','b','d']

print(dict(zip(ls1, ls2)))

print(DeployConfig.TESTING)
print('secret key',DeployConfig.SECRET_KEY)


my_loger.debug('DEBUG')
my_loger.info('INFO')
my_loger.error('ERROR')
my_loger.critical('Critical')
my_loger.warning('WARNING')