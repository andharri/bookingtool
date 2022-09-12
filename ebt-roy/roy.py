import logging

logging.basicConfig(
	format='%(asctime)s.%(msecs)03d %(levelname)-8s %(message)s',
	level=logging.INFO,
	datefmt='%d-%m-%Y %H:%M:%S')
log = logging.getLogger("logger")

log.info("ROY")