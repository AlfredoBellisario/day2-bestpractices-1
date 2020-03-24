class Birds:
    def __init__(self):
        '''Constructor for Birds.'''
        self.members = ['Canary', 'Turkey', 'Chicken']

    def printMembers(self):
        print('Printing members')
        for member in self.members:
            print('\t {}'.format(member))
