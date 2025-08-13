# w - write
# r - read
# a - append

# t - text
# b - binary

######### write to a file
# file = open("data.txt", "w")
#
# names = []

# while True:
#     name = input("Enter a name: ")
#
#     if name == "0":
#         break
#
#     names.append(name + "\n")

# if file.writable():
#     file.write()
#     file.writelines(names)
#
# file.close()



######### read from a file

with open("data.txt", "r") as file:
    ### read lines thru for loop
    # for line in file:
    #     print(line, end="")

    ### read lines
    # lines = file.readlines()
    #
    # print(lines)

    ### read chunks, seek, tell
    # chunk = file.read(4)
    #
    # print(chunk)
    #
    # file.seek(5)
    #
    # chunk = file.read(5)
    #
    # print(chunk)
    #
    # file.seek(0, 2)
    #
    # pos = file.tell()
    #
    # print(pos)

    ### read a single line
    # line1 = file.readline()
    # line2 = file.readline()
    #
    # print(line1, line2)


# x = "Hello\nWorld"
# # \n - new line
# # \t - tab
# # \b - backspace
#
# print(x)