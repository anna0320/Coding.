list = [4, 2 , 6 , 8, 0 , 11 , 49, 34 , 100 , 75 , 82 , 3, 42]
index = 0
while index < len(list) - 1:
    minNum = index
    startMin = index + 1
    while startMin < len(list):
        if list[startMin] < list[minNum]:
            minNum = startMin
        startMin += 1
    indexNum = list[index]
    list[index] = list[minNum]
    list[minNum] = indexNum
    index += 1
    print(list)