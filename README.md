# bestbuy-notify
A discord bot that messages you whenever bestbuy item (gtx 3060/3070/3080) comes in stock.

# Personal deployment
## Installation
1. Clone repo to server or AWS EC2 machine.
```
$ git clone https://github.com/sm5art/bestbuy-notify-bot.git
```
2. Install Docker on machine.
3. Setup bot with Discord Developers and retrieve bot token, also retrieve your user id from the discord client.
4. Rename bot.template.cfg to bot.cfg and replace token and user_id with your own values.

## Building Docker image
```
$ ./build_docker.sh
```

## Running Docker image
```
$ ./run_docker.sh
```
It will run the docker image in a new container detached

# Developing
## Installation
1. Install virtualenv and python
2. 
```
$ virtualenv venv
$ . venv/bin/activate
$ pip install -r requirements.txt
```
3. Setup bot with Discord Developers and retrieve bot token, also retrieve your user id from the discord client.
3. Rename bot.template.cfg to bot.cfg and replace token and user_id with your own values.

## Running
```
$ python -m bbbot.bot
```

