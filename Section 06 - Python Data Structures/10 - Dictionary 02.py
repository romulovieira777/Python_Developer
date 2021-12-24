mycar = {
    "brand": "Range Rover Sports",
    "model": "HSE",
    "year": 2017
}

my_greens = dict(fruit="Green Apples", vegetables="Kale")

print(len(mycar))

mycar["year"] = 2019
print(mycar)

print(mycar.get("year"))

mycar.update({"color": "silver"})
print(mycar)

b = mycar.keys()
print(b)

v = mycar.values()
print(v)

mycar.pop("color")
print(mycar)

mycar.clear()
print(mycar)

del mycar
