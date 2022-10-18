
class l1GTl2(Exception):
    pass

class l2GTL1(Exception):
    pass

try:
    list1 = [1, 2, 4]
    list2 = [1, 2, 3]

    if list1 > list2:
        raise l1GTl2 ("List1 is greater than list2")
    if list2 > list1:
        raise l2GTL1 ("List2 is greater than list1")
    if list1 == list2:
        print("Both lists are equal......")


except l1GTl2 as L1:
    print(L1)
except l2GTL1 as L2:
    print(L2)
else:
    print('Both Lists are same!')
finally:
    print('*** Done! ***')