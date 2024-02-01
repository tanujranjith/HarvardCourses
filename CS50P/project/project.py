import sys
import csv

def main():
    check_correct_args()
    data = []
    try:
        with open(sys.argv[1]) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        sys.exit("Could't read CSV file")

    output = []
    for row in data:
        house = select_house(row["charecterstic"])
        grade = select_grade(row["birthdate"])
        output.append({"name": row["name"], "house": house, "grade": grade})

    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "house", "grade"])
        writer.writerow({"name": "name", "house": "house", "grade": "grade"})
        for row in output:
            writer.writerow({"name": row["name"], "house": row["house"], "grade": row["grade"]})

def check_correct_args():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        sys.exit("Not CSV files")


def select_house(char):
    if char in["courage", "loyalty", "adventure"]:
        return "Oakridge House"
    elif char in ["dedication", "patience", "honesty"]:
        return "Cresthaven Manor"
    elif char in ["wisdom", "creativity", "perfectionsim"]:
        return "Willowbrook Cottage"
    elif char in ["ambition", "competitive", "leadership"]:
        return "Falconwood Estate"
    else:
        return "No House"


def select_grade(year):
    age = 2023 - int(year)
    grade = age - 5
    return "Grade " + str(grade)


if __name__ == "__main__":
    main()