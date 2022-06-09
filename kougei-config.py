import subprocess
from subprocess import PIPE

def main():
    # kougei-config 1.0
    # Copyright (C) Ryota Murai
    # repo: https://github.com/rmuraix/kougei-proxy

    proc = subprocess.run('netsh wlan show interfaces', shell=True, stdout=PIPE, stderr=PIPE, text=True)
    datalist = proc.stdout.split('\n')
    for data in datalist :
        if data.find('    SSID') == 0:
            ssid = data[data.find(':')+2:len(data)]

    proxy = 'proxy-a.t-kougei.ac.jp:8080'

    if ssid == 'kougei-WiFi.1xST':
        subprocess.run('git config --global http.proxy {}'.format(proxy), shell=True, stdout=PIPE, stderr=PIPE)
    else:
        subprocess.run('git config --global --unset http.proxy', shell=True, stdout=PIPE, stderr=PIPE)

    subprocess.call('PAUSE', shell=True)

    return

if __name__ == '__main__':
    main()