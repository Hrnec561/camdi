import exifread # type: ignore
import subprocess
import os
from colorama import Fore
import requests
import sys

prefix = f"{Fore.YELLOW}[CD]{Fore.RESET}"
version = f"v 1.2"
dev = False

def updater():
    os.system("title " + f"CamDi {version}")
    try:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        print(f'''{Fore.YELLOW}
   ____                ____  _   
  / ___|__ _ _ __ ___ |  _ \(_)
 | |   / _` | '_ ` _ \| | | | |
 | |__| (_| | | | | | | |_| | |
  \____\__,_|_| |_| |_|____/|_|{Fore.RESET}
             {version}
    ''')
        try:
            os.mkdir("temp")
        except FileExistsError:
            pass
        f = open("temp/info.txt", "w")
        f.close()
        link = 'https://raw.githubusercontent.com/Hrnec561/camdi/main/version.txt'
        file_name = "temp/version.txt"
        with open(file_name, "wb") as f:
            response = requests.get(link, stream=True)
            f.write(response.content)
        f = open("temp/version.txt", "r")
        content = f.read()
        content = content.replace("\n", "")
        f.close()
        if version == f"v {content}":
            pass
        else:
            content = f"v {content}"
            update(content)
        os.remove("temp/version.txt")
        if os.path.exists("temp/exiftool.exe") == True:
            pass
        else:
            print(f"{prefix} Downloading update...")
            link = "https://drive.usercontent.google.com/download?id=1wZ4jKqusrhbUwdbc8QJ5DxX0cL-ETcvW&export=download&authuser=0&confirm=t&uuid=7ff399ee-572a-495c-80b2-52dcdb988dcd&at=APZUnTWeKYzrEpbJyAkDhtPRcXr8%3A1713628369891"
            file_name = "temp/exiftool.exe"
            with open(file_name, "wb") as f:
                response = requests.get(link, stream=True)
                total_length = response.headers.get('content-length')

                if total_length is None:
                    f.write(response.content)
                else:
                    dl = 0
                    total_length = int(total_length)
                    for data in response.iter_content(chunk_size=4096):
                        dl += len(data)
                        f.write(data)
                        done = int(20 * dl / total_length)
                        sys.stdout.write(f"\r{prefix} [%s%s]" % (f'{Fore.YELLOW}={Fore.RESET}' * done, '=' * (20-done)) )
                        sys.stdout.flush()
            input("\n" + f"{prefix} Update sucessfull press any key to continue...")
        menu()
    except KeyboardInterrupt:
        exit()

def update(content):
    version = content
    try:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        print(f'''{Fore.YELLOW}
   ____                ____  _   
  / ___|__ _ _ __ ___ |  _ \(_)
 | |   / _` | '_ ` _ \| | | | |
 | |__| (_| | | | | | | |_| | |
  \____\__,_|_| |_| |_|____/|_|{Fore.RESET}
          {version} Update
    ''')
        print(f"{prefix} Downloading update...")
        if dev == True:
            menu()
        else:
            if ".py" in __file__:
                link = "https://raw.githubusercontent.com/Hrnec561/camdi/main/camdi.py"
            else:
                link = "https://raw.githubusercontent.com/Hrnec561/camdi/main/camdi.exe"
            file_name = "main.py"
            with open(__file__, "wb") as f:
                response = requests.get(link, stream=True)
                total_length = response.headers.get('content-length')

                if total_length is None:
                    f.write(response.content)
                else:
                    dl = 0
                    total_length = int(total_length)
                    for data in response.iter_content(chunk_size=4096):
                        dl += len(data)
                        f.write(data)
                        done = int(20 * dl / total_length)
                        sys.stdout.write(f"\r{prefix} [%s%s]" % (f'{Fore.YELLOW}={Fore.RESET}' * done, '=' * (20-done)) )
                        sys.stdout.flush()
            print("\n" + f"{prefix} Restart required")
            input("\n" + f"{prefix} Update sucessfull press any key to continue...")
            exit()
    except KeyboardInterrupt:
        exit()

def menu():
    try:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        print(f'''{Fore.YELLOW}
   ____                ____  _   
  / ___|__ _ _ __ ___ |  _ \(_)
 | |   / _` | '_ ` _ \| | | | |
 | |__| (_| | | | | | | |_| | |
  \____\__,_|_| |_| |_|____/|_|{Fore.RESET}
             {version}
        
{Fore.YELLOW}[1]{Fore.RESET}      Info from raw
{Fore.YELLOW}[2]{Fore.RESET}         Credits
{Fore.YELLOW}[3]{Fore.RESET}      Ctrl+C for Exit
    ''')
        moznost = input(f"{prefix} Choose option : ")
        print(moznost)
        if moznost == "1":
            start()
        elif moznost == "2":
            credits()
        elif moznost == "3":
            exit()
        else:
            menu()
    except KeyboardInterrupt:
        exit()
def start():
    try:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        print(f'''{Fore.YELLOW}
   ____                ____  _   
  / ___|__ _ _ __ ___ |  _ \(_)
 | |   / _` | '_ ` _ \| | | | |
 | |__| (_| | | | | | | |_| | |
  \____\__,_|_| |_| |_|____/|_|{Fore.RESET}
             {version}
    ''')
        cesta = input(f"{prefix} {'Specify path to RAW image':<25} : ")
        print("")
        cesta_check = cesta.replace("'", "")
        cesta_check = cesta_check.replace('"', '')
        cesta = r'{}'.format(cesta)
        try:
            open(cesta_check, "r")
        except FileNotFoundError:
            print(f"{prefix} {'Error':<25} : File Not Found")
            input(f"{prefix} {'Press any key to continue':<25} : ")
            start()
        main(cesta)
    except KeyboardInterrupt:
        exit()

def credits():
    try:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        print(f'''{Fore.YELLOW}
   ____                ____  _   
  / ___|__ _ _ __ ___ |  _ \(_)
 | |   / _` | '_ ` _ \| | | | |
 | |__| (_| | | | | | | |_| | |
  \____\__,_|_| |_| |_|____/|_|{Fore.RESET}
             {version}

{Fore.YELLOW}[1]{Fore.RESET} Hrnec561 - https://github.com/hrnec561
{Fore.YELLOW}[2]{Fore.RESET}    ExifTool - https://exiftool.org/ 
    ''')
        input(f"{prefix} {'Press any key to continue':<25} : ")
        menu()
    except KeyboardInterrupt:
        exit()

def main(cesta):
    try:
        file_path = cesta
        f = open("temp/info.txt", "w")
        subprocess.call(f'temp/exiftool.exe {file_path}', stderr=subprocess.STDOUT, stdout=f)
        f.close()
        with open("temp/info.txt", "r") as f_info:
            brand = []
            model = []
            shutter_count = []
            used_lens = []
            content = f_info.readlines()
            for i in content:
                if "Error  " in i:
                    i = i.replace("Error                           : ", "")
                    i = i.rstrip()
                    print(f"{prefix} {'Error':<25} : {i}")
                    input(f"{prefix} {'Press any key to continue':<25} : ")
                    start()
                else:
                    for i in content:
                        if "Make  " in i:
                            i = i.replace("Make                            : ", "")
                            brand.append(i)
                        elif "Camera Model Name  " in i:
                            i = i.replace("Camera Model Name               : ", "")
                            model.append(i)
                        elif "Shutter Count  " in i:
                            i = i.replace("Shutter Count                   : ", "")
                            shutter_count.append(i)
                        elif "Lens ID   " in i:
                            i = i.replace("Lens ID                         : ", "")
                            used_lens.append(i)
                        else:
                            pass
        #   print(content)
            print(f"{prefix} Specifications")
            print("")
            try:
                brand = brand[0].rstrip()
            except IndexError:
                brand = "No Data"
            print(f"{Fore.YELLOW}{'Camera brand':<25}{Fore.RESET} : {brand}")
            try:
                model = model[0].rstrip()
            except IndexError:
                model = "No Data"
            print(f"{Fore.YELLOW}{'Camera model':<25}{Fore.RESET} : {model}")
            try:
                shutter_count = shutter_count[0].rstrip()
            except IndexError:
                shutter_count = "No Data"
            print(f"{Fore.YELLOW}{'Shutter count':<25}{Fore.RESET} : {shutter_count}")
            try:
                used_lens = used_lens[0].rstrip()
            except IndexError:
                used_lens = "No Data"
            print(f"{Fore.YELLOW}{'Lens ID':<25}{Fore.RESET} : {used_lens}")
        try:
            os.remove("temp/info.txt")
        except FileNotFoundError:
            pass
        input("\n" + f"{prefix} {'Press any key to continue':<15} : ")
        start()
    except KeyboardInterrupt:
        exit()

updater()