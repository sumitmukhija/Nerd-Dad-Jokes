from ndf import app as appl
from .singleton import singleton
from random import randrange

@singleton
class JokeHelper(object):
    """SINGLETON Class responsible to read and return a random joke
    from ndf/static/jokes/jokes.txt
    
    Arguments:
        object
    """

    def __init__(self, file_path='static/jokes/jokes.txt'):
        app = appl.create_app()
        with app.open_resource(file_path) as file:
            contents = file.read()
            self.jokes = self.segregate_jokes_from_file_contents(contents)
            
    def segregate_jokes_from_file_contents(self, contents):
        """In the given content,
        1. Replaces the **Q** with questions
        2. Replaces the **A** with Answer
        3. splits based on ---. Each split is an individual joke
        Arguments:
            contents string -- The text from the file in the initializer
        """
        contents = self.strip_escape_sequences(contents)
        jokes = contents.split('---')
        return jokes
    
    def strip_escape_sequences(self, contents):
        """Removes tabs, spaces, replaces **Q** & **A** with Questions and answers
        Adds a space after ?
        
        Arguments:
            contents {str} -- Contents read from the file
        
        Returns:
            str -- Stripped string
        """
        return str(contents).replace("**Q**", "Question").replace("**Q:**", "Question").replace(
            "**A**", "Answer").replace("**A:**", "Answer").replace("\\n", "").replace("\n", "").replace("\\t", " ").replace("\t", "").replace("?", "? ")


    def get_random_joke(self):
        """Returns a random joke from the source       
        
        Returns:
            str -- A random joke
        """
        if self.jokes is None:
            return "No Joke. (Dad's gone fishing. Catch you later!)"
        random_joke_index = randrange(len(self.jokes))
        return str(self.jokes[random_joke_index])

    def should_post(self, factor = 10):
        """Randomly decides if a joke should be posted on Twitter.
            1/10 chance that it'll be posted. Factor defaults to 10
        Returns:
            [Boolean] -- True if should be posted, False otherwise
        """
        return True if ((10 + randrange(100))%factor == 0) else False
