
LEGAL_LIMIT = 42


length = float(input("Enter the length of the zander in centimeters: "))


if length < LEGAL_LIMIT:
    shortage = LEGAL_LIMIT - length
    print(f"The zander is too small and must be released back into the lake.")
    print(f"It is {shortage:.1f} cm short of the legal limit.")
else:
    print("The zander meets the size requirement. You may keep it.")
