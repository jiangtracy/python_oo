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
        self.offset = -1

    def generate(self):
        '''Generate a new serial number that's next in sequence'''

        self.offset += 1
        return self.start + self.offset
    
    def reset(self):
        '''Reset serial number sequece back to start number'''
        self.offset = -1
    