class Fishes:
    def __init__(self):
        '''Constructor for Fishes.'''
        self.members = ['I hate fishes. None is harmless.']
    def printMembers(self):
        print('Printing members')
        for member in self.members:
            print('\t {}'.format(member))
