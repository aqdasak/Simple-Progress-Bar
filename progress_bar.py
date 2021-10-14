from math import ceil

class ProgressBar:
    def __init__(self, bar_length=35):
        self.__bar_length = bar_length
        self.__total = None
        self.__multiplier=0

    @property
    def total(self):
        return self.__total

    @total.setter
    def total(self, total):
        if self.__total is not None:
            raise Exception('total already set')

        self.__total = total
        self.__multiplier = self.__bar_length/total

    def update(self, current, msg=''):
        if self.__total is None:
                raise Exception('total not set')

        length = ceil(self.__multiplier*current)
        if length > self.__bar_length:
            length = self.__bar_length
    
        if current > self.total:
            msg='(!) Received more than expected. ' + msg

        print('\r',current * 100 // self.total, '% ',sep='', end='')
        progress_str = '\r\t'+'\b'*3 + '[' + '#'*length + ' '*(self.__bar_length-length) + ']' + msg
        print(progress_str, end='')

