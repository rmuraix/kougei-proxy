# kougei-config
![License:MIT License](https://img.shields.io/github/license/rmuraix/kougei-proxy)  
[![DeepSource](https://deepsource.io/gh/rmuraix/kougei-proxy.svg/?label=active+issues&show_trend=true&token=YoxuUkgu37sKwPgyJqUOECP9)](https://deepsource.io/gh/rmuraix/kougei-proxy/?ref=repository-badge)[![DeepSource](https://deepsource.io/gh/rmuraix/kougei-proxy.svg/?label=resolved+issues&show_trend=true&token=YoxuUkgu37sKwPgyJqUOECP9)](https://deepsource.io/gh/rmuraix/kougei-proxy/?ref=repository-badge)  

Script for [Tokyo polytechnic university](https://t-kougei.ac.jp/) students.  
東京工芸大学のkougei-wiFi.1xST下でGit、pipを使用できるようにします。
## Features
- Gitとpipのconfigの変更
- SSIDを見てオンオフを決定する
## Download/Usage
[こちら](https://github.com/rmuraix/kougei-proxy/releases)から最新のリリースをダウンロードしてください。
### Windows
`kougei-config_windows_x64.zip`をダウンロードして`kougei-config.exe`を実行してください。  
または`kougei-konfig.ps1`を実行してください。実行ポリシーの関係で実行できない場合はPowerShellを**管理者権限**で実行の上、以下のコマンドを入力してください。（コマンドの解説は[Qiita(by Targityen)](https://qiita.com/Targityen/items/3d2e0b5b0b7b04963750)や[Microsoft Docs](https://docs.microsoft.com/ja-jp/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.2)が参考になります。）  
```powershell
> Set-ExecutionPolicy Bypass
```
### Mac
`kougei-config_mac_x64.tgz`をダウンロードして`kougei-config.app`を実行してください。
### Linux
`kougei-config_linux_x64.tgz`をダウンロードして`kougei-config.bin`を実行してください。  
実行権限を与える必要があります。  
```shell
$ chmod u+x kougei-config.bin
```
## Develop
### Requirement
- Python 3.10.5以上
### Setup
#### 仮想環境の作成（共通）
```shell
$ cd [project directory]
$ python -m venv venv
```
#### 仮想環境の有効化  
Windows  
```powershell
> .\venv\Scripts\activate
```
Mac/Linux  
```shell
$ . venv/bin/activate
```
#### パッケージのインストール（共通）  
```shell
$ pip install -r requirements.txt
```
### Build
ここでは[Nuitka](https://github.com/Nuitka/Nuitka)を使用します。  
Windows/Linux
```shell
$ nuitka --follow-imports --onefile kougei-config.py
```  
Mac  
```shell
nuitka --follow-imports --onefile --macos-create-app-bundle kougei-config.py
```
## Contributing  
[CONTRIBUTING.md](/CONTRIBUTING.md)と[CODE_OF_CONDUCT.md](/CODE_OF_CONDUCT.md)をお読みください。   
## Auther/Contributer
Ryota Murai ([@rmuraix](https://github.com/rmuraix))  
## License
'rmuraix/kougei-proxy' is under [MIT License](/LICENSE).