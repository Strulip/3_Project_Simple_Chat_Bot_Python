def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    for x in range(num + 1):
          print(x, '!')


def test():
    print("Let's test your programming knowledge.")
    # write your code here
    print('Completed, have a nice day!')


def end():
    print('Congratulations, have a nice day!')

def user_test():
      print('Why do we use methods?\n'
            '1. To repeat a statement multiple times.\n'
            '2. To decompose a program into several small subroutines.\n'
            '3. To determine the execution time of a program.\n'
            '4. To interrupt the execution of a program.')

      correct_answer = 2

      while True:

            user_answer = input()

            if not user_answer.isdigit():
                  print('Please enter the number')
                  continue

            if int(user_answer) == correct_answer:
                  end()
                  break

            else:
                  print("Please, try again.")

greet('StanAI', '2025')  # change it as you need
remind_name()
guess_age()
count()
user_test()
