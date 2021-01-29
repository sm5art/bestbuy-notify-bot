# bestbuy-notify
A discord bot that tells you whenever bestbuy item (gtx 3060/3070/3080) comes in stock.

# Personal use
## Installation
1. Clone repo to server or AWS EC2 machine.
2. Install Docker on machine.
3. Setup bot with Discord Developers and retrieve bot token, also retrieve your user id from the discord client.
3. Rename bot.template.cfg to bot.cfg and replace token and user_id with your own values.
4. 
```
$ ./build_docker.sh
```

## Running
```
$ ./run_docker.sh
```
It will run the docker image in a new container detached
