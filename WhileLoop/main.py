# try:
#     num1 = int(input())
#     num2 = int(input())
#
#     print(num1 / num2)
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
# except ValueError:
#     print("Invalid input.")

# a = 3
# i = 0
#
# while i < a:
#     print("Hello while loop!")
#     i += 1
#
# print("While loop ended")


### continue

i = 0
## [3, 7]
# 0 1 2 3 4 5 6 7 8 9
# while i < 10:
#     if i >= 3 and i <= 7:
#         continue
#     print(i)
#     i += 1 # инкремент

### break
# a = 5
#
# while True:
#     if a == 0:
#         break
#
#     print("Hello while loop!")
#
#     a -= 1  # декремент




###
# while True:
#     print("1. Start game")
#     print("2. Options")
#     print("3. Exit")
#
#     choice = int(input())
#
#     if choice == 1:
#         print("Starting game...")
#     elif choice == 2:
#         print("Opening options...")
#     elif choice == 3:
#         break
#     else:
#         print("Invalid choice!")
#
# print("Thanks for playing!")

# i = 0
#
# while i < 3:
#     print("some text")
#
#     i += 1 #



while True:
    number = int(input()) # 0

    if number == 0:
        break

    print(number)

print("end")
