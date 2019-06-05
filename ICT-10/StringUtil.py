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
        for x in range(0, len(words)):
            phrase = words[x]
            if not "a" in phrase and not "e" in phrase and not "i" in phrase and not "o" in phrase and not "u" in phrase:
                result = result + phrase + "ay" + " "
            elif phrase[0] is "a" or phrase[0] is "e" or phrase[0] is "i" or phrase[0] is "o" or phrase[0] is "u":
                result = result + phrase + "yay" + " "
            else:
                index = self.first_vowel(phrase)
                start = phrase[0:index]
                end = phrase[index:]
                result = result + end + start + "ay "
        return result

    def first_vowel(self, s):
        for index, char in enumerate(s):
            if char in 'aeiou':
                return index

    def shorthand(self, s):
        s = s.lower()
        while "and" in s:
            index = s.index("and")
            beginning = s[0:index]
            end = s[index+3:]
            s = beginning + "&" + end
        while "to" in s:
            index = s.index("to")
            beginning = s[0:index]
            end = s[index+2:]
            s = beginning + "2" + end
        while "you" in s:
            index = s.index("you")
            beginning = s[0:index]
            end = s[index+3:]
            s = beginning + "U" + end
        while "for" in s:
            index = s.index("for")
            beginning = s[0:index]
            end = s[index+3:]
            s = beginning + "4" + end
        s = self.remove_vowels(s)
        return s

    def remove_vowels(self, s):
        s = s.lower()
        while "a" in s:
            index = s.index("a")
            beginning = s[0:index]
            end = s[index+1:]
            s = beginning + end
        while "e" in s:
            index = s.index("e")
            beginning = s[0:index]
            end = s[index+1:]
            s = beginning + end
        while "i" in s:
            index = s.index("i")
            beginning = s[0:index]
            end = s[index+1:]
            s = beginning + end
        while "o" in s:
            index = s.index("o")
            beginning = s[0:index]
            end = s[index+1:]
            s = beginning + end
        while "u" in s:
            index = s.index("u")
            beginning = s[0:index]
            end = s[index+1:]
            s = beginning + end
        return s


utility = StringUtil()
print("Reversed String: " + utility.reverse("Bryce Tsuyuki"))
print("Is tombstone a palindrome? " + str(utility.is_palindrome("tombstone")))
print("Is racecar a palindrome? " + str(utility.is_palindrome("racecar")))
print("How are you in Pig Latin: " + str(utility.pig_latin("How are you")))
print("The cat and the dog went to the farm to see you and the family for 5 days.")
result = str(utility.shorthand("The cat and the dog went to the farm to see you and the family for 5 days."))
print("Conversion of the above to shorthand: " + result)

