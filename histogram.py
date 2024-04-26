from os import strerror

counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
file_name=input("Enter File name:  " )

try:
    s = open(file_name, 'rt', encoding='utf-8')
    for line in s:
        for char in line:
            if char.isalpha():
                counters[char.lower()] += 1
    s.close()

    for char in counters.keys():
        cnt = counters[char]
        if cnt > 0: 
            print(char, '->', cnt)
except IOError as e:
    print("IOError occurred: ", strerror(e.errorno))