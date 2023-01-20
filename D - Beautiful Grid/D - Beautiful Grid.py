test_cases= int(input())
 
for i in range(test_cases):
    size=int(input())
    matr=[[ 0 for i in range(size)] for j in range(size)]
 
    for row in range(size):
        row_ele=input()
        for col in range(size):
            matr[row][col]=int(row_ele[col])
 
    cols=rows=len(matr)-1
 
    count=0
    for row in range(size//2):
        
        for col in range(size-1):
            elements={0:0,1:0}
            elements[matr[0+row][row+col]]+=1
            elements[matr[row+col][cols-row]]+=1
            elements[matr[rows-row][(cols-row)-col]]+=1
            elements[ matr[rows-row-col][0+row]]+=1
 
            count+=min(elements[0],elements[1])
        size-=2
        
    print(count)
