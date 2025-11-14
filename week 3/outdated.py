
months_numbered = {
    "January" : 1 ,
    "February": 2 ,
    "March" : 3,
    "April": 4,
    "May" : 5,
    "June" : 6,
    "July" : 7,
    "August" : 8,
    "September" : 9,
    "October" : 10,
    "November": 11,
    "December": 12
}

while True:
    z = 0
    input_date = input("date; ")
    for i in input_date:
        if i == "/":
            z += 1
    if z == 2:
        try:
            month_in_num, day_in_num, year_in_num = input_date.split("/")
            #convert to int:
            month_in_num = int(month_in_num)
            day_in_num = int(day_in_num)
            year_in_num = int(year_in_num)
            #check validity
            if 0 < month_in_num <= 12 and 0 < day_in_num <= 31:
                print(str(year_in_num), str(month_in_num).zfill(2), str(day_in_num).zfill(2), sep="-")
                break
            else:
                raise ValueError
        except (ValueError, TypeError, KeyError):
            print("incorrect format")
            continue
    elif z == 0:
        try:
            input_date = input_date.replace(",", "")
            month_word, day, year = input_date.split()
            month_in_num = months_numbered[month_word]
            #covert to int to compare
            day = int(day)
            year = int(year)
            #check validiy:
            if 0 < month_in_num <= 12 and 0 < day <= 31:
                print(str(year), str(month_in_num).zfill(2), str(day).zfill(2), sep="-")
                break
            else:
                raise ValueError
            
        except (ValueError, TypeError, KeyError):
            print("incorrect format")
            continue
