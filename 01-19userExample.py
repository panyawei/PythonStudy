#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      12SigmaTech
#
# Created:     19/01/2017
# Copyright:   (c) 12SigmaTech 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os
def main():

    filename=open('D:/user.txt','w')
    filename.write('userA 111\n')
    filename.write('userB 222\n')
    filename.close()
    lis=[]
    file_object=open('D:/user.txt')
    list_of_all_lines=file_object.readlines()
    for line in list_of_all_lines:
        list_of_all=line.split()
        lis.append(list_of_all)
    print lis




if __name__ == '__main__':
    main()
