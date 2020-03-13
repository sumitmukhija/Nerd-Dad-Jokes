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
        contents = str(contents).replace("**Q**", "Question").replace("**Q:**", "Question")
        contents = str(contents).replace(
            "**A**", "Answer").replace("**A:**", "Answer")
        jokes = contents.split('---')
        return jokes

    def get_random_joke(self):
        """Returns a random joke from the source       
        Arguments:
            jokes list of string -- Each element is a joke. Also, new lines 
            removed and tabs replaced with space
        """
        if self.jokes is None:
            return "No Joke. (Dad's gone fishing. Catch you later!)"
        random_joke_index = randrange(len(self.jokes))
        return str(self.jokes[random_joke_index]).replace("\\n", "").replace("\\t", " ")
