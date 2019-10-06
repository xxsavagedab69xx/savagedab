import math

""" A collection of methods for dealing with triangles specified by the length
    of three sides (a, b, c)

    If the sides cannot form a triangle,then return None for the value

"""

# @TODO - add the errlog method and use wolf fencing to identify the errors in this code

def validate_triangle(sides):
    """
    This method should return True if and only if the sides form a valid triangle
        Given three side lengths, the sum of smallest two should be greater than longest sides

    :param sides: a tuple with side lengths
    :return: True if sides form a triangle, False otherwise
    """
    if len(sides) == 3:
        if(sides[0] + sides[1]) > sides[2]:
            return True
        elif (sides[1] + sides[2]) < sides[0]:
            return True
        elif (sides[0] + sides[2]) < sides[1]:
            return True
        elif (sides[0] + sides[1] == sides[2]):
            return True
        else:
            return False

def get_angle(sides):
    """
    Returns the angle C defined for the triangle defined by side lengths (a, b, c)
    first value in the tuple point
    :param sides: a tuple with 3 side lengths
    :return: the angle (in radians) of the angle opposite side c; return None if invalid
    """
    # Using the law of cosines
    #  c^2 = a^2 + b^2 - 2abcos(C)
    #  cos(C) = (a^2 + b^2 - c^2)/(2ab)
    if not validate_triangle(sides):
        return None
    a = sides[0]
    b = sides[1]
    c = sides[2]

    num = math.pow(a, 2) + math.pow(b, 2) - math.pow(c, 2)
    den = 2*a*b

    val = num/den

    angle = math.acos(val)

    return angle

def get_height(sides):
    """
    Returns the height of triangle defined by side lengths (a, b, c)

    Given angle C between sides a & b, the height h from side b to vertex of a and c is
    given by sin(C) = h/a so that h = a*sin(C)
       /|\
      / | \
    a/  |  \ c
    / C |h  \
   /____|____\
         b
    :param sides:
    :return: height from b side to a-c vertex; None if invalid sides
    """
    if not validate_triangle(sides):
        return None
    c = get_angle(sides)  # angle formed by sides a and b, opposite side c
    height = sides[0]*math.sin(c)
    return height

def get_area(sides):
    """
    Returns the area of triangle defined by side lengths (a, b, c)
    :param sides:
    :return: area
    """
    if not validate_triangle(sides):
        return None
    base = sides[1]
    height = get_height(sides)
    area = (1/2)*base*height
    return area

def get_area_heron(sides):
    """
    Returns the area of triangle defined by side lengths (a, b, c)
    using https://www.mathsisfun.com/geometry/herons-formula.html

    This method is intended to be correct to assist you in debugging other methods

    :param sides:
    :return: area
    """
    if not validate_triangle(sides):
        return None

    a = sides[0]
    b = sides[1]
    c = sides[2]
    s = 0.5*(a + b + c)
    area = math.sqrt(s*((s-a)*(s-b)*(s-c)))
    return area

print('name is', __name__)
if __name__ == "__main__":
    sides = (3, 4, 5)
    areaHeron = get_area_heron(sides) # This should be 6.0
    area = get_area(sides)
    print('Area of triangle with sides={} is {} {}'.format(str(sides), str(area), str(areaHeron)))

    sides = (4, 5, 3)
    areaHeron = get_area_heron(sides)  # This should be 6.0 (same as 3,4,5)
    area = get_area(sides)
    print('Area of triangle with sides={} is {} {}'.format(str(sides), str(area), str(areaHeron)))

    sides = (2, 2, 2*math.sqrt(2))  # equilateral right triangle
    areaHeron = get_area_heron(sides)  # This should be 2.0
    area = get_area(sides)
    print('Area of triangle with sides={} is {} {}'.format(str(sides), str(area), str(areaHeron)))

    sides = (4, 4, 5)  # This is an invalid triangle
    areaHeron = get_area_heron(sides)  #
    area = get_area(sides)
    print('Area of triangle with sides={} is {} {}'.format(str(sides), str(area), str(areaHeron)))

    sides = (3, 4, 8)  # This is an invalid triangle
    areaHeron = get_area_heron(sides)  # This should be None
    area = get_area(sides)
    print('Area of triangle with sides={} is {} {}'.format(str(sides), str(area), str(areaHeron)))

    sides = (3, 4)  # This is an invalid triangle
    areaHeron = get_area_heron(sides) # This should be None
    area = get_area(sides)
    print('Area of triangle with sides={} is {} {}'.format(str(sides), str(area), str(areaHeron)))
