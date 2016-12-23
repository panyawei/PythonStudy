# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        模块1
# Purpose:
#
# Author:      潘先生
#
# Created:     22/12/2016
# Copyright:   (c) 潘先生 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Student:
    count = 0
    sumage = 0
##    marks = ['chinese','math','english']
    def __init__(self,name,age,marks):
        Student.count += 1
        self.name = name
        self.age = age
        self.marks = marks
        Student.sumage += age
    def get_Name(self):
        print 'Name:"%s"' % self.name

    def get_Age(self):
        print 'Age:"%d"' % self.age

    def getMaxCourse(self):
        print sorted(self.marks)[2]

    def getAverageAge(self):
        if Student.count == 0:
            print 'AverageAge:"%d"' % self.age
        else:
            print 'AverageAge:"%d"' % (Student.sumage/Student.count)

zm = Student('ZhangMing',20,[69,88,92])
lm = Student('LiMing',21,[90,89,100])
ww = Student('WangWu',22,[89,81,90])

members = [zm,lm,ww]
for member in members:
    member.getAverageAge(),member.get_Name(),member.get_Age(),member.getMaxCourse()



