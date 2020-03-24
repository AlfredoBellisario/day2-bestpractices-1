class Birds:
    def __init__(self):
        '''Constructor for Birds.'''
        self.members = ['Eagle','More eagles','Dragon']

    def printMembers(self):
        print('Printing members')
        for member in self.members:
            print('\t {}'.format(member))
