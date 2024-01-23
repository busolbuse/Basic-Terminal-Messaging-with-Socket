import socket
def client_program():
    host = '------'  # as both code is running on same pc
    port = 5018  # socket server port number
    #####   a different port number should be used for each connection ####

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # instantiate-take a case.
    client_socket.connect((host, port))  # connect to the server



    message = input(" -> ")  # take terminal input

    while message.lower().strip() != 'bye': #bye :(
        client_socket.send(message.encode())  # send message :)
        readata = client_socket.recv(1024).decode()  # receive response

        print('Received from anonymous: ' + readata)  # show in terminal

        message = input(" -> ")  # again take input

    client_socket.close()  # close the connection-leave the connection :)


if __name__ == '__main__':
    client_program()