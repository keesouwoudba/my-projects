import re
import sys


time_conversion = {
    "12AM": "00",
    "1AM": "01",
    "2AM": "02",
    "3AM": "03",
    "4AM": "04",
    "5AM": "05",
    "6AM": "06",
    "7AM": "07",
    "8AM": "08",
    "9AM": "09",
    "10AM": "10",
    "11AM": "11",
    "12PM": "12",
    "1PM": "13",
    "2PM": "14",
    "3PM": "15",
    "4PM": "16",
    "5PM": "17",
    "6PM": "18",
    "7PM": "19",
    "8PM": "20",
    "9PM": "21",
    "10PM": "22",
    "11PM": "23"
    }

def main():
    time = input("Hours: ").strip().upper()

    finaltime = convert(time)
    if finaltime is not None:
        print(f"time is {finaltime}")
    elif finaltime is None:
        print("incorrect time was passed")


def convert(s):
    if matches := re.search(r"^((?:[0-9]|1[0-2])(?:\:(?:[0-9]|[1-5][0-9]))?\s*?(?:AM|PM))\s*?TO\s*?((?:[0-9]|1[0-2])(?:\:(?:[0-9]|[1-5][0-9]))?\s*?(?:AM|PM))$",s):
        frrom, tto = matches.groups()
        frrom = to24(frrom)
        tto = to24(tto)

        time = f"from {frrom} to {tto}"

        if frrom is not None and tto is not None:
            return time
        else:
            return None



def to24(time_12):
    try:
        #data received: 12[:15] AM
        time_12 = time_12.strip()
        if matches1 := re.search(r"^([0-9]|1[0-2])\:([0-9]|[1-5][0-9])\s*?(AM|PM)",time_12):
            hours, minutes, ampm = matches1.groups()
            hours_ampm = f"{hours}{ampm}"
            hours_final = time_conversion[hours_ampm]
            time_24 = f"{hours_final}:{minutes}"

        elif matches2 := re.search(r"^([0-9]|1[0-2])\s*?(AM|PM)",time_12):
            hours, ampm = matches2.groups()
            hours_ampm = f"{hours}{ampm}"
            hours_final = time_conversion[hours_ampm]
            time_24 = f"{hours_final}:00"

        return time_24
    except Exception as e:
        print(f"error {e}")
        return None


if __name__ == "__main__":
    main()