import time
import os

from flask import Flask
app = Flask(__name__)

@app.route("/")
def get_dog() -> str:
    dog: str = ""
    dog += "\n"
    dog += "\n"
    dog += "\n"
    dog += "             hello\n"
    dog += "                            __\n"
    dog += "     ,                    ,\" e`--o\n"
    dog += "    ((                   (  | __,'\n"
    dog += "     \\~----------------' \_;/\n"
    dog += "     (                      /\n"
    dog += "     /) ._______________.  )\n"
    dog += "    (( (               (( (\n"
    dog += "     ``-'               ``-'\n"
    dog += "             bello\n"
    dog += "\n"
    dog += "\n"
    dog += "\n"
    return dog

def main():
    dog: str = get_dog()
    end: int = int(os.getenv('DOG_REPITITIONS', -1))
    index: int = 0
    while True:
        print(dog)
        
        if end > 0 and index >= end -1:
            return
        index += 1

        time.sleep(1)

if __name__ == "__main__":
    mode: str = os.getenv('DOG_MODE', 'SERVER')
    print('Start hello_bello as', mode)
    
    if mode == 'SERVER':
        app.run(host='0.0.0.0')
    else:
        main()
    