import logging as log

'''
DOC:
    # asctime: agrega el tiempo (fecha y hora)
    # levelname: nivel del mensaje (DEBUG, INFO, ETC)
    # filename: nombre del archivo que envía el mensaje
    # lineno: agrega el número de línea al mensaje del log
    # message: muestra el mensaje que hemos agregado al log
    # StreamHandler: envía info a la consola
'''

log.basicConfig(level=log.DEBUG,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('logger.log'),
                    log.StreamHandler()
                ])

if __name__ == '__main__':
    log.debug('Mensaje a nivel debug')
    log.info('Mensaje a nivel info')
    log.warning('Mensaje a nivel de warning')
    log.error('Mensaje a nivel de error')
    log.critical('Mensaje a nivel critico')