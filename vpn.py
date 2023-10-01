from config import *
from VPN.windscribe import Windscribe

windscribe = Windscribe(login,password)
while 1:
    windscribe.connect(rand=True)
    input("Connect to Next Country>>>: ")