first_part = "251224"
for i in range(10000):

    if i < 10:
        i = f"000{i}"
    elif i < 100:
        i = f"00{i}"
    elif i < 1000:
        i = f"0{i}"
    else:
        i = str(i)
     
    potential_birth_number = first_part + i
    if int(potential_birth_number) % 11 == 0:
        print(potential_birth_number)