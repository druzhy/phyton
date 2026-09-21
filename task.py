# import lib
#
# res = lib.my_abs(-5)
# print(res)

# file = open("data.txt","r", encoding="utf-8")
# for line in file:
#     print(line.strip())
# file.close()

# file  = open("out.txt","a", encoding="utf-8")
# file.write("Hello!!!\n")
# file.write("Hello\n")
# file.close()

with open("data.txt","r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
