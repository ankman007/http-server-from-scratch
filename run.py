import socket
from loguru import logger 

def start_server(SERVER_HOST = "0.0.0.0", SERVER_PORT = 8000):
    server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen()
    
    logger.info(f"Listening on {SERVER_HOST}:{SERVER_PORT}")

    while True:
        client_socket, client_address = server_socket.accept()
        
        client_ip, client_port = client_address
        logger.info(f"New connection from {client_ip}:{client_port}")    
        
        request = client_socket.recv(8192).decode()
        if not request:
            client_socket.close()
            continue
        
        parts = request.split("\r\n\r\n", 1)
        
        header_items = parts[0].split("\r\n")
        request_method, path, http_version = header_items[0].split(" ")    

        logger.info(f'{client_ip} - - "{request_method} {path} {http_version}"')
        
        if request_method == 'GET':
            if path == '/':
                with open('static/index.html', 'r') as file:
                    content = file.read()
                response = ('HTTP/1.1 200 OK\n\n' + content).encode()
                
            elif path == '/style.css':
                with open('static/style.css', 'r') as file:
                    content = file.read()
                response = ('HTTP/1.1 200 OK\n\n' + content).encode()
            
            elif path == '/favicon.ico':            
                with open('static/favicon.png', 'rb') as file:
                    content = file.read()
                response = 'HTTP/1.1 200 OK\n\n'.encode() + content
            
            else:
                logger.warning(f'{client_address[0]} - - 404 Not Found: {path}')
                response = ('HTTP/1.1 404 Not Found\r\n' + 'Not Found').encode()

        else: 
            logger.warning(f"Method Not Allowed: {request_method}")
            response = 'HTTP/1.1 405 Method Not Allowed\n\nAllow: GET'.encode()
        
        client_socket.sendall(response)
        client_socket.close()