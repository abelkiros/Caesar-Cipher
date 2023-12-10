"""
file: caesar.py
language: python3
author: amk7296@g.rit.edu abel m kiros
description: This program reads a data file encrypts and decrypt.
"""
def read_file(data):
    """This function reads the file line by line and stores it as a list

    :param file: Is the text file the user selects
    :return: A list of numbers
    """
    with open(data) as f:
        lst = []
        for line in f:
            lst.append(line.strip())
        return lst

def quick_sort(lst):
    """
    quickSort: List( A ) -> List( A )
        where A is 'totally ordered'
    """
    if lst == []:
        return []
    else:
        pivot = lst[0][1]
        (less, same, more) = partition(pivot, lst)
        return quick_sort(more) + same + quick_sort(less)

def partition(pivot, lst):
    """
    partition: A * List( A ) -> Tuple( List( A ), List( A ), List( A ) )
        where A is totally ordered
    """
    (less, same, more) = ([], [], [])
    for e in lst:
        if e[1] < pivot:
            less.append(e)
        elif e[1] > pivot:
            more.append(e)
        else:
            same.append(e)
    return (less, same, more)


def encrypt(string, offset):
    """

    :param string: takes in string
    :param offset: int shifts value
    :return: result of new value offset
    """
    result = ''

    for ch in string:
        value = ord(ch)
        value += offset

        if ch.isspace():
            result += ch

        else:

            if value > ord('z'):
                value = value - 26
            new_ch = chr(value)
            result += new_ch

    return result


def decrypt(strings,offset):

    new_list =[]

    for string in strings:
        result = ''
        for ch in string:
            value = ord(ch)
            value -= offset #decrypt is subtracted

            if ch.isspace():
                result += ch

            else:
                if value < ord('a'):
                    value = value + 26
                new_ch = chr(value)
                result += new_ch
        new_list.append(result)

    return new_list

def brute(string):

    result = []
    for i in range(0,26): # 1.....26
        d = decrypt(string, i)
        result += [d]
    return result

def char_count(strings):
    index_offset = ord('a')
    new_string = ''
    for char in strings:
        new_string += "".join(char.strip().split(" "))

    lst = []
    for i in range(ord('a'), ord('z') +1):
        lst += [[chr(i), 0]]

    for ch in new_string:
        lst[ord(ch) - index_offset][1] += 1

    return lst


def educated_brute(strings):
    print(char_count(strings))
    sorted_strings_list = quick_sort(char_count((strings)))
    print(sorted_strings_list)

    max_count = 0
    max_char = ''
    result = []
    prev_char = sorted_strings_list[0]
    count = 0
    for char in sorted_strings_list:
        if max_count < count:
            max_count = count
            max_char = prev_char
        count += 1
        prev_char = char
    result = []

    return result

def main():

    input_encrypt = input("Encrypting file: ")

    datafile = read_file(input_encrypt)

    input_offset = int(input("Using the offset to encrypt: "))

    x = datafile

    result = []
    for line in x:
        b = encrypt(line, input_offset)
        result.append(b)

    counter = 0

    for i in brute(result):

        for j in i:
            print(j)

        print('\n')
        answer = input("Does this look right? (Y/N)").upper()
        if answer == "Y":
            print("The offset was: ", counter)
            break
        counter += 1

    decrypt = ["dahhk sknhz", "ep pdeo skngejc", "e ywj nawz pdeo", "ok ep iqop xa"]

    counter = 0

    for line in decrypt:
        print(line)

    string = ""
    strings = string.join(decrypt)


main()