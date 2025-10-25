import pyjokes


"""this program fetches a random programming 
joke using the pyjokes module"""

#This is a single line commment 

# 1. First, make sure you have the pyjokes module installed.
# You can install it using pip if you haven't already:
print("Fetching a random programming joke for you:")
joke = pyjokes.get_joke()
print(joke)



