import pyfiglet
import sys
import random






text_to_convert = input("TEXT: ")

font = None


if len(sys.argv) == 1:
    try:
        fonts = pyfiglet.FigletFont.getFonts()
        font = random.choice(fonts)
        ascii_art = pyfiglet.figlet_format(text_to_convert, font)
        print(f"your font is: {font}\n")
        print(ascii_art)

    except (ValueError, IndexError, pyfiglet.FontNotFound, pyfiglet.FontError):
        sys.exit("incorrect format(font)")

elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    try:
        ascii_art = pyfiglet.figlet_format(text_to_convert, sys.argv[2])
        print(f"your font is: {sys.argv[2]}\n")
        print(ascii_art)
    except (ValueError, IndexError, pyfiglet.FontNotFound, pyfiglet.FontError):
        sys.exit("incorrect format(font)")

else:
    sys.exit("incorrect format(elif)")