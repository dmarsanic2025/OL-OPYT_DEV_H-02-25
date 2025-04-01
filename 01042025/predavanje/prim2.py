file = open(
    r"01042025\predavanje\text.txt",
    "r",
    encoding="utf-8",
)
print(file.read())
# print(file.readlines())
file.close()


file_w = open(
    r"01042025\predavanje\text_w.txt",
    "w",
    encoding="utf-8",
)
file_w.write("Sad je nesto drugo : Upisi nesto tu!!!!!!!!!!!!!!!!!!!!!!!!!!")
file_w.close()


file_w = open(
    r"01042025\predavanje\text_w.txt",
    "a",
    encoding="utf-8",
)
file_w.write("\nSad je nesto drugo ali je ostalo i staro")
file_w.close()


with open(
    r"01042025\predavanje\text.txt",
    "r",
    encoding="utf-8",
) as file:
    sadrzaj = file.read()


print(sadrzaj)

try:
    file = open(
        r"01042025\predavanje\text.txt",
        "r",
        encoding="utf-8",
    )
    print(file.read())
except Exception as e:
    print(e)
finally:
    file.close()

print("*" * 70)

with open(
    r"01042025\predavanje\text.txt",
    "r",
    encoding="utf-8",
) as file:
    line = file.readline()
    while line != "":
        print(line.strip())
        line = file.readline()

print("*" * 70)

with open(
    r"01042025\predavanje\text.txt",
    "r",
    encoding="utf-8",
) as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())
