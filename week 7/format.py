import re

url = input("URL: ").strip()



if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)$", url, re.IGNORECASE):
    username = matches.group(1)
    print(f"username: {username}")




username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
