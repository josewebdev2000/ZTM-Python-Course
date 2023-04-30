# Show how to use external packages
import pyjokes

joke = pyjokes.get_joke('en', 'neutral')
print(joke)