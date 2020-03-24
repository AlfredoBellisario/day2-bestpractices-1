class Mammals:
    def __init__(self):
        '''Constructor for Mammals.'''
        self.members = ['Zebra', 'Platypus', 'Dolphin']
    def printMembers(self):
        print('Printing members')
        for member in self.members:
            print('\t {}'.format(member))
