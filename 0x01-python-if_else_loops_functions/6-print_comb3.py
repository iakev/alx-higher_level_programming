#!/usr/bin/python3
for i in range(0,100,10):
    for j in range(i + (i//10) + 1, i + 10):
        if j < 10:
          print(f"0{j}",end=", ")
        else:
            if j % 10 == 0:
                j = j + (j // 10)
                print(f"{j}",end=", " if j != 99 else "\n")
            else:
                print(f"{j}",end=", " if j != 89 else "\n")
