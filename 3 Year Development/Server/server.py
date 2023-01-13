import sys
import socket
import struct
import time
import random
import hashlib

class Server:

    def __init__(self, address, port, max_packet_size=512):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((address, port))
        self.max_packet_size = max_packet_size
        self.blacklisted_clients = {}
        self.challenged_clients = {}
        self.known_clients = {}

    def run(self):
        while True:
            packet, sender = self.socket.recvfrom(self.max_packet_size)
            print(packet, sender)
            if sender in self.blacklisted_clients:
                continue
            if sender in self.challenged_clients:
                self.check_challenge(packet, sender)
                continue
            if sender in self.known_clients:
                # TODO process message
                continue
            
            # new client
            if len(packet) != 4:
                self.blacklist_client(sender)
                continue

            client_first_challenge, = struct.unpack('i', packet[0:4])

            if client_first_challenge < 0 or client_first_challenge > 99999:
                 self.blacklist_client(sender)
                 continue

            self.send_challenge(client_first_challenge, sender)

    def send_challenge(self, client_random_value, client_address):
        challenge_value = random.randrange(0, 99999)
        self.challenged_clients[client_address] = (client_random_value, challenge_value)
        packet = struct.pack('i', challenge_value)
        self.socket.sendto(packet, client_address)
        print('ready to challenge', client_address)

    def check_challenge(self, packet, sender):
        client_random_value, server_random_value = self.challenged_clients[sender]
        del(self.challenged_clients[sender])
        if len(packet) != 32:
            self.blacklist_client(sender)
            return
        client_plus_server_value = client_random_value + server_random_value
        hash = hashlib.sha256(struct.pack('i', client_plus_server_value)).digest()
        if hash != packet:
            self.blacklist_client(sender)
            return
        self.known_clients[sender] = True
        print('Welcome client', sender)

    def blacklist_client(self, client_address):
        print('blacklisted', client_address)
        self.blacklisted_clients[client_address] = time.time()

            

if __name__ == '__main__':
    server = Server(sys.argv[1], int(sys.argv[2]))
    server.run()