while True:
    print("\n--- STRING OPERATIONS MENU ---")
    print("1. Reverse string")
    print("2. Convert to Uppercase")
    print("3. Convert to Lowercase")
    print("4. Count digits in string")
    print("5. Count alphabets in string")
    print("6. Exit")

    choice = int(input("Enter your choice: "))
    s = input("Enter a string: ")

    if choice == 1:
        print("Reversed string:", s[::-1])

    elif choice == 2:
        print("Uppercase:", s.upper())

    elif choice == 3:
        print("Lowercase:", s.lower())

    elif choice == 4:
        count = 0
        for ch in s:
            if ch.isdigit():
                count += 1
        print("Number of digits:", count)

    elif choice == 5:
        count = 0
        for ch in s:
            if ch.isalpha():
                count += 1
        print("Number of alphabets:", count)

    elif choice == 6:
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")
