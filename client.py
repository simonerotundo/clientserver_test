###  CLIENT  ###

import address_info
from socket import *

# memorizzo le informazioni del server
server_name, server_port = address_info.get_server_name(), address_info.get_server_port()

# AF_INET -> la rete sottostante è di tipo IPv4.
# SOCK_STREAM -> il socket è di tipo UDP
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_name, server_port))

# acquisisco una frase in input ..
sentence = input('frase in input: ')

# .. e la invio al server
client_socket.makefile('w').writelines(sentence + '\n')

# memorizzo la risposta del server
modified_sentence = client_socket.makefile().readline()

# stampo la risposta
print('frase in output: ', modified_sentence)

# termino la comunicazione
client_socket.close()
