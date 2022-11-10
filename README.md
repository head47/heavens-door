# Heaven's door v0.1
telegram bot to control your VPN connection
Can be used for Wireguard VPN to control users, their online time and their connection.
## Intalling

Install the sqlite:
  ```sudo apt install sqlite3```

Install database:
  ```./setup.py```

Add Telegram API Token to config file .bot_token
  ```echo -n "TOKEN" > .bot_token```

## Using
  ```sudo ./bot.py```

## Admin commands
  ```
  help - show all commands.
  show_users - show all users table. 
  block_user *** - block user if it's possible, check the status table. 
  unblock_user *** - unblock user if it's possible, check the status table. 
  check_connection - show connections of *all users* or by tg id. 
  add_new_user *name*:*ip*:*tg* - add new user in database. 
  remove_user *ip* - remove user from database by ip
  ```

## User commands
  ```
  help - show all commands.
  unblock - unblock user if it's possible.
  time - show your active time.
  status - show your status.
  ```
  
