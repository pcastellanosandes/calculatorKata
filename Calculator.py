__autor__= 'Paula Castellanos'

class Calculator:
    def add(self, stringNumbers):
        if stringNumbers == "":
            return 0
        elif "," in stringNumbers or ":" in stringNumbers or "&" in stringNumbers:
            stringNumbers = stringNumbers.replace("&" , ",")
            stringNumbers = stringNumbers.replace(":" , ",")
            numbers = stringNumbers.split(",")
            result = 0
            for number in numbers:
                result = result + int(number)

            return result
        else:
            return int(stringNumbers)