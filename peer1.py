import socket

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serv.bind(('localhost', 8080))
serv.listen()

while True:
    conn, addr = serv.accept()
    from_client = ''
    
    while True:
        data = conn.recv(4096)
        if not data: break
        from_client += str(data)
        print (from_client)
        conn.send(bytes('I am SERVER\n', 'utf-8'))
        
    conn.close()
    print ('client disconnected')