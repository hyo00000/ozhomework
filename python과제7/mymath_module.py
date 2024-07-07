
#삼각형의 넓이
def number_a():
    base = input("삼각형의 밑변의 길이를 입력해주세요")
    return float(base)

def number_b():
    height = input("삼각형의 높이를 입력해주세요")
    return float(height)

def get_triangle(area):
    return (number_a * number_b)/ 2

#원의 넓이
pi = 3.141592
def number_input():
    value = input("반지름을 입력해주세요")
    return float(value)

def get_circle(radius):
    return pi * radius * radius

#직육면체의 넓이
def number_c():
    width = input("직육면체 가로의 길이를 입력해주세요")
    return float(width)

def number_d():
    length = input("직육면체 세로의 길이를 입력해주세요")
    return float(length)

def get_rectangular(area):
    return (number_c * number_d) * 6