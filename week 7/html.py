import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(r"^<iframe.*?src=\"(?:https?://(?:www\.)?youtube\.com/)embed/(.+?)\".*?></iframe>$",s):
        id = matches.group(1)
        if "?" in id:
            pieces = id.split("?")
            id = pieces[0]
        elif "&" in id:
            pieces = id.split("&")
            id = pieces[0]

        final = f"https://youtu.be/{id}"
        return final
    else:
        return "error"


if __name__ == "__main__":
    main()