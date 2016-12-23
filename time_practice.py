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
import time,calendar
import datetime
def main():
    t = time.time()
    print u'时间戳',t

    datetime = time.localtime(time.time())
    print datetime
    print time.asctime(datetime)
    print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())



def months(dt,months):
    month = dt.month - 1 + months
    year = dt.year + month / 12
    month = month % 12 + 1
    day = min(dt.day,calendar.monthrange(year,month)[1])
    dt = dt.replace(year=year, month=month, day=day)

    return str(dt.replace(year=year, month=month, day=day)).replace('-','')
time_temp = time.strftime("%Y%m%d", time.localtime())
dt=datetime.date(int(time_temp[0:4]), int(time_temp[4:6]), int(time_temp[6:8]))
print u'一个月前的今天是',months(dt,-1)

if __name__ == '__main__':
    main()


