# w, r, b, a, t
# +

# with open("main.py", "r") as myfile:
# myfile.write("\nprint(\"Hello world\")")

# chunk = myfile.read(10)
#
# print(chunk, end="")
#
# chunk = myfile.read(10)
#
# print(chunk, end="")

# lines = myfile.readlines()
#
# for line in lines:
#     print(line, end="")


################### Binary FS
# rb - read binary

# with open("data.abc", "rb") as f:
#     result = f.read(5)
#
#     print(result)

################### Binary FS (pickle)
import pickle

#
# games = [{
#     "name": "GTA VI",
#     "price": 13
# }, {
#     "name": "PUBG",
#     "price": 19
# }, {
#     "name": "R6",
#     "price": 9
# }]
#
# file = open("games.bin", "wb")
#
# pickle.dump(games, file)
#
# file.close()

###

# file = open("games.bin", "rb")
#
# games = pickle.load(file)
#
# print(games)
#
# file.close()


################### JSON (write)
import json
# data = {
#     "Language": "Python",
#     "Version": 3.12,
#     "IsSupported": True,
#     "Versions": [3.10, 3.11, 3.12],
#     "Metadata": {
#         "Localized": True
#     },
#     "Data": None
# }

# with open("data.json", "w") as f:
#     json.dump(data, f)

################### JSON (read)

# with open("data.json", "r") as file:
#     data = json.load(file)
#
#     print(data["Version"])
#     print(data["Versions"][0])

################### shelve

import shelve

# write data
# with shelve.open("data.bin") as f:
#     f["Language"] = "Python"
#     f["Version"] = 3.12
#     f["Versions"] = [3.07, 3.11, 3.12]


with shelve.open("data.bin") as f:
    print(f["Language"])
    print(f["Version"])
    print(f["Versions"])