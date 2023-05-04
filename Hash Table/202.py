class Solution:
    def isHappy(self, n: int) -> bool:
        '''
        Check if a number is happy number.

        :param n: An integer representing the number to be checked.
        :return: A boolean value indicating whether the number is a happy number.
        '''
        # Define a helper function to get sum of the squares of the digits
        def getSum(num):
            '''
            Returns the sum of squares of digits of a number.
            '''
            sum_of_square = 0
            while num:
                sum_of_square += (num % 10)**2
                num = num // 10
            return sum_of_square

        # Keep track of the numbers we've seen
        seen = set()

        # Repeatedly replace the number by the sum of the squares of its digits
        # until we either find 1 or detect a cycle
        while True:
            n = getSum(n)
            if n == 1:
                return True
            if n in seen:
                return False
            else:
                seen.add(n)