import subprocess
from subprocess import PIPE

def main():
    print("kougei-config 1.0")
    print("Copyright (C) Ryota Murai")
    print("repo: https://github.com/rmuraix/kougei-proxy\n")

    proc = subprocess.run("netsh wlan show interfaces", shell=True, stdout=PIPE, stderr=PIPE, text=True)
    datalist = proc.stdout.split('\n')
    for data in datalist :
        if data.find('    SSID') == 0:
            ssid = data[data.find(':')+2:len(data)]
            print('ssid = '+ssid)
        elif data.find('    BSSID') == 0:
            bssid = data[data.find(':')+2:len(data)]
            print('bssid = '+bssid)

    subprocess.call('PAUSE', shell=True)

    return

if __name__ == "__main__":
    main()