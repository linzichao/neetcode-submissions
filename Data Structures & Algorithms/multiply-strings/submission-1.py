class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        product = [0] * (len(num1) + len(num2))
        counter = len(product) - 1

        int_to_str = {i : c for i, c in enumerate("0123456789")}
        str_to_int = {c : i for i, c in enumerate("0123456789")}

        for n1 in reversed(num1):
            tmp = counter
            for n2 in reversed(num2):
                product[tmp] += str_to_int[n1] * str_to_int[n2]
                product[tmp - 1] += product[tmp] // 10
                product[tmp] %= 10
                tmp -= 1
            counter -= 1

        index = 0
        while index < len(product) - 1 and product[index] == 0:
            index += 1
        
        return "".join([int_to_str[i] for i in product[index:]])