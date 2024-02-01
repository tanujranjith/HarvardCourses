import re

def main():
    print(convert(input("Hours: ").strip()))

def convert(prompt):
    hhMM = re.match(r'(^(([1-9])|([1][0-2]))(:[0-5]\d)\s(A|P)M) to ((([1-9])|([1][0-2]))(:[0-5]\d)\s(A|P)M$)', prompt) # HH:MM AM/PM format
    hh = re.match(r'(^(([1-9]|[1][0-2]))\s(A|P)M) to ((([1-9]|[1][0-2]))\s(A|P)M$)', prompt) # HH AM/PM format

    if hhMM:
        start, startAMPM, to, end, endAMPM = prompt.split()
        if startAMPM == 'PM':
            s_hh12, s_mm12 = start.split(':')
            startTime = f'{int(s_hh12) + 12}:{s_mm12}' if int(s_hh12) < 12 else f'12:{s_mm12}'
            if endAMPM == 'PM':
                e_hh12, e_mm12 = end.split(':')
                endTime = f'{int(e_hh12) + 12}:{e_mm12}' if int(e_hh12) < 12 else f'12:{e_mm12}'
            else:
                e_hh12, e_mm12 = end.split(':')
                endTime = f'0{end}' if int(e_hh12) < 10 else (f'{end}' if int(e_hh12) == (10 or 11) else f'00:{e_mm12}')
        else:
            s_hh12, s_mm12 = start.split(':')
            startTime = f'0{start}' if int(s_hh12) < 10 else (f'{start}' if int(s_hh12) == (10 or 11) else f'00:{s_mm12}')
            if endAMPM == 'PM':
                e_hh12, e_mm12 = end.split(':')
                endTime = f'{int(e_hh12) + 12}:{e_mm12}' if int(e_hh12) < 12 else f'12:{e_mm12}'
            else:
                e_hh12, e_mm12 = end.split(':')
                endTime = f'0{end}' if int(e_hh12) < 10 else (f'{end}' if int(e_hh12) == (10 or 11) else f'00:{e_mm12}')

    elif hh:
        start, startAMPM, to, end, endAMPM = prompt.split()
        if startAMPM == 'PM':
            startTime = f'{int(start) + 12}:00' if int(start) < 12 else '12:00'
            if endAMPM == 'PM':
                endTime = f'{int(end) + 12}:00' if int(end) < 12 else '12:00'
            else:
                endTime = f'0{end}:00' if int(end) < 10 else (f'{end}:00' if int(end) == (10 or 11) else '00:00')
        else:
            startTime = f'0{start}:00' if int(start) < 10 else (f'{start}:00' if int(start) == (10 or 11) else '00:00')
            if endAMPM == 'PM':
                endTime = f'{int(end) + 12}:00' if int(end) < 12 else '12:00'
            else:
                endTime = f'0{end}:00' if int(end) < 10 else (f'{end}:00' if int(end) == (10 or 11) else '00:00')

    elif (hhMM and hh) == None:
        raise ValueError

    return f'{startTime} to {endTime}'


if __name__ == "__main__":
    main()