import math
import os
from decimal import Decimal, ROUND_HALF_UP

def area_circle(radius):
 area = Decimal(math.pi * radius ** 2)
 return area.quantize(Decimal("0.00"),ROUND_HALF_UP)


def area_square(side):
  area_square = side **2
  return area_square


def area_triangle(base,height):
    area_triangle = base * height/2
    return area_triangle


def inserting_values():
    while True:
        try:
            radius = int(input("Insert circle's radius:"))
            side = int(input("Insert square's side:"))
            base = int(input("Insert triangle's base: "))
            height = int(input("Insert triangle's height: "))
            print(f"Circle's area: {area_circle(radius)}")
            print(f"Square's area: {area_square(side)}")
            print(f"Triangle's area: {area_triangle(base, height)}")
            break

        except ValueError:
            input("You entered the wrong value, enter any key to return to the beginning")
            os.system('cls') # Clean the screen
            continue # Return to looping

inserting_values()
def addition(num,num1):
    sum =num+num1
    return sum

num = int(input('Digite um número: '))
num1 = int(input('Digite o número a ser somado: '))
resultado_soma = addition(num, num1)
print(resultado_soma)



