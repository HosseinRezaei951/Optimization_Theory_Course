import numpy as np

filePath = "Data/mat1.txt"
mat1 = np.loadtxt(filePath, dtype=int)
print(mat1)

############################################################
### Making Random Matrix
############################################################
def makeRandomMatrix():
    '''
    Code to making random matrix
    ''' 
    mat = None
    Exit = False
    while Exit != True:
        try:
            numbersRange = input("Plz enter «range of numbers» for matrix seperate by comma(example: 1,10): ")
            numbersRange = numbersRange.split(",")
            numbersRange = [int(x) for x in numbersRange]
            if len(numbersRange) != 2 or numbersRange[0] > numbersRange[1]:
                input("Invalid «range of numbers» ... press enter to try again.")
            else:
                dimensions = input("Plz enter «dimensions» for matrix seperate by comma(example: 3,4): ")
                dimensions = dimensions.split(",")
                dimensions = [int(x) for x in dimensions]
                if len(dimensions) != 2 or dimensions[0] <= 0 or dimensions[1] <= 0:
                    input("Invalid «dimensions» ... press enter to try again.")
                else:
                    mat = np.random.randint(numbersRange[0], numbersRange[1], size=(dimensions[0], dimensions[1]))
                    Exit = True
        except:
            input("Invalid input ... press enter to try again.")
    return mat


# for i in range(nrow1):
    #     tmpMat = np.full(mat2.shape, mat1[i][0])
    #     rowMat = hadamardProduct(tmpMat, mat2)
    #     print("\n rowMat:",rowMat, rowMat.shape)
    #     input()
    #     for j in range(1, ncol1):
    #         tmpMat = np.full(mat2.shape, mat1[i][j])
    #         colMat = hadamardProduct(tmpMat, mat2)
    #         print("\n colMat:",colMat, colMat.shape)
    #         input()
    #         rowMat = np.concatenate((rowMat, colMat), axis=1)
    #         print("\n rowMat:",rowMat, rowMat.shape)
    #         input()
    #     resultMat = np.concatenate((resultMat, rowMat))
    #     print("\n resultMat:",resultMat, resultMat.shape)
    #     input()