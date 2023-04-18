from socket import * 
import sys 

serverSocket = socket(AF_INET, SOCK_STREAM)

serverPort = 6789

serverSocket.bind(("", serverPort))

serverSocket.listen(1)

while True:
	print('The server is ready to receive')

	
	connectionSocket, addr = serverSocket.accept() 

	try:
		
		
		print ("** Passou o ACCEPT **")

		message = connectionSocket.recv(8192)

		filename = message.split()[1]

		
		print ("** Arquivo: ", filename)
		if filename == "/favicon.ico": continue
		
		f = open(filename[1:])
		outputdata = f.read()

		connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode()) 
 
		for i in range(0, len(outputdata)):  
			connectionSocket.send(outputdata[i].encode())
		connectionSocket.send("\r\n".encode()) 
		
		
		print ("** Fecha Socket de conexão **")
		
		connectionSocket.close()

	except IOError:				
			print("** IO Error **")
					

			connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())
			serverSocket.close()  


serverSocket.close()  
sys.exit()