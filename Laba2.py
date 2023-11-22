import numpy as np



def zadanie1():  # this task shows the amount vowels and syllables in a string

    try:
        word = str(input("Enter the word"))
    except TypeError:
        print("Incorrect input!")
    else:
        vowcount = 0
        sylcount = 0
        print(f"Your string: {word}")
        word = word.lower()
        for i in word:
            if i.isalpha():
                if i in vowels:
                    vowcount += 1
                else:
                    sylcount += 1
        print(f"Syllables: {sylcount}, vowels: {vowcount}")


def zadanie2():
    while 1:
        try:
            print("1 - Enter a string\n2 - Enter a list\n3 - Enter a dictionary (preset)")
            ch = int(input("Enter the type you want to type in."))
        except TypeError:
            print("Incorrect value!")
        else:
            if ch == 1:
                try:
                    phrase = str(input("Enter your sentence:"))
                except TypeError:
                    print("Incorrect input!")
                else:
                    words = 1
                    for i in phrase:
                        if not i.isalnum():
                            phrase.replace("ab", "")
                    for i in phrase:
                        if i == " ":
                            words += 1

                    print(f"{phrase}. Number of words = {words}")
            elif ch == 2:
                try:
                    size = int(input("Enter the size of the list: "))
                    if size <= 0:
                        raise ValueError("Negative or null size is not allowed!")
                except TypeError:
                    continue
                else:
                    mylist = list()
                    for m in range(size):
                        try:
                            el = int(input())
                        except ValueError:
                            print("Incorrect value found!")
                        else:
                            mylist.append(el)
                count = 0
                for i in mylist:
                    if i % 2 == 0:
                        count += 1
                print(f"Original list:{mylist}. Amount of even numbers: {count}")
                mylist = set(mylist)
                mylist = list(mylist)
                print(f"Final list: {mylist}. ")

            # The dictionary you're supposed to type is actually preset, cause i'm too lazy
            elif ch == 3:
                mydict = {"Border of space": 100000,
                          "Deepest point on Earth": 12300,
                          "Average altitude of planes": 4000}

                vals = list(mydict.values())
                max = vals[0]
                for i in vals:
                    if i > max:
                        max = i
                print(max)


def zadanie3():
    try:
        cols = int(input("Enter the number of columns: "))
        rows = int(input("Enter the number of rows: "))
        if cols <= 0 or rows <= 0:
            raise ValueError
    except ValueError:
        print("Incorrect sizes!")
    else:
        matrix = np.empty([cols, rows], dtype=int)
        for j in range(cols):
            for i in range(rows):
                try:
                    el = int(input())
                except TypeError:
                    print("Incorrect value found!")
                else:
                    matrix[i][j] = el

        count = 0
        for i in range(rows):
            sw = True
            for j in range(cols):
                if matrix[i][j] == 0:
                    sw = False
                else:
                    continue
            if sw:
                count += 1
        print(f"Number of rows that don't have 0: {count}")
