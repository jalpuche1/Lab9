def password_encoder(password):
    encoded_password = ""
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)  # Shifting each digit up by 3 numbers
        encoded_password += encoded_digit
    return encoded_password

while True:
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

    choice = input("Please enter an option: ")

    if choice == "1":
        password = input("Please enter your password to encode: ")
        encoded_password = password_encoder(password)
        print("Your password has been encoded and stored!")
    # elif choice == "2":
    #     if 'encoded_password' not in locals():
    #         print("Please encode a password first.")
    #         continue
    #     print(
    #         f"The encoded password is {encoded_password}, and the original password is {password_decoder(encoded_password)}.")
    elif choice == "3":
        print("Exiting the program.")
        break
    else:
        print("Invalid option. Please choose again.")