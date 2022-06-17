$code=(chcp).split(":")[1].trim()
chcp 65001 | out-null

$STATE=8
$SSID=9

$result=netsh wlan show interfaces

if ( $result[$STATE].split(":")[1].trim() -eq "connected"){
    $SSIDNAME=$result[$SSID].split(":")[1].trim()
}else{
    $SSIDNAME=$null
}
pip | Out-File -FilePath ./configtemp.txt -Encoding utf8

chcp $code | out-null

$pipfind=Select-String -Path ./configtemp.txt -Pattern Usage

Remove-Item -Recurse ./configtemp.txt

if ($SSIDNAME -eq "kougei-WiFi.1xST") {
    git config --global http.proxy proxy-a.t-kougei.ac.jp:8080
    if ($pipfind -like "*configtemp.txt*") {
        pip config set global.proxy proxy-a.t-kougei.ac.jp:8080
    }
}else{
    git config --global --unset http.proxy
    pip config unset global.proxy
}