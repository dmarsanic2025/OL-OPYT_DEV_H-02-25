s = "           hellO woRld       "
upper_s = s.upper()
print(upper_s)


lower_s = s.lower()
print(lower_s)


stripped_s = s.strip().strip("d").strip("h")
print(stripped_s)


splitted_s = s.split()
print(splitted_s)

separator = ";"
joined_string = separator.join(splitted_s)
print(joined_string)


name = "Petar"
years = 25
print("Dobrodosao, {}! Sretan ti {}. rodendan!".format(name, years))
print("Dobrodosao, {0}! Sretan ti {1}. rodendan!".format(name, years))


PI = 3.1415925355463
print("Vrijednost broja pi je {:.2f} !".format(PI))

# f-strings -> preporuka
print(f"Dobrodosao, {name}! Sretan ti {years}. rodendan!")

print("Dobrodosao, ", name, "! Sretan ti ", years, ". rodendan!", sep="")
print(
    "Dobrodosao, " + name + "! Sretan ti " + str(years) + ". rodendan!",
)
