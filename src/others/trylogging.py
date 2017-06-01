# -*- coding: utf-8 -*-

import logging
import logging.config
from src.utils.config import DefaultConfig

# log_path = DefaultConfig().base_path + '\config\log.conf'
# print log_path
# logging.config.fileConfig(log_path)

# logging.basicConfig(level=logging.NOTSET)
log = logging.getLogger('s')
logging.root.setLevel(logging.NOTSET)

console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

log.addHandler(console)
print log.getEffectiveLevel()

# log.debug('debug message')
log.info('info message')
# log.error('error message')
# log.critical('critical message')

print log.handlers
print logging.root.handlers
