import random
import os
#this program generates a aleatoy number between 0 and 100


def generate_random_number():
  choose1 = random.randrange(0,100)
  print(choose1)

def start_choose():
    
         input('Type any key to choose a aleatory number between 0 100: ')
         generate_random_number() 


def user_choise():
 while True:
  print('Do you wanna generate another number?')
  user_input = input('Type YES to continue or NO to exit:  ').lower()

  if user_input == 'yes':
    os.system('cls')
    start_choose()
  elif user_input == 'no':
    os.system('cls')
    break
  else:
    input('Invalid answer, please type YES or NO to choose if you wanna continue or not. Press any key again  ')
    os.system('cls')
    
    


    
def main():
    start_choose()
    user_choise()
if __name__ == '__main__':
    main()    

