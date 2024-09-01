import os, sys
import numpy as np

############################################################
### GLOBAL STRINGS
############################################################
# for main program panel 
PANEL_MESSAGE =             "\t1- Gram-Schmidt Process\n"+\
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
### Load Vector Space
############################################################
def loadVectorSpace():
    VectorSpace = None
    Exit = False
    while Exit != True:
        try:
            filePath = input("\nPlz enter VectorSpace filePath: ")
            VectorSpace = np.loadtxt(filePath, dtype=int)
            Exit = True
        except:
            input("Invalid input ... press enter to try again.")
    return VectorSpace


############################################################
### Gram-Schmidt Process
############################################################
def gramSchmidtProcess(V):
    nrows, ncols = V.shape
    U = np.empty((nrows, 0))
    U = np.concatenate((U, np.array([V[:, 0]]).T), axis=1)
    for k in range(1, ncols):
        vk = np.array([V[:, k]]).T
        for i in range(0, k):
            ui = np.array([U[:, i]]).T
            vk = vk - ((np.dot(vk.T, ui))/(np.dot(ui.T, ui)))*ui
        U = np.concatenate((U, vk), axis=1)
    for j in range(ncols):
        U[:, j] = U[:, j] / np.sqrt(np.dot(np.array([U[:, j]]), np.array([U[:, j]]).T))
    return U


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
        print("\n\t *** Gram-Schmidt Process ***")

        print("\n==>Loading vector space: ")
        VectorSpace = loadVectorSpace()
        nrows, ncols = VectorSpace.shape
        
        V = np.empty((nrows, 0))
        for j in range(ncols):
            print("\nVector" + str(j+1) +": \n", np.array([VectorSpace[:, j]]).T)  
            V = np.concatenate((V, np.array([VectorSpace[:, j]]).T), axis=1)  
        
        V = V.astype(int)

        result = gramSchmidtProcess(V)
        print("\nResult of «Gram-Schmidt Process»: ")
        for j in range(ncols):
            print("\nu" + str(j+1) +": \n", np.array([result[:, j]]).T)
        return input(RETURN_MESSAGE)



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

    