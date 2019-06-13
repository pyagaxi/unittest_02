# -*- coding:utf-8 -*-
import math
from datetime import datetime, timedelta
import pytz
import arrow

def in_range(v, base, percent):
    return math.fabs((v - base) / base) * 100 <= percent

def timel():
    """定义返回周几"""

    today = datetime.now(time_zone())

    number = today.weekday() # 定义今天周几，0，1，2，3，4
    this_week_start = arrow.now('Asia/Shanghai').floor('week').datetime
    this_week_end = this_week_start + arrow.arrow.timedelta(days=2)
    month_number = today.day
    return number, this_week_start, this_week_end, month_number


def time_zone():

    tz = pytz.timezone('Asia/Shanghai')

    # return tz

def run_time():

    tz = pytz.timezone('Asia/Shanghai')
    today = datetime.now(tz)
    run_time = datetime(today.year, today.month, today.day, 17, 10, 0).replace(tzinfo=tz)
    return today, run_time


def run_time_():
    today = datetime.today()
    # yesterday = today - timedelta(days=1)
    week = today.weekday()
    secondtime = datetime(today.year, today.month, today.day, 10, 0, 0)
    return today, secondtime, week

def time():
    times = [
        arrow.now().datetime,
        arrow.now().floor('day').datetime + timedelta(hours=1),
        arrow.now().floor('day').datetime + timedelta(hours=12),
        arrow.now().floor('day').datetime + timedelta(hours=9),
        arrow.now().floor('day').datetime + timedelta(hours=17, minutes=30),
        arrow.now().floor('day').datetime + timedelta(hours=10, minutes=20)]
    return times


if __name__ == '__main__':
    # unittest.main()
    # timel()
    # time_zone()
    # run_time()
    # run_time_()
    time()