numbers = [1,2,3,4,5,6,7,8,9,10]
names = ["Ana","Mario", "John", "Carl"]
years = [2003,2025]

for number in numbers:
    print(number)


odd = 0
for i in range(1, 11, 2):
    odd += i
print(odd)


for i in range(10, 0, -1):
    print(i)


multiplication_table_number = int(input("Type a number for table: "))
for i in range(1, 11):
    result = multiplication_table_number * i
    print(f"{multiplication_table_number} x {i} = {result}")    