brands = ["Apple", "Microsoft", "Asus", "lenovo"]


for item in brands:
    print(f"The name of this brand is {item}")

    if item == "Hp":
        break
else:
    print("This is else after for loop")