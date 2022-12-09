__author__ = "Jemmo Joseph(JJ)"
# Calculating mean, median, sample variance, and sample
# standard deviation of user-inputted numbers
import time
import math


def human_verification():
    """
    This function verifies if the user is a student in this class.
    """
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
        except ValueError:
            print("That is incorrect. Please Try again.")
            guess = input("Please enter this class's Course Number or CRN: ")


def intro():
    """This function only displays an introduction."""
    time.sleep(1)
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
        "Let's input some data! You can input as many numbers as you'd like, "
        "and they can be positive or negative.")
    print(
        "Please be aware that this program does not consider the frequency of "
        "the data.")


def data_input(sampledata):
    """
    This function takes inputs and adds them to a list.

    Parameters:
        sampledata (sampledata): An empty list that'll have inputs added to it.

    Returns:
        sampledata: A list filled with float number inputs from the user.
    """
    junk1 = 0
    while junk1 < 2:
        try:
            value = float(
                input("Please Enter Data #" + (str(junk1 + 1)) + ":"))
            # + is the addition operation for numbers. It adds numbers together
            sampledata.append(value)
            junk1 += 1
        except ValueError:
            print("Invalid input. Please try again.")
    print("Whenever you are done inputting data, just write the word 'STOP'. ")
    new_value = 0
    loop = True
    mini_loop = True
    while mini_loop:
        new_value = (input("Please Enter Data #3:"))
        new_value = new_value.replace(" ", "")
        new_value = new_value.lower()
        try:
            new_value = float(new_value)
            mini_loop = False
        except ValueError:
            if new_value != "stop":
                print("Invalid input. Please try again.")
            else:
                mini_loop = False
                loop = False

    while loop:
        try:
            while new_value != "stop":
                new_value = float(new_value)
                sampledata.append(new_value)
                junk1 += 1
                new_value = input(
                    "Please Enter Data #" + (str(junk1 + 1)) + ":")
                new_value = new_value.replace(" ", "")
                new_value = new_value.lower()
            loop = False

        except ValueError:
            print("Invalid input. Please try again.")
            new_value = input("Please Enter Data #" + (str(junk1 + 1)) + ":")
            loop = True
    return sampledata


def get_median(data_list):
    """
    This function finds the median in a list.

    Parameters:
        data_list (median): The list filled with float numbers

    Returns:
        median: The middle number of the list
    """
    data_list.sort()
    number = len(data_list)
    if number % 2 != 0:
        middle = int((number - 1) / 2)
        # - is the subtraction operation. It subtracts the second number from
        # the first
        median = data_list[middle]

    else:
        middle = (number + 1) / 2
        # / is the regular division operation. It divides the numbers and keeps
        # the quotient and remainder
        upper = math.ceil(middle)
        lower = math.floor(middle)
        upper = data_list[upper - 1]
        lower = data_list[lower - 1]
        median = (upper + lower) / 2
    return median


def get_mean(data_list):
    """This function finds the average of a list"""

    total = data_list[0]
    for x in range(1, (len(data_list))):
        total = total + data_list[x]
    mean = total / (len(data_list))
    return mean


def get_variance(data_list, average):
    """This function finds the statistical variance of a list"""
    for x in range(len(data_list)):
        data_list[x] = data_list[x] - average
    for x in range(len(data_list)):
        data_list[x] = (data_list[x]) ** 2
    # ** is the exponent operation. It multiplies the first number to itself a
    # certain amount of times stated by the second number
    total = data_list[0]
    for x in range(1, (len(data_list))):
        total = total + data_list[x]
    variance = total / (len(data_list) - 1)
    return variance


def main():
    human_verification()
    intro()
    junk2 = []
    sample = data_input(junk2)
    print("Thank you! The program will now give you your results!")
    sample.sort()
    time.sleep(3.0)
    print("Your sample data is:", sample)
    median = get_median(sample)
    mean = get_mean(sample)
    variance = get_variance(sample, mean)
    std_dev = variance ** 0.5
    print('The mean of your sample is:', format(mean, '.3f'))
    print("The median of your sample is:", median)
    print("The variance of your sample is:", format(variance, '.0f'))
    print("The standard deviation of your sample is", format(std_dev, '.3f'),
          sep=': ')


main()
