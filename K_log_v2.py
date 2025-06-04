import sys
sys.path.append('C:/Users/Emre/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0/LocalCache/local-packages/Python312/site-packages')
from pynput import keyboard

current_word = ""

def on_press(key):
    global current_word
    try:
        if key.char:  # Normal bir harfse
            current_word += key.char  # Harfi biriktir
    except AttributeError:
        # Özel tuşlar (örneğin shift, ctrl) burada ele alınabilir
        pass

def on_release(key):
    global current_word
    if key == keyboard.Key.space:  # Boşluk tuşuna basıldığında
        print(f"Kelime: {current_word}")
        current_word = ""  # Yeni kelime için sıfırla

    if key == keyboard.Key.esc:  # Escape tuşuyla çıkış
        return False


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()