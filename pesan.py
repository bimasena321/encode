import os
import time
import base64

os.system('clear')
nk = input("siapa ini ?")
time.sleep(2)
os.system('clear')
time.sleep(2)
print ("halo kak",nk)
time.sleep(2)
os.system('clear')


print ("""
      =====================================
      =   ___ _ __   ___ ___   __| | ___  =
      =  / _ \ '_ \ / __/ _ \ / _` |/ _ \ =
      = |  __/ | | | (_| (_) | (_| |  __/ =
      =  \___|_| |_|\___\___/ \__,_|\___| =
      =====================================
[+] github: Bimasena321
[+] youtube: ******
[+] discord: ******
\n""")
nma = input("input encode: ")
ef = base64.b64encode(nma.encode('utf-8'))
ed = str(ef, "utf-8")
print (ed)
