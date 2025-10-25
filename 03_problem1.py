# Problem 1
print ('''Twinkle, twinkle, little star, how I wonder what you are. Up above the world so high,
like a diamond in the sky. Twinkle, twinkle, little star, how I wonder what you are.
When the blazing sun is set, and the grass with dew is wet. Then you show your little
light, twinkle, twinkle all the night. Twinkle, twinkle little star, how I wonder what you
are.
Then the traveler in the dark thanks you for your tiny spark. How could he see where to
go if you did not twinkle so? Twinkle, twinkle little star, how I wonder what you are.
As your bright and tiny spark lights the traveler in the dark, though I know not what you
are, twinkle, twinkle, little star. Twinkle, twinkle, little star, how I wonder what you are.''') 


# Problem 2
# Python text to speech
import pyttsx3
engine = pyttsx3.init()
engine.say("Assalamualaikum. Muhammad is our prophet.")
engine.runAndWait()


# Problem 3
import os

def print_directory_contents(path='.'):
    """
    Print the files and directories inside the given path.
    Default is the current working directory.
    """
    try:
        entries = os.listdir(path)
    except FileNotFoundError:
        print(f"Error: The path '{path}' does not exist.")
        return
    except PermissionError:
        print(f"Error: Permission denied for path '{path}'.")
        return
    except OSError as e:
        print(f"OS error for path '{path}': {e}")
        return

    print(f"Contents of directory '{path}':")
    for entry in entries:
        print(entry)

if __name__ == '__main__':
    # You can pass a directory path here, or leave it to default '.' (current directory)
    dir_path = input("Enter directory path (or press Enter for current directory): ").strip()
    if not dir_path:
        dir_path = '.'
    print_directory_contents(dir_path)
