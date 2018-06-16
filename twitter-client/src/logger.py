import logging
import socket

FORMAT = '%(asctime)-15s - {host} - %(message)s'.format(host=socket.gethostname())
logging.basicConfig(format=FORMAT)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
