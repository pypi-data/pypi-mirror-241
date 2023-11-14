#!/usr/bin/env python3

from srx_classes import cli_loop
from srx_classes.logger_config import setup_logging
import logging

# Call the setup_logging function from logger_config
setup_logging()

module_name = __name__.split('.')[0]


def main():

    logging.debug(f' {module_name} This is a debug message in some_module')
    logging.info(f' {module_name} This is an info message in some_module')


    cli_loop.main_cli_loop()
    

    

if __name__ == "__main__":
    main()

