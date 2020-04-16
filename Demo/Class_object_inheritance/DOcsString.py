class CollegeStudent():
    """
    Blueprint for a student at an institution of higher learning

    """
    def __init__(self):
        pass

    def sleep(self):
        """
        Sleep through class
        """
    def eat(self):
        """
        Go to the cafeteria

        """
    def party(self):
        """
        Hit the books hard

        """
print(CollegeStudent.__doc__)

mart = CollegeStudent()
print(mart.sleep.__doc__) # Sleep through class
print(mart.eat.__doc__)   # Go to the cafeteria
print(mart.party.__doc__) # Hit the books har



