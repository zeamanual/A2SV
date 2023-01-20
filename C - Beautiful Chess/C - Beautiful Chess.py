test_cases = int(input())
 
for i in range(test_cases):
    matrics = [[0 for j in range(8)] for i in range(8)]
    input()
    for row in range(8):
        row_ele=input()
        for col in range(8):
            matrics[row][col]=row_ele[col]
    
    # print('matrics is ',matrics)
 
    result=''
 
    for row in range(8):
        for col in range(8):
            if((row>0 and row<7 and col>0 and col <7) and matrics[row][col]=='#'):
                if( matrics[row-1][col-1]=='#' and  matrics[row+1][col+1]=='#' and
                matrics[row-1][col+1]=='#' and matrics[row+1][col-1]=='#'   ):
                    
                    result+=f'{row+1} {col+1}'
 
                    break
    print(result)
