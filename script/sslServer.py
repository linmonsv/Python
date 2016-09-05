import socket, ssl
import time

cacrtf="cacert.pem"
crtf="cacert.pem"
keyf="cakey.pem"

server_sc = socket.socket()
server_sc.bind(('', 10023))
server_sc.listen(5)

newsocket, addr = server_sc.accept()
sc = ssl.wrap_socket(newsocket,
                     server_side=True,
                     certfile=crtf,
                     keyfile=keyf,
                     ca_certs=cacrtf)

data = sc.read()
print data
sc.write('Back time: ' + str(time.time()))

sc.close()
server_sc.close()