#  Python

def calculate_rectangle_are(width, height):
    area = width * height
    return area

def calc_triangle_area (height, base):
    area = (height * base) / 2
    return area

def main():
    print("This is our shapes program")
    rectangle_area = calculate_rectangle_are(10, 20)
    print(f'the area of my rectangle is : {rectangle_area}')
    triangle_area = calc_triangle_area(10, 20)
    print(f'the area of my triangle is : {triangle_area}')

main()