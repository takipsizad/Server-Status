#! /bin/bash

pip3 install discord.py
pip3 install mcstatus
pip3 install python-decouple
echo "Enter server Address"
read address
echo "ADDRESS=${address}" > .env
echo "Enter Discord Bot TOKEN"
read TOKEN
echo "TOKEN=${TOKEN}" >> .env
echo "DONE!"
