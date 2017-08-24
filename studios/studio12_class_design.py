# Design Problems
class Rectangle:
    # A rectangle has a length and a width.
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # A rectangle should be able to provide its area and perimeter.
    def area(self):
        return self.length * self.width

    def perimeter(self):
        return (self.length + self.width) * 2

    # A rectangle can indicate whether it is smaller than another rectangle in terms of area.
    def is_smaller(self, other):
        return self.area() < other.area()

    # A rectangle can indicate whether it is in fact a square.
    def is_square(self):
        return self.length == self.width

    def __repr__(self):
        return str(self.length) + "x" + str(self.width)

    def get_length(self):
        return (self.length)

    def get_width(self):
        return (self.width)

    def test(self, other):
        test_str = "Rectangle:\t" + str(self) + "\t|\t" + str(other) + \
            "\nArea:\t\t" + \
            str(self.area()) + "\t|\t" + str(other.area()) + \
            "\nPerimeter:\t" + \
            str(self.perimeter()) + "\t|\t" + str(other.perimeter()) + \
            "\nSmaller:\t" + \
            str(self.is_smaller(other)) + "\t|\t" + str(other.is_smaller(self)) + \
            "\nIs square:\t" + \
            str(self.is_square()) + "\t|\t" + str(other.is_square()) + \
            "\n"
        return test_str


class Fraction:
    '''
    A fraction has a numerator and denominator.
    A fraction should be able to add itself to another fraction, returning a new fraction that represents the sum.
    A fraction should be able to multiply itself by another fraction, returning a new fraction as the product.
    A fraction should be able to take the reciprocal of itself, returning that value as a new fraction.
    A fraction should be able to simplify itself, returning a new fraction as that simplification.'
    '''

    def __init__(self, num, den):
        self.num = num
        self.den = den

    def get_num(self):
        return self.num

    def get_den(self):
        return self.den

    def __repr__(self):
        return str(self.num) + "/" + str(self.den)

    def add(self, other):
        if self.den != other.den:
            new_den = self.den * other.den
            new_num = (self.num * other.den) + (other.num * self.den)
        else:
            new_num = self.num + other.num
            new_den = self.den
        return Fraction(new_num, new_den).simplify()

    def multiply(self, other):
        new_den = self.den * other.den
        new_num = self.num * other.num
        return Fraction(new_num, new_den).simplify()

    def recip(self):
        return Fraction(self.den, self.num).simplify()

    def simplify(self):
        numerator = self.num
        denominator = self.den
        while numerator % denominator != 0:
            old_num = numerator
            old_den = denominator
            numerator = old_den
            denominator = old_num % old_den
        gcd = denominator
        self.num = self.num // gcd
        self.den = self.den // gcd
        return Fraction(self.num, self.den)

    def test(self, other):
        test_str = "Fraction:\t" + \
            str(Fraction(self.num, self.den).simplify()) + "\t|\t" + str(Fraction(other.num, other.den).simplify()) + \
            "\nAdd:\t\t" + str(self.add(other)) + \
            "\nMultiply:\t" + str(self.multiply(other)) + \
            "\nReciprocal:\t" + \
            str(self.recip()) + "\t|\t" + str(other.recip()) + \
            "\n"
        return test_str


class BaseballPlayer:
    '''
    A baseball player has a name and a jersey number.
    Most players hit either right or left, but some can hit either way.
    This object should be able to react when a player completes a game, recording how many hits and RBIs the player earned in that game.
    A player has a certain number of runs and RBIs he or she has recorded over all games played.
    A player has a certain number of games he or she has played.
    '''

    def __init__(self, name, jersey_number, handed):
        self.name = name
        self.jersey_number = jersey_number
        self.handed = handed
        self.total_hits = 0
        self.total_rbis = 0
        self.total_runs = 0
        self.total_games = 0

    def complete_a_game(self, hits, rbis, runs):
        self.total_hits += hits
        self.total_rbis += rbis
        self.total_runs += runs
        self.total_games += 1

    def __repr__(self):
        default_str = self.name + \
            ' (#' + str(self.jersey_number) + ', ' + self.handed + ')' + \
            '\nHits:\t' + str(self.total_hits) + \
            '\nRBIs:\t' + str(self.total_rbis) + \
            '\nRuns:\t' + str(self.total_runs) + \
            '\nGames:\t' + str(self.total_games) + \
            '\n'
        return default_str


# Bonus Missions

class Student:
    '''
    A student has a name and student ID number.
    A student can record grades and will track how many credits they have taken as well as their GPA.
    A student can also report what their class standing is (Freshman, Sophomore, Junior, Senior, Graduated) based on the number of credits they have taken.
    '''
    # def __init__


class Course:
    '''
    A course has a name and course number.
    A course has a certain number of seats - once those seats are filled, it is not possible for anyone else to take the course.
    A course has a roster of students (use your student object!).
    A course can add a student (if there are open seats) or drop a student.
    A course can report the average GPA of all students currently enrolled in the course.
    '''
    # def __init__


def rectangle_test():
    r1 = Rectangle(20, 40)
    r2 = Rectangle(30, 30)
    print(r1.test(r2))


def fraction_test():
    f1 = Fraction(3, 4)
    f2 = Fraction(8, 5)
    print(f1.test(f2))


def baseball_test():
    jackie = BaseballPlayer('Jackie Robinson', 42, 'right')
    print(jackie)
    albert = BaseballPlayer('Albert Pujols', 5, 'right')
    print(albert)
    mark = BaseballPlayer('Mark McGuire', 25, 'left')
    print(mark)
    albert.complete_a_game(3, 2, 1)
    mark.complete_a_game(1, 3, 1)
    albert.complete_a_game(3, 2, 1)
    mark.complete_a_game(2, 3, 2)
    print(albert)
    print(mark)


def main():
    # rectangle_test()
    fraction_test()
    # baseball_test()


if __name__ == '__main__':
    main()
