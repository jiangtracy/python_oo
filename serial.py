class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        '''Create a serial number generator starting from start'''

        self.start = start
        self.next = start - 1
    
    def __repr__(self):
        '''Returns the start and next values of the SerialGenerator instance'''

        return f"<SerialGenerator start={self.start} next={self.next + 1}>"


    def generate(self):
        '''Generate a new serial number that's next in sequence'''

        self.next += 1
        return self.next

    def reset(self):
        '''Reset serial number sequece back to start number'''
        self.next = self.start - 1
