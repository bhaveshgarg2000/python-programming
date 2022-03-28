# statement1= int(input('Does the statement require reliable backup and recovery?'))
# while(statement1>5):
#     print('invalid')
#     statement1= int(input('Does the statement require reliable backup and recovery?'))
# else:
#     print('accepted')
# statement2= int(input('Is data communication required?'))
# while(statement1>5):
#     print('invalid')
#     statement2= int(input('Is data communication required?'))
# else:
#     print('accepted')
# statement3= int(input('are there distributed processing functions?'))
# while(statement1>5):
#     print('invalid')
#     statement3= int(input('are there distributed processing functions?'))
# else:
#     print('accepted')
# statement4= int(input('is performance critical?'))
# while(statement1>5):
#     print('invalid')
#     statement4= int(input('is performance critical?'))
# else:
#     print('accepted')
# statement5= int(input('will the system run in a heavily utilized operational environment?'))
# while(statement1>5):
#     print('invalid')
#     statement5= int(input('will the system run in a heavily utilized operational environment?'))
# else:
#     print('accepted')
# statement6= int(input('does the system require in line data entry?'))
# while(statement1>5):
#     print('invalid')
#     statement6= int(input('does the system require in line data entry?'))
# else:
#     print('accepted')
# statement7= int(input('does the on line data entry require the input transaction to be built over multiple screens or operation?'))
# while(statement1>5):
#     print('invalid')
#     statement7= int(input('does the on line data entry require the input transaction to be built over multiple screens or operation?'))
# else:
#     print('accepted')
# statement8= int(input('are the master files updated on line?'))
# while(statement1>5):
#     print('invalid')
#     statement8= int(input('are the master files updated on line?'))
# else:
#     print('accepted')
# statement9= int(input('is the inputs, output, files, or inquiress complex?'))
# while(statement1>5):
#     print('invalid')
#     statement9= int(input('is the inputs, output, files, or inquiress complex?'))
# else:
#     print('accepted')
# statement10= int(input('is the internal processing complex?'))
# while(statement1>5):
#     print('invalid')
#     statement10= int(input('is the internal processing complex?'))
# else:
#     print('accepted')
# statement11= int(input('is the code designed to be reausable ?'))
# while(statement1>5):
#     print('invalid')
#     statement11= int(input('is the code designed to be reausable ?'))
# else:
#     print('accepted')
# statement12= int(input('are conversion and installation include in the design?'))
# while(statement1>5):
#     print('invalid')
#     statement12= int(input('are conversion and installation include in the design?'))
# else:
#     print('accepted')
# statement13= int(input('is the system designed for multiple installation in different organisation?'))
# while(statement1>5):
#     print('invalid')
#     statement13= int(input('is the system designed for multiple installation in different organisation?'))
# else:
#     print('accepted')
# statement14= int(input('is the application designed to facilitate change and ease of use by the user?'))
# while(statement1>5):
#     print('invalid')
#     statement14= int(input('is the application designed to facilitate change and ease of use by the user?'))
# else:
#     print('accepted')
#
# sum= statement1+statement2+statement3+statement4+statement5+statement6+statement7+statement8+statement9+statement10+statement11+statement12+statement13+statement14
# CAF= 0.65+(0.01*sum)
# print("CAF :",CAF)










externalInput = [int(input("Low : "))*3, int(input("Avg :  "))
                 * 4, int(input("High : "))*6]
externalOutput = [int(input("Low "))*4, int(input("Avg : "))
                  * 5, int(input("High "))*7]
externalEng = [int(input("Low :  "))*3, int(input("Avg :  "))
               * 4, int(input("High :  "))*6]
internalLogicalFiles = [
    int(input("Low : "))*7, int(input("Avg : "))*10, int(input("High : "))*15]
internalInterfaceFiles = [
    int(input("Low : "))*5, int(input("Avg : "))*7, int(input("High : "))*10]

externalInputsAgg = externalOutputAgg = externalEngAgg = internalLogicalFilesAgg = internalInterfaceFilesAgg = 0

for i in range(0, 3):
    externalInputsAgg = externalInput[i] + externalInputsAgg

for i in range(0, 3):
    externalOutputAgg = externalOutput[i] + externalOutputAgg

for i in range(0, 3):
    externalEngAgg = externalEng[i] + externalEngAgg

for i in range(0, 3):
    internalLogicalFilesAgg = internalLogicalFiles[i] + internalLogicalFilesAgg

for i in range(0, 3):
    internalInterfaceFilesAgg = internalInterfaceFiles[i] + internalInterfaceFilesAgg

print("Total External Input : ", externalInputsAgg)
print("Total External Output : ", externalOutputAgg)
print("Total External Eng : ", externalEngAgg)
print("Total Internal Logical Files : ", internalLogicalFilesAgg)
print("Total Internal Interface Files : ", internalInterfaceFilesAgg)
UFP= externalInputsAgg+externalOutputAgg+externalEngAgg+internalLogicalFilesAgg+internalInterfaceFilesAgg
print('The UFP value : ',UFP)

value= int(input('This value will be entered all 14 question : '))
Fi= value*14
CAF=(0.65+ 0.01*Fi)
print('The CAF value : ',CAF)
FP= UFP*CAF
print('value of FP : ',FP)