while True:
    x = input("podaj co wybierasz: 1 dla papieru, 2 dla nożyczek, 3 dla kamienia: ")
    
    print("\n"*100)
    
    y = input("podaj co wybierasz: 1 dla papieru, 2 dla nożyczek, 3 dla kamienia: ")
    
    try:
        x1 = int(x)
        y1 = int(y)
    except ValueError:
        print("niepoprawne dane")
        print(f"1: {x}, 2: {y}")
        continue
    
    if x1 > 3 or x1 < 1 or y1 < 1 or y1 > 3:
        print("niepoprawne dane")
        print(f"1: {x1}, 2: {y1}")
        continue
    
    if x == y:
        print("remis")
        continue
    
    if (x1 == y1 - 1) or (x1 == 3 and y1 == 1):
        print("2 wygrywa!")
    else:
        print("1 wygrywa!")