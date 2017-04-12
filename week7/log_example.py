import logging

FORMAT = '%(levelname)s: %(asctime)-15s %(clientip)s %(user)-8s %(message)s'
logging.basicConfig(format=FORMAT)
#logging.basicConfig(filename='example.log',level=logging.DEBUG, filemode='w')

d = {'clientip': '192.168.0.1', 'user': 'foobar'}
logger = logging.getLogger('tcpserver')
logger.warning('Protocol problem: %s', 'connection reset', extra=d)

#logging.debug('This message should go to the log file')
#logging.info('So should this')
#logging.warning('And this, too')
#
#logging.warning("Danger Will Robinson")
#logging.info("FYI")


