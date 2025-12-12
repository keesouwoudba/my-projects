from PIL import ImageOps, Image
import sys
import os
#the code pastes the photo with shirt to your photo, so you will become with shirt

if len(sys.argv) != 3:
    sys.exit("too few or many command-line args")

rfile = sys.argv[1]#file to read, the file with your photo
wfile = sys.argv[2]#the name of the file to save as your final photo with shirt

allowed = {".jpg", ".jpeg", ".png"}

rfile_ext = os.path.splitext(rfile)[1].lower()
wfile_ext = os.path.splitext(wfile)[1].lower()

if not os.path.exists(rfile):
    sys.exit(f"the file {rfile} was not found")

if rfile_ext not in allowed or wfile_ext not in allowed:
    sys.exit("the extension should be .jpg, .jpeg, .png")

try:
    shirt_image = Image.open("shirt.png").convert("RGBA")
    size = shirt_image.size
    input_image = Image.open(rfile).convert("RGBA")
    fitted_input = ImageOps.fit(input_image, size)
    fitted_input.paste(shirt_image, shirt_image)
    fitted_input.save(wfile)


except FileNotFoundError:
    sys.exit("the file was not found")

except Exception as e:
    sys.exit(f"the error {e} occurred")