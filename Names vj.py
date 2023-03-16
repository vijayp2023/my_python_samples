
# host name
import platform
print(platform.node())


# ip address
import socket
print(socket.gethostbyname(socket.gethostname()))

# Computer name
import os
print(os.environ["COMPUTERNAME"])