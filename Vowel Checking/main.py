char = input("Enter any alphabet : ")
ch=char.lower()
if ch=='a' or ch=="e" or ch=="i" or ch=="o" or ch=="u":
    print(f"This {char} is a vowel.")
else:
    print(f"This {char} is not a vowel.")