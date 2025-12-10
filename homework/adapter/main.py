import sys
sys.path.append('')
from adapter import *

def run_aplication_code(logger: LoggerInterface):
    logger.log('This is info', 'INFO')
    logger.log('This is warning', 'WARNING')
    logger.log('This is error', 'ERROR')


if __name__ == '__main__':
    print('file logger adapter test')
    ofl = OldFileLogger()
    fla = FileLoggerAdapter(ofl)
    run_aplication_code(fla)
    print()
    
    print('console adapter test')
    con_print = ConsolePrinter()
    con_adapter = ConsoleAdapter(con_print)
    run_aplication_code(con_adapter)
    
