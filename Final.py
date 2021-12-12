final = []
answer = []
answer1 = []

def move(list1, list2, n, actions):
    if(n <= 0):
        tank = 1000
        for a in actions:
            tank = tank + a
            answer.append(tank)
    else:
        list1D = list(dict.fromkeys(list1))
        for x in list1D:
            list2.append(x)
            list1.remove(x)
            if (n % 2) ==0:
                actions.append(-x)
            else:
                actions.append(x)
                
            move(list2, list1, n-1, actions)
            # give x back
            list1.append(x)
            list2.remove(x)
            if (n%2) == 0:
                actions.remove(-x)
            else:
                actions.remove(x)


listA = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]
listB = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]

move(listA,listB,4,final)

answer1 = list(set(answer))
print(len(answer1))
