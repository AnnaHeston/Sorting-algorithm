def annaSort (annalist):
    inorder = False #starting out not in order
    while not inorder:
        for num in range(len(annalist)-1, 0, -1): #[for any number in the index up until the index runs out so I don't exceed it
            for i in range(num): #for any number in the range defined above, so it makes multiple passes
                if annalist[i] > annalist[i+1]: #if the number is bigger than the one next to it
                    inorder = False #it's not in order 
                    temp = annalist[i] 
                    annalist[i] = annalist[i+1]
                    annalist[i+1] = temp #switch the order
                elif annalist[i] < annalist[i+1]:#but if they are in the right places
                    inorder = True #don't switch 
    return annalist#return the result
annalist = [67, 45, 2, 13, 1, 998]
annaSort(annalist)
print(annalist)

