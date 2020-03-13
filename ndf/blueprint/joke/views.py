from flask import Blueprint
from ndf.utility.read_jokes import JokeHelper
from ndf.utility.bot import Bot
from flask import jsonify

joke = Blueprint("joke", __name__)

@joke.route("/")
def random_joke():
    """Root url will return a random joke. Uses utility/read_jokes/JokeHelper class
    
    Returns:
        JSON string -- JSON string with 'random_joke' key
    """
    joke_helper = JokeHelper()
    joke = joke_helper.get_random_joke()
    if joke_helper.should_post():
        Bot().make_public_tweet(joke + " #DadJokes #Programmer #Dev #PJ")
        Bot().retweet_dad_joke()
    return jsonify({"random_joke" : joke})

@joke.route("/about")
def about():
    """About endpoint credits the actual jokes repo and will point to the repo

    Returns:
        JSON string - JSON string with repo_url, github_username
    """
    return jsonify({"about": "The RESTful service is based on the awesome repo by Wes Bos with an assortment of Dad jokes.", "repo_url": "https://github.com/wesbos/dad-jokes", "github_username": "wesbos"})
    
