class Rectangle:
    def __init__(self, x1=None, x2=None, y1=None, y2=None):
        if x1 is not None :
            self.__myX__ = float(x1)
        else:
            self.__myX__ = 0
        if y1 is not None:
            self.__myY__ = float(y1)
        else:
            self.__myY__ = 0
        if x2 is not None and x1 is not None:
            self.__myWidth__ = abs(float(x2) - float(x1))
        else:
            self.__myWidth__ = 0
        if y2 is not None and x2 is not None:
            self.__myHeight__ = abs(float(y2) - float(y1))
        else:
            self.__myHeight__ = 0

    def getPerimeter(self):
        return abs(2 * self.__myHeight__ + 2 * self.__myWidth__)

    def getArea(self):
        return abs(self.__myWidth__ * self.__myHeight__)