from datetime import date
import sys
from datetime import timedelta
import inflect

bday = input("Date of Birth: ")
p=inflect.engine()

def main():
    try:
        x,y,z= bday.split("-")
        birth=date(int(x),int(y),int(z))
    except:
        sys.exit("Invalid date")

    dif=date.today()-birth
    letters=p.number_to_words(int(dif.total_seconds()/60), andword="")
    print(f'{letters.capitalize()} minutes')

if __name__=="__main__":
    main()