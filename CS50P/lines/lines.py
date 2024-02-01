import sys

def count_lines(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.read().splitlines()
        count = 0
        for line in lines:
            line = line.strip()
            if line and not line.startswith('#'):
                count += 1
        return count
    except:
        print("File does not exist")
        sys.exit(1)
try:
    #print(sys.argv[1])
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    else:
        file_name = sys.argv[1]
        file_split = file_name.split(".")
        if file_split[1] == "py":
            line_count = count_lines(file_name)
            print(line_count)
        else:
            print("Not a Python file")
            sys.exit(1)

except:
    sys.exit(1)