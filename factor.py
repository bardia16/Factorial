#made by Bardia Khalafi
'''
Factorial In Python3
'''
class Fac():
    '''
    this is our factorial class
    '''
    def __init__(self, num):
        '''
        this will make variable for our program
        '''
        self.num = num


    def facy(self, number):
        '''
        this method will make calculate factorial of a number of us
        '''
        return 1 if number == 1 else self.facy(number-1)*number


    def __repr__(self):
        return str(self.facy(self.num))


    def __str__(self):
        return str(self.facy(self.num))


    def __add__(self, other):
        return self.facy(self.num) + other.facy(other.num)


    def __sub__(self, other):
        return self.facy(self.num) - other.facy(other.num)


    def __mul__(self, other):
        return self.facy(self.num) * other.facy(other.num)


    def __mod__(self, other):
        return self.facy(self.num) % other.facy(other.num)


    def __floordiv__(self, other):
        return self.facy(self.num) // other.facy(other.num)


    def __truediv__(self, other):
        return self.facy(self.num) / other.facy(other.num)


    def __lt__(self, other):
        return self.facy(self.num) < other.facy(other.num)


    def __le__(self, other):
        return self.facy(self.num) <= other.facy(other.num)


    def __gt__(self, other):
        return self.facy(self.num) > other.facy(other.num)


    def __ge__(self, other):
        return self.facy(self.num) >= other.facy(other.num)


    def __eq__(self, other):
        return self.facy(self.num) == other.facy(other.num)


    def __ne__(self, other):
        return self.facy(self.num) != other.facy(other.num)


if __name__ == "__main__":
    Number_Input = int(input("Please enter our number : "))
    print(Fac(Number_Input))
    input("Please press enter to exit ")
