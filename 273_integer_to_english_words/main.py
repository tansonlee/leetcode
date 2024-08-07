class Solution:
    def numberToWords(self, num: int) -> str:
        number_to_word = {
            0: "Zero",
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety"
        }
        
        if num < 20:
            return number_to_word[num]
        
        if len(str(num)) == 2:
            tens_word = number_to_word[(num // 10) * 10]
            ones_digit = num % 10
            if ones_digit == 0:
                return tens_word
            else:
                ones_word = self.numberToWords(ones_digit)
                return tens_word + " " + ones_word
        
        if len(str(num)) == 3:
            return self.word_template(num, 100, "Hundred")
        
        if len(str(num)) <= 6:
            return self.word_template(num, 1000, "Thousand")

        if len(str(num)) <= 9:
            return self.word_template(num, 1000000, "Million")

        if len(str(num)) <= 12:
            return self.word_template(num, 1000000000, "Billion")
        
    
    def word_template(self, num, scale, signifier):
        significant_number = num // scale
        significant_word = self.numberToWords(significant_number)

        rest_number = num % scale
        if rest_number == 0:
            return significant_word + " " + signifier
        else:
            rest_word = self.numberToWords(rest_number)
            return significant_word + " " + signifier + " " + rest_word

