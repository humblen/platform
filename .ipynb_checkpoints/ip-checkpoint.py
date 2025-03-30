import netifaces as ni
ni.interfaces()
ni.ifaddresses('eth0')
