# default
![License:MIT License](https://img.shields.io/github/license/rmuraix/kougei-proxy)
![issues](https://img.shields.io/github/issues/rmuraix/kougei-proxy)  
Script for [Tokyo polytechnic university](https://t-kougei.ac.jp/) students.  
東京工芸大学のkougei-wiFi.1xST下でGitなどを使用できるようにします。
## Features
- Gitのconfigの変更
- SSIDを見てオンオフを決定する
## Download/Usage
[こちら](https://github.com/rmuraix/kougei-proxy/releases)から最新のリリースをダウンロードしてください。
### スクリプトファイルを使う
#### Windows
`kougei-proxy-config.ps1`を実行します。  

実行時、`このシステムではスクリプトの実行が無効になっているため～`などと表示される場合には実行ポリシーによって実行がブロックされています。実行するには設定を変更する必要があります。  
PowerShellを*管理者権限*で起動し、以下のコマンドを実行します。
```shell
Set-ExecutionPolicy Unrestricted
```  
`Unrestricted`の部分は[こちら](https://docs.microsoft.com/ja-jp/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.2#powershell-execution-policies)を参考に変更できます。（UnrestrictedまたはBypassが必要です。）
### 実行ファイルを使う
#### Windows
Windowsで実行ポリシーを変更したくない方におすすめです。  
`kougei-proxy-config.exe`を実行します。 
#### Mac
ソースコードからビルドする必要があります。[Develop](#develop)を参考にビルドしてください。
## Develop
### Requirement
- Python 3.10.4以上
### Setup
仮想環境の作成（共通）
```shell
$ cd [project directory]
$ python3 -m venv venv
```
仮想環境の有効化  
Windows  
```shell
$ .\venv\Scripts\activate
```
Mac/Linux  
```shell
$ . venv/bin/activate
```
パッケージのインストール(共通)
```shell
pip install requirements.txt
```
### Build
ここでは[Nuitka](https://github.com/Nuitka/Nuitka)を使用します。
```shell
nuitka --follow-imports --onefile kougei-proxy-config.py
```
## Contributing  
[CONTRIBUTING.md](/CONTRIBUTING.md)と[CODE_OF_CONDUCT.md](/CODE_OF_CONDUCT.md)をお読みください。   
## Auther
Ryota Murai ([@rmuraix](https://github.com/rmuraix))  
## License
'rmuraix/kougei-proxy' is under [MIT License](/LICENSE).