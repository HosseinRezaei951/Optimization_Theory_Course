import os, sys
import numpy as np

############################################################
### GLOBAL STRINGS
############################################################
# for main program panel 
PANEL_MESSAGE =             "\t1- Hadamard Product\n"+\
                            "\t2- Kronecker Product\n"+\
                            "\t3- Khatri–Rao Product\n"+\
                            "\t0- Exit "
                            
SWITCH_MESSAGE =            "\n Plz select function number and press enter: "
EMPTY_INPUT =               "\n Empty input !!!"
INVALID_MESSAGE =           "\n Invalid input !!!"
RETURN_MESSAGE =            "\n Press any key to return panel ..."
TRY_AGAIN_MESSAGE =         "\n Press any key to try again ..."
EXIT_MESSAGE =              "<or 0 for exit>"


############################################################
### clear_screen
############################################################
def clear_screen():
    '''
    Code to clear running screen
    '''    
    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # for windows platfrom
        _ = os.system('cls')


############################################################
### Load Matrix
############################################################
def loadMatrix():
    '''
    Code to loading matrix from .txt file
        example:
            1 2 3
            4 5 6
            7 8 9
    ''' 
    mat = None
    Exit = False
    while Exit != True:
        try:
            filePath = input("\nPlz enter Matrix filePath: ")
            mat = np.loadtxt(filePath, dtype=int)
            Exit = True
        except:
            input("Invalid input ... press enter to try again.")
    return mat


############################################################
### Hadamard Product
############################################################
def hadamardProduct(mat1, mat2):
    resultMat = None
    if mat1.shape != mat2.shape:
        print("\n ==> Error: Dimensions of first matrix and second matrix isn\'t equal.")
    else:
        nrow, ncol = mat1.shape         
        resultMat = np.empty((0, ncol)) 
        for i in range(nrow):
            tmp_row = np.empty((1, 0))
            for j in range(ncol):
                matElement = np.array([[mat1[i][j] * mat2[i][j]]])
                tmp_row = np.concatenate((tmp_row, matElement), axis=1)
            resultMat = np.concatenate((resultMat, tmp_row))           
    return resultMat


############################################################
### Kronecker Product
############################################################
def kroneckerProduct(mat1, mat2):
    resultMat = None
    nrow, ncol = tuple(l * r for l, r in zip(mat1.shape, mat2.shape))
    resultMat = np.empty((0, ncol))
    nrow1, ncol1 = mat1.shape
    nrow2, ncol2 = mat2.shape
    for i in range(nrow1):
        tmp_row = np.empty((nrow2, 0))
        for j in range(ncol1):
            tmpMat = np.full(mat2.shape, mat1[i][j])
            tmp_colMat = hadamardProduct(tmpMat, mat2)
            tmp_row = np.concatenate((tmp_row, tmp_colMat), axis=1)
        resultMat = np.concatenate((resultMat, tmp_row))
    return resultMat


############################################################
### Khatri–Rao Product
############################################################
def KhatriRaoProduct(mat1, mat2):
    resultMat = None
    if mat1.shape[1] != mat2.shape[1]:
        print("\n ==> Error: numeber of columns in first matrix and second matrix isn\'t equal")
    else:
        nrow1, ncol1 = mat1.shape
        nrow2, ncol2 = mat2.shape
        resultMat = np.empty((nrow1*nrow2, 0))
        for j in range(ncol1):
            colMat = kroneckerProduct(np.array([mat1[:,j]]).T, np.array([mat2[:,j]]).T)
            resultMat = np.concatenate((resultMat, colMat), axis=1)
        resultMat = resultMat
    return resultMat


############################################################
### SWITCH CLASS
############################################################ 
class Switch(object):
    ''' 
        Switch class: it represents switching between parts of panel.
    '''

    def select(self, i):
        ''' 
            Get a number and represents part of panel .
            Parameters: i - type: string - a number that used to select one part of the panel.
        ''' 
        method_name = 'number_' + str(i)
        method = getattr(self, method_name, lambda :input(INVALID_MESSAGE + RETURN_MESSAGE))
        return method()


    '''
    <Each method of this class represents one part of panel. And any of them help user 
     to get inputs and doing some thing.>
    '''
    def number_1(self):
        clear_screen()
        print("\n\t *** Hadamard Product ***")

        print("\n==>Loading first matrix: ")
        mat1 = loadMatrix()

        print("\n==>Loading second matrix: ")
        mat2 = loadMatrix()

        print("\nFirst matrix: \n", mat1)            
        print("\nSecond matrix: \n", mat2)
        
        resultMat = hadamardProduct(mat1, mat2)
        print("\nResult matrix of first matrix and second matrix «Hadamard Product»: \n", resultMat)

        return input(RETURN_MESSAGE)


    def number_2(self):
        clear_screen()
        print("\n\t *** Kronecker Product ***")

        print("\n==>Loading first matrix: ")
        mat1 = loadMatrix()

        print("\n==>Loading second matrix: ")
        mat2 = loadMatrix()

        print("\nFirst matrix: \n", mat1)            
        print("\nSecond matrix: \n", mat2)
        
        resultMat = kroneckerProduct(mat1, mat2)
        print("\nResult matrix of first matrix and second matrix Kronecker Product»: \n", resultMat)
        
        return input(RETURN_MESSAGE)


    def number_3(self):
        clear_screen()
        print("\n\t *** Khatri–Rao Product ***")

        print("\n==>Loading first matrix: ")
        mat1 = loadMatrix()

        print("\n==>Loading second matrix: ")
        mat2 = loadMatrix()

        print("\nFirst matrix: \n", mat1)            
        print("\nSecond matrix: \n", mat2)
        
        resultMat = KhatriRaoProduct(mat1, mat2)
        print("\nResult matrix of first matrix and second matrix Khatri–Rao Product»: \n", resultMat)
    
        return input(RETURN_MESSAGE)


############################################################
### __MAIN__
############################################################ 
if __name__ == "__main__":  
    s = Switch()
    while True :
        clear_screen()
        print()
        print(PANEL_MESSAGE)
        switch_input = ""
        switch_input = input(SWITCH_MESSAGE)
        if switch_input == "0":
            clear_screen()
            print("\n\t *** Good Bye ***")
            break
        elif switch_input == "":
                input(EMPTY_INPUT + TRY_AGAIN_MESSAGE)
        else:
            s.select(switch_input)

    