# Nerd-Dad-Jokes

[![Build Status](https://travis-ci.com/sumitmukhija/Nerd-Dad-Jokes.svg?token=RqyE2wrDxJzawRVg3Bzd&branch=master)](https://travis-ci.com/sumitmukhija/Nerd-Dad-Jokes)

Nerd-Dad-Jokes is a Flask based REST API server and a Twitter Bot.

![Image description](ndf/static/images/icon.png)

| API endpoint | resource |
| ------ | ------ |
| / | random joke from the stored static file |
| /about | about the project |

# Installation
- Clone the repo
    ```sh
        git clone https://github.com/sumitmukhija/Nerd-Dad-Jokes.git
    ```
- Install dependencies  
    ```sh
    pip install -r requirements.txt
    ```
- Populate `config/production_settings.py` with your Twitter account values. Use keys from `config/settings.py`
- Execute flask app.

    ```ssh
    export FLASK_APP=nfg/app.py
    flask run
    ```
- Browse `localhost:5000/` to get a random bad dad joke.

# Twitter Bot 

[Nerd Dad Jokes](https://twitter.com/NerdDadJokes)

| Action | isActive |
| ------ | ------ |
| Tweet | ✓ |
| Retweet | ✓ |

### Todos

 - Write Tests
 - Add Tweets to file

## Original Jokes 

- Taken from https://github.com/wesbos/dad-jokes

License
----

MIT
