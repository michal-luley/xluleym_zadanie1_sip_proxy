
import SocketServer
import socket
import sipfullproxy


# xluleym@stuba.sk

HOST, PORT = '0.0.0.0', 5060

if __name__ == "__main__":
    # vytvorenie objektu kniznice
    kniznica = sipfullproxy

    # zistenie mena a ip adresy
    hostname = socket.gethostname()
    ipaddress = socket.gethostbyname(hostname)

    # nastavenie premennych servera
    kniznica.recordroute = "Record-Route: <sip:%s:%d;lr>" % (ipaddress, PORT)
    kniznica.topvia = "Via: SIP/2.0/UDP %s:%d" % (ipaddress, PORT)
    server = SocketServer.UDPServer((HOST, PORT), kniznica.UDPHandler)

    # spustenie servera
    server.serve_forever()