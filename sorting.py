# Insertion sort

def bubbleSort(list):
    print(f"Bubble sort => {list}")
    
    steps = 0
    isSorted = False
    while not isSorted:
        isSorted = True
        for i in range(len(list)-1):
            steps += 1
            if list[i] > list[i+1]:
                swap(list, i, i+1)
                isSorted = False
        print(list)
    print(steps)
        
def selectionSort(list):
    print(f"Selection sort => {list}")
    
    steps = 0
    for j in range(len(list)):
        indexOfSmallest = j
        for i in range(j, len(list)):
            steps += 1
            if list[i] < list[indexOfSmallest]:
                indexOfSmallest = i
        swap(list, indexOfSmallest, j)
        print(list)
    print(steps)
        
def insertionSort(list):
    print(f"Insertion sort => {list}")

    steps = 0
    for i in range(1, len(list)-1):
        for j in range(i, -1, -1):
            steps += 1
            if list[j] > list[j+1]:
                swap(list, j, j+1)
            else:
                break
        print(list)
    print(steps)
        
                
def swap(list, index1, index2):
    temp = list[index1]
    list[index1] = list[index2]
    list[index2] = temp

def test():
    ''' Test the sorting algorithms '''
    
    #list = [54, 26, 93, 17, 77, 31, 44, 55, 20, 9, 6]
    list =  [1,2,3,4,5,6,7,8,9,10]
    bubbleSort(list)

    #list = [54, 26, 93, 17, 77, 31, 44, 55, 20, 9, 6]
    list =  [1,2,3,4,5,6,7,8,9,10]
    selectionSort(list)

    #list = [54, 26, 93, 17, 77, 31, 44, 55, 20, 9, 6]
    list =  [1,2,3,4,5,6,7,8,9,10]
    insertionSort(list)
    
test()
