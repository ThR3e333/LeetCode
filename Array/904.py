class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        '''
        Returns the maximum number of fruits that can be collected by the worker. The worker can only pick two types of fruits.

        :param fruits: A list of integers representing the types of fruits on each tree.
        :return: An integer representing the maximum number of fruits that can be collected.
        '''
        start_index = 0
        fruit_count = {}
        max_fruit_count = float('-inf')

        for i in range(len(fruits)):
            # Add current fruit to fruit count
            if fruits[i] in fruit_count.keys():
                fruit_count[fruits[i]] += 1
            else:
                fruit_count[fruits[i]] = 1

            # Check if there are more than 2 types of fruits
            while len(fruit_count) > 2:
                # Remove the oldest type of fruit from the count
                fruit_count[fruits[start_index]] -= 1
                if fruit_count[fruits[start_index]] == 0:
                    del fruit_count[fruits[start_index]]
                start_index += 1

            # Update the maximum fruit count
            max_fruit_count = max(max_fruit_count, i - start_index + 1)

        return max_fruit_count
