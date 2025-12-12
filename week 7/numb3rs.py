import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    pattern = r"(?:[1-9]?[0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])"
    final_pattern = rf"^{pattern}\.{pattern}\.{pattern}\.{pattern}$"

    if match := re.search(final_pattern, ip):
        return "valid"
    return "invalid"

    
if __name__ == "__main__":
    main()