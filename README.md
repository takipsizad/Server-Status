# Server-Status
Discord bot which checks status of minecraft server and returns details

## There are 4 functions in total:
  
  1. Server Status  
     Checks if server is online or offline
      ```
      $status
      ```
  
  2. Latency  
     Checks the latency of the server
     ```
     $ping
     ```
  
  3. Player Amount  
     Gives the number of players currently online
     ```
     $players
     ```
  
  4. Player List  
     Gives the names of all the players online
     ```
     $player-names
     ```  
 


## Dependencies

1) [Python 3.7 & above](https://www.python.org/downloads/)
2) [pip3](https://pip.pypa.io/en/stable/installing/)
3) [mcstatus](https://github.com/Dinnerbone/mcstatus) Module (Python)
4) [Discord](https://pypi.org/project/discord.py/) Module (Python)
5) [Decouple](https://pypi.org/project/python-decouple/) Module (Python)  




## Setup

Create a new discord bot and invite it to your discord server  
If you are new to discord bots check this [tutorial](https://www.freecodecamp.org/news/create-a-discord-bot-with-python/) out

Linux

1)Clone the repository with 
         
```
git clone https://github.com/AwareSuperCC/Server-Status.git && cd Server-Status/
```

2)Give execution permission and Run setup.sh and input IP of server (or Domain Name) and Token from discord bot
```
sudo chmod +x setup.sh && ./setup.sh
```
    
3)Run main.py
```
python3 main.py
```
    
4)Add main.py to crontab to start script on startup (Optional)
        
```
sudo crontab -e
```
  copy and paste into file
       
```
@reboot PYTHONPATH=/usr/bin/python3 /usr/bin/python3 $HOME/serverstat.py &
```  
  
  
