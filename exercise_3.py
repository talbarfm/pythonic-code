def count_hi_v1(string):
    count = 0
    i = 0
    while i<len(string):
        if string[i] == "h":
            if i+1 < len(string) and string[i+1] == "i":
                count = count + 1
        i = i + 1
    return count


print(count_hi_v1("blahiblahi"))

