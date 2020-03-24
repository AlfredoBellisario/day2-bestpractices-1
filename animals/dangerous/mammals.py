class Mammals:
    def __init__(self):
        '''Constructor for Mammals.'''
        self.members = ['Lion','Tiger','Human']
    def printMembers(self):
        print('Printing members')
        for member in self.members:
            print('\t {}'.format(member))
