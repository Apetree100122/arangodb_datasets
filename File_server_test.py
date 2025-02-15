import socket
import ssl

def secure_file_server(host, port, file_path):
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile="server.crt", keyfile="server.key")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
        sock.bind((host, port))
        sock.listen(5)
        print(f"Server listening on {host}:{port}")

        with context.wrap_socket(sock, server_side=True) as ssock:
            conn, addr = ssock.accept()
            print(f"Connection from {addr}")
            with open(file_path, 'rb') as f:
                data = f.read()
                conn.sendall(data)
            conn.close()

def secure_file_client(host, port, output_path):
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    context.load_verify_locations(cafile="server.crt")

    with socket.create_connection((host, port)) as sock:
        with context.wrap_socket(sock, server_hostname=host) as ssock:
            with open(output_path, 'wb') as f:
                while True:
                    data = ssock.recv(1024)
                    if not data:
                        break
                    f.write(data)

if __name__ == "__main__":
    # Example usage:
    # secure_file_server('localhost', 12345, 'file_to_send.txt')
    # secure_file_client('localhost', 12345, 'received_file.txt')
    pass
