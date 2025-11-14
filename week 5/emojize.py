import emoji
import sys

if len(sys.argv) == 2:
    print(emoji.emojize(f":{sys.argv[1]}:", language='alias'))