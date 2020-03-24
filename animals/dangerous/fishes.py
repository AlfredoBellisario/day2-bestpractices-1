class Fishes:
    def __init__(self):
        '''Constructor for Fishes.'''
        self.members = ['Baby Shark', 'Mama Shark', 'Papa Shark', 'Gradma Shark', 'Grandpa Shark']
    def printMembers(self):
        print('Printing members')
        for member in self.members:
            print('\t {}'.format(member))
