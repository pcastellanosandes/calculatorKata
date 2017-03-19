__autor__= 'Paula Castellanos'

class Calculator:
    def add(self, numbers):
        if numbers == "":
            return 0
        elif ',' in numbers:
            return int(numbers[0]) + int(numbers[2])
        else:
            return int(numbers)