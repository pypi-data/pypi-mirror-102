import datetime
from datetime import timedelta

class dtutil(object):
    @classmethod
    def getXdayBefore(n: int, dt=None)->str:
        if point is None:
            dt = datetime.datetime.now()
        if n > 0:
            dt -= datetime.timedelta(days=n)
        else:
            dt += datetime.timedelta(days=-n)
        return dt.strftime('%Y-%m-%d')

    @classmethod
    def getMonday(dt=None)->str:
        if dt is None:
            dt = datetime.date.today() 
        dt += datetime.timedelta(days=-dt.weekday())
        return dt.strftime('%Y-%m-%d')

    @classmethod
    def getNextMonday(dt:None)->str:
        if dt is None:
            dt = datetime.date.today()
        dt += datetime.timedelta(days=7-dt.weekday())
        return dt.strftime('%Y-%m-%d')

    @classmethod
    def getSunday()->str:
        if dt is None:
            dt = datetime.date.today()
        dt += datetime.timedelta(days=-dt.weekday()+6)
        return dt.strftime('%Y-%m-%d')

    @classmethod
    def getStartOfMonth()->str:
        if dt is None:
            dt = datetime.date.today()
        dt = datetime.datetime(dt.year, dt.month, 1)
        return dt.strftime('%Y-%m-%d')

    @classmethod
    def getStartOfNextMonth()->str:
        if dt is None:
            dt = datetime.date.today()
        dt = datetime.datetime(dt.year, dt.month, 1) + datetime.timedelta(days=calendar.monthrange(dt.year, dt.month)[1])
        return dt.strftime('%Y-%m-%d')

    @classmethod
    def getEndOfMonth()->str:
        if dt is None:
            dt = datetime.date.today()
        dt = datetime.datetime(dt.year, dt.month, calendar.monthrange(dt.year, dt.month)[1])
        return dt.strftime('%Y-%m-%d')