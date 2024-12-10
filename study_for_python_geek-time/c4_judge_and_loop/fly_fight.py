# 飞机大战
# 要先安装 pynput 包: pip3 install pynput

from pynput.keyboard import Key, Listener, KeyCode

def onPress(key):
    if(key == KeyCode.from_char('w')):
        print("you press up key")
    elif(key == KeyCode.from_char('s')):
        print("you press down key")
    elif(key == KeyCode.from_char('a')):
        print("you press left key")
    elif(key == KeyCode.from_char('d')):
        print("you press right key")
                
    print()

with Listener(on_press=onPress) as listener:
    listener.join()                  