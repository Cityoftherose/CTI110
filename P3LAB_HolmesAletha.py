is_leap_year = False
   
def is_leap_year(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False

if __name__ == '__main__':

    year = int(input())

    if is_leap_year(year):
        print(f'{year} - leap year')
    else:
        print(f'{year} - not a leap year')