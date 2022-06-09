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

chcp $code | out-null

if ($SSIDNAME -eq "kougei-WiFi.1xST") {
    git config --global http.proxy proxy-a.t-kougei.ac.jp:8080
}else{
    git config --global --unset http.proxy
}

write-host "Press any key to continue..."
[void][System.Console]::ReadKey($true)