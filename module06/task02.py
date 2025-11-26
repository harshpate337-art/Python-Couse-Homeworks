names = set()

while True:
    name = input("Enter a name (leave blank to stop): ")

    if name == "":
        break

    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)

print("\nUnique names entered:")
for n in names:
    print(n)
