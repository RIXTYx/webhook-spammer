import os, time, requests, pyfiglet, threading
os.system('clear')

print(" ")
print("\033[1;34;48m          ⣼⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣶⣦\33[0m")
print("\033[1;34;48m        ⣵⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶\33[0m")
print("\033[1;34;48m       ⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧\33[0m")
print("\033[1;34;48m       ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\33[0m")
print("\033[1;34;48m       ⣿⣿⣿⣿⣿⣿⣿⣿⠛⠩⡐⢄⠢⠙⢋⠍⣉⠛⡙⡀⢆⡈⠍⠛⣿⣿⣿⣿⣿⣿⣿⣿\33[0m")
print("\033[1;34;48m       ⣿⣿⣿⣿⣿⣿⣿⠃⠌⡡⠐⢂⠡⠉⡄⠊⢄⢂⠡⠐⠂⢌⠘⡰⠘⣿⣿⣿⣿⣿⣿⣿\33[0m")
print("\033[1;34;48m       ⣿⣿⣿⣿⣿⣿⠃⠌⠒⢠⠑⡨⠄⠃⠤⠉⢄⠢⠌⢡⠉⢄⢂⠡⠒⠸⣿⣿⣿⣿⣿⣿\33[0m")
print("\033[1;34;48m       ⣿⣿⣿⣿⣿⡏⠤⢉⠰⢁⢢⣶⣾⣧⢂⠩⡀⠆⣼⣶⣮⣄⠂⡂⠍⣂⢹⣿⣿⣿⣿⣿\33[0m")
print("\033[1;34;48m       ⣿⣿⣿⣿⣿⠁⢆⠨⢐⠂⣿⣿⣿⣿⠇⢂⠱⢸⣿⣿⣿⡿⢀⠂⠅⢢⠘⣿⣿⣿⣿⣿\33[0m")
print("\033[1;34;48m       ⣿⣿⣿⣿⣿⠌⢠⠂⢡⠊⠌⠛⠟⡋⢌⠂⢅⢂⡙⠿⠛⣁⢂⠉⡄⠃⡌⣿⣿⣿⣿⣿\33[0m")
print("\033[1;34;48m       ⣿⣿⣿⣿⣿⡨⠄⡘⠄⠎⣔⣉⡐⠌⡐⣈⠂⠆⡐⢂⣡⣤⢂⠡⡐⢡⢐⣿⣿⣿⣿⣿\33[0m")
print("\033[1;34;48m       ⣿⣿⣿⣿⣿⡨⠄⡘⠄⠎⣔⣉⡐⠌⡐⣈⠂⠆⡐⢂⣡⣤⢂⠡⡐⢡⢐⣿⣿⣿⣿⣿\33[0m")
print("\033[1;34;48m       ⣿⣿⣿⣿⣿⣿⣶⣥⣘⡐⠨⣽⣿⣿⣷⣶⣾⣾⣿⣿⣯⢁⠢⣐⣤⣷⣿⣿⣿⣿⣿⣿\33[0m")
print("\033[1;34;48m       ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\33[0m")
print("\033[1;34;48m       ⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏\33[0m")
print("\033[1;34;48m        ⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿\33[0m")
print("\033[1;34;48m         ⠛⠿⢿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⢿⠿⠟⠋\33[0m")
print(" ")

figlet_txt= pyfiglet.figlet_format("WEBHOOK SPAMMER")
print("\033[1;34;48m" + figlet_txt + "\33[0m")
print("\033[1;34;48mBY\33[0m \033[1;35;48mRIXTY ✓\33[0m")
print(" ")
print(" ")

print("\033[1;34;48m|====================|\33[0m")
msg = input("\033[1;34;48m[+] Spam Message => \33[0m")
webhook = input("\033[1;34;48m[+] WebHook Url => \33[0m")
th = int(input('\033[1;34;48m[+] Threads => \33[0m'))
sleep = int(input("\033[1;34;48m[+] Delay in seconds => \33[0m"))
print("\033[1;34;48m|====================|\33[0m")
print(" ")

print("\033[1;35;48m[v] RESULTS [v]\33[0m")
def spam():
    while True:
        try:
            data = requests.post(webhook, json={'content': msg})
            if data.status_code == 204:
                print(f"\33[92m[✓] Sent message\33[0m")
        except:
            print("\033[31m[✘] Invalid Webhook\33[0m")
        time.sleep(sleep)

for x in range(th):
    t = threading.Thread(target = spam)
    t.start()
