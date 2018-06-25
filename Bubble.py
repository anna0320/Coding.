list = [4, 2 , 6 , 8, 0 , 11 , 49, 34 , 100 , 75 , 82 , 3, 42]
counter = 1
while counter < len(list):
     for i in range(len(list) - counter):
          if list[i] > list[i + 1]:
              list[i], list[i + 1] = list[i + 1], list[i]
     counter += 1
     print(list)