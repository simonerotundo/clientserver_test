###  SERVER  ###

import address_info
from socket import *

# memorizzo le informazioni del server
server_name, server_port = address_info.get_server_name(), address_info.get_server_port()

welcome_socket = socket()                       # inizializzo il socket
welcome_socket.bind((server_name, server_port)) # configuro il socket
welcome_socket.listen(5)                        # numero massimo di client collegati simultaneamente

while True:
    # resto in attesa di una connessione
    connection_socket, address = welcome_socket.accept()


    # memorizzo la frase inviata dal client ..
    client_sentence = connection_socket.makefile().readline()

    # .. la elaboro ..
    capitalized_sentence = client_sentence.upper()

    # .. e la mando al client
    connection_socket.makefile('w').writelines(capitalized_sentence + '\n')


    # chiudo la connessione
    connection_socket.close()
