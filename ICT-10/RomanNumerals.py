class RomanNumerals:
    @classmethod
    def convert_to_roman(cls, num):
        num = int(num)
        thousands = num // 1000
        num = num % 1000
        five_hundreds = num // 500
        num = num % 500
        hundreds = num // 100
        num = num % 100
        fifties = num // 50
        num = num % 50
        tens = num // 10
        num = num % 10
        fives = num // 5
        num = num % 5
        ones = num
        result = ""

        print("Thousands: " + str(thousands))
        print("Five Hundreds: " + str(five_hundreds))
        print("Hundreds: " + str(hundreds))

        result += cls.__add_letters__(thousands, "M", "C", "")
        result += cls.__add_letters__(five_hundreds, "D", "C", "")
        result += cls.__add_letters__(hundreds, "C", "X", "")
        result += cls.__add_letters__(fifties, "L", "")
        result += cls.__add_letters__(tens, "X", "L")
        result += cls.__add_letters__(fives, "V", "X", "I")
        result += cls.__add_letters__(ones, "I", "V", "")
        return result

    @staticmethod
    def __add_letters__(num, letter, larger, larger2):
        num = int(num)
        letter = str(letter)
        larger = str(larger)
        larger2 = str(larger2)
        result = ""
        if num == 4 and letter in 'IXC':
            result = letter + larger
        elif num == 9 and letter in 'IXC':
            result = letter + larger2
        else:
            while num > 0:
                num = num - 1
                result = result + str(letter)
        return str(result)


print("19 in Roman Numerals: " + str(RomanNumerals.convert_to_roman(19)))