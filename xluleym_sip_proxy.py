

#    Copyright 2014 Philippe THIRION
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

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