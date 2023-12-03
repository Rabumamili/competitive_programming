class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1 = [int(digit) for digit in num1][::-1]
        num2 = [int(digit) for digit in num2][::-1]
    
        # Initialize the result list with zeros
        result = [0] * (len(num1) + len(num2))
    
        # Multiply each digit in num2 with num1 and add the result to the appropriate position in the result list
        for i, digit2 in enumerate(num2):
            carry = 0
            for j, digit1 in enumerate(num1):
                product = digit1 * digit2 + carry + result[i + j]
                carry = product // 10
                result[i + j] = product % 10
            result[i + len(num1)] = carry
    
        # Remove leading zeros from the result list and convert it back to a string
        result = result[::-1]
        print(result)
        while len(result) > 1 and result[0] == 0:
            result.pop(0)
        return ''.join(str(digit) for digit in result)