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
    

Dependencies
1) [mcstatus](https://github.com/Dinnerbone/mcstatus) Module (Python)
2) [Discord](https://pypi.org/project/discord.py/) Module (Python)


## Setup

Linux

1)Clone the repository with 
         
```
git clone https://github.com/AwareSuperCC/Server-Status.git
```

2)Run setup.py and input Token from discord bot and IP of server (or Domain Name)
    
3)Run main.py
    
4)Add main.py to crontab to start script on startup (Optional)
        
```
sudo crontab -e
```
  copy and paste into file
       
```
@reboot PYTHONPATH=/usr/bin/python3 /usr/bin/python3 $HOME/serverstat.py &
```
