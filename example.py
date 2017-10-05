#!/usr/bin/env python

import log4py.config
import logging
import time

log4py.config.fileConfig("example.properties")

while True:
  logging.debug("debug message")
  logging.info("info message")
  logging.warn("warn message")
  logging.error("error message")
  logging.fatal("fatal message")
  time.sleep(1)
