def to_str(num, base):
    convert_string = "0123456789ABCDEF"
    if num < base:
        return convert_string[num]
    else:
        return to_str(num // base, base) + convert_string[num % base]

if __name__ == "__main__":
    print(to_str(1453, 16))
    print(to_str(11, 10))
    print(to_str(11, 8))
    print(to_str(11, 2))
