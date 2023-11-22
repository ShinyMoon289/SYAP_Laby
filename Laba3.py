def zadanie1():
    while 1:

        print("1 - Enter a string\n2 - Copy contents to F2\n3 - Return")

        ch = int(input())
        if ch == 1:
            myfile = open("F1.txt", "a")
            line = str(input("Enter string: "))
            myfile.writelines(f"{line}\n")
            myfile.close()
        elif ch == 2:
            myfile = open("F1.txt", "r")
            myfile2 = open("F2.txt", "a")
            line = myfile.readline()
            word = str("")
            for i in line:
                if i == " ":
                    break
                else:
                    word = word+i
            for i in myfile:
                if word not in i:
                    myfile2.writelines(f"{i}")
            myfile.close()
            myfile2.close()

            myfile2 = open("F2.txt", "r")
            sylcount = 0
            vowels = "aeiuyo"
            line = myfile2.readline()
            line = line.lower()
            for i in line:
                if i.isalpha():
                    if i not in vowels:
                        sylcount += 1
            print(f"Syllables: {sylcount}")
        elif ch == 3:
            break
