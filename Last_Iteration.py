# Jemmo Joseph (JJ) Calculating mean, median, sample variance, and sample
# standard deviation of user-inputted numbers
import time


def humanverification():
    user = input("Please Enter Your Name:")
    print("Hello " + user, end='! ')
    # is the addition operation for strings. It concatenates strings together
    time.sleep(1)
    print("Before we begin, I must verify that you are a member of this "
          "class.")
    time.sleep(2)
    guess = input("Please enter this class's Course Number or CRN: ")
    while not (not (guess != 80597) or not (guess != 1500)):
        try:
            guess = int(guess)
            if guess == 80597 or guess == 1500:
                print("That is correct!")
                time.sleep(1)
                print("Let's continue.")
                time.sleep(1)
            else:
                while guess != 80597 and guess != 1500:
                    print("That is incorrect. Please Try again.")
                    guess = int(input(
                        "Please enter this class's Course Number or CRN: "))
                print("That is correct!")
                print("Let's continue.")
                time.sleep(1)
        except:
            print("That is incorrect. Please Try again.")
            guess = input("Please enter this class's Course Number or CRN: ")


def intro():
    time.sleep(2)
    print("This program will calculate your 1-variable statistics for you!")
    time.sleep(2)
    countdown_three = int(1.5 * 2)
    # * is the multiplication operation for numbers. It multiplies numbers
    countdown_two = 25 // 9
    # // is the floor division operation. It divides the numbers and only keeps
    # the quotient, not the remainder
    countdown_one = int(11 % 5)
    # % is the modulo division operation. It divides the numbers and only keeps
    # the remainder, not the quotient
    print("Let's begin in:")
    time.sleep(1)
    print(countdown_three)
    time.sleep(1)
    print(countdown_two)
    time.sleep(1)
    print(countdown_one, end='\n' * 2)
    time.sleep(1)
    # * is the multiplication operation for strings. It multiplies and
    # concatenates a string by an integer
    print(
        "Let's input some data! You can only input 7 numbers, but they can be "
        "positive or negative.")
    print(
        "Please be aware that this program does not consider the frequency of "
        "the data.")


def samplevaluesandmedianfinder():
    sample = ["one", "two", "three", "four", "five", "six", "seven"]

    number = float(input("Please Enter Data #1:"))
    sample[0] = number
    largest = number

    number2 = float(input("Please Enter Data #2:"))
    sample[1] = number2
    if not (largest < number2):
        second_largest = number2
    else:
        second_largest = largest
        largest = number2
    number3 = float(input("Please Enter Data #3:"))
    sample[2] = number3
    if number3 >= largest:
        third_largest = second_largest
        second_largest = largest
        largest = number3
    elif second_largest < number3 < largest:
        third_largest = second_largest
        second_largest = number3
    else:
        third_largest = number3
    number4 = float(input("Please Enter Data #4:"))
    sample[3] = number4
    if number4 > third_largest:
        potential_third_largest = number4
        if potential_third_largest > second_largest:
            potential_second_largest = potential_third_largest
            if potential_second_largest > largest:
                fourth_largest = third_largest
                third_largest = second_largest
                second_largest = largest
                largest = potential_second_largest
            else:
                fourth_largest = third_largest
                third_largest = second_largest
                second_largest = potential_second_largest
        else:
            fourth_largest = third_largest
            third_largest = potential_third_largest
    else:
        fourth_largest = number4

    for x in range(4, 7):
        y = str(x + 1)
        number5 = float(input("Please Enter Data #" + y + ":"))
        if number5 > fourth_largest:
            potential_fourth_largest = number5
            if potential_fourth_largest > third_largest:
                potential_third_largest = potential_fourth_largest
                if potential_third_largest > second_largest:
                    potential_second_largest = potential_third_largest
                    if potential_second_largest > largest:
                        fourth_largest = third_largest
                        third_largest = second_largest
                        second_largest = largest
                        largest = potential_second_largest
                    else:
                        fourth_largest = third_largest
                        third_largest = second_largest
                        second_largest = potential_second_largest
                else:
                    fourth_largest = third_largest
                    third_largest = potential_third_largest
            else:
                fourth_largest = potential_fourth_largest
        sample[x] = number5
    median = int(fourth_largest)

    return sample, median


def meancalculator():
    sample, median = samplevaluesandmedianfinder()
    v_one = sample[0]
    v_two = sample[1]
    v_three = sample[2]
    v_four = sample[3]
    v_five = sample[4]
    v_six = sample[5]
    v_seven = sample[6]
    print("Thank you! The program will now give you your results!")
    total = v_one + v_two + v_three + v_four + v_five + v_six + v_seven
    # + is the addition operation for numbers. It adds numbers together
    n = 7.0
    # - is the subtraction operation. It subtracts the second number from the
    # first
    mean = total / n
    # / is the regular division operation. It divides the numbers and keeps
    # the quotient and remainder
    print('The mean of your sample is:', format(mean, '.3f'))
    print("The median of your sample is:", median)
    return v_one, v_two, v_three, v_four, v_five, v_six, v_seven, n, mean


def varianceandstandarddeviationcalculator():
    v_one, v_two, v_three, v_four, v_five, v_six, v_seven, n, mean = \
        meancalculator()
    # The next calculations are the steps needed to find the variance and
    # std dev. Please refer to the formula for variance and standard deviation
    # to understand further
    final_one = v_one - mean
    final_two = v_two - mean
    final_three = v_three - mean
    final_four = v_four - mean
    final_five = v_five - mean
    final_six = v_six - mean
    final_seven = v_seven - mean
    final_one **= 2
    # ** is the exponent operation. It multiplies the first number to itself a
    # certain amount of times stated by the second number
    final_two **= 2
    final_three **= 2
    final_four **= 2
    final_five **= 2
    final_six **= 2
    final_seven **= 2
    final_sum = final_one + final_two + final_three + final_four + final_five \
        + final_six + final_seven
    n -= 1
    variance = final_sum / n
    print("The variance of your sample is:", format(variance, '.0f'))
    std_dev = (variance ** 0.5)
    print("The standard deviation of your sample is", format(std_dev, '.3f'),
          sep=': ')


def main():
    humanverification()
    intro()
    varianceandstandarddeviationcalculator()


main()
