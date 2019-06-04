class StringUtil:
    def reverse(self, to_reverse):
        result = ""
        for i in range(0, len(to_reverse)):
            result = to_reverse[i] + result
        return result

    def is_palindrome(self, to_check):
        return self.reverse(to_check) == to_check

    def pig_latin(self, convert):
        words = convert.split()
        result = ""
        for phrase in range(0, len(words)):
            if not "a" in phrase and not "e" in phrase and not "i" in phrase and not "o" in phrase and not "u" in phrase:
                result = result + phrase + "ay" + " "
            elif phrase[0] is "a" or phrase[0] is "e" or phrase[0] is "i" or phrase[0] is "o" or phrase[0] is "u":
                result = result + phrase + "yay" + " "
            else:
                index = self.first_vowel(phrase)
                start = phrase[0:index]
                end = phrase[index:]
                result = result + end + start + "ay "

    def first_vowel(self, s):
        for index, char in enumerate(s):
            if char in 'aeiou':
                return index


utility = StringUtil()
print("Reversed String: " + utility.reverse("Bryce Tsuyuki"))
print("Is tombstone a palindrome? " + str(utility.is_palindrome("tombstone")))
print("Is racecar a palindrome? " + str(utility.is_palindrome("racecar")))
print("How are you in Pig Latin: " + str(utility.pig_latin("How are you")))

