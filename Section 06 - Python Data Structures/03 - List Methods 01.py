fruits = ["Berries", "Apples", "Grapes", "Oranges"]
vegetables = ["Kale", "Broccoli", "Lettuce"]

# Method extend
fruits.extend(vegetables)
print(fruits)

# Method append
vegetables.append("Bean")
print(vegetables)

# Method sort
vegetables.sort()
print(vegetables)

vegetables.sort(reverse=True)
print(vegetables)

# Method count
print(fruits.count("Berries"))
