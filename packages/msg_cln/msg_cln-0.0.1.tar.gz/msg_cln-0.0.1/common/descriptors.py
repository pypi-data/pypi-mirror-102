import logging

SRV_LOGGER = logging.getLogger('server')


class PortValue():
    def __set__(self, instance, value):
        if value < 1024 or value > 65535:
            SRV_LOGGER.debug(f'incorrect port {value}. will use the default port 7777')
            # print(f'incorrect port {value}. will use the default port 7777')
            # exit(1)
            value = 7777
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class AddrValue():
    def __set__(self, instance, value):
        octets = value.split('.')
        if len(octets) != 4 or not octets[0].isdigit() or not octets[1].isdigit() \
                or not octets[2].isdigit() or not octets[3].isdigit():
            SRV_LOGGER.debug(f'{value} is not IpV4 address')
            exit(1)
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name
