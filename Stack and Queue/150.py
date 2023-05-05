from operator import add, sub, mul
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        Evaluates the given Reverse Polish Notation expression and returns the result.

        :param tokens: A list of strings representing the Reverse Polish Notation expression.
        :return: An integer representing the result of the evaluation.
        '''
        # Define a dictionary to map operators to their corresponding functions
        operators = {'+':add, '-':sub, '*':mul, '/':lambda x,y : int(x/y)}

        # Create an empty stack to hold the operands
        stack = []
        for token in tokens:
            # If the token is an operand, pushes it onto the stack
            if token not in operators:
                stack.append(int(token))

            # If the token is an operator, pops two operands from the stack, applies the operator and pushes the result onto the stack
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                stack.append(operators[token](operand1,operand2))

        return stack.pop()