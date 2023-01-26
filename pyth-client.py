
import socket

def main():
	host = '10.0.2.5'
	port =  6666

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	farenheit = input("Farenheit temp:")
	s.send(farenheit.encode('utf-8'))
	data  = s.recv(1024).decode('utf-8')
	print("Converted tp celcius:" + str(data))

	s.close()

if __name__ == '__main__':
    main()
