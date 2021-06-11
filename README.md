# Server-Status
Discord bot which checks status of minecraft server and returns details

##There are 4 functions in total:
  
  1. Server Status
     Checks if server is online or offline
     $status
  
  2. Latency
     Checks the latency of the server
     $ping
  
  3. Player Amount
     Gives the number of players currently online
     $players
  
  4. Player List
     Gives the names of all the players online
     $player-names
    
    
##Setup

Linux

1)Clone the repository with 
         ```
         git clone ''
         ```

2)Run setup.py and input necessary fields
    
3)Run main.py
    
4)Add main.py to crontab to start script on startup (Optional)
        ```
        sudo crontab -e
        ```
        copy and paste into file
       
        ```
        @reboot sleep 5m && PYTHONPATH=/usr/bin/python3 /usr/bin/python3 $HOME/serverstat.py &
        ```
