
i = 0

while i < 10:
    if i == 3:
        print("Skipping 3 using continue")
        i += 1
        continue  # Skip the rest of the loop when i is 3

    if i == 5:
        print("Break at 5 using break")
        break  # Exit the loop when i is 5

    if i == 7:
        pass  # Do nothing, just a placeholder
        # Normally used when a statement is syntactically required
        print("This is a pass statement at 7")

    print("Current value of i:", i)
    i += 1
