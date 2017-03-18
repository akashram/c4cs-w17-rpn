#!/usr/bin/env python3

import operator

OPERATORS = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv,
	'^': expy,
}

def expy(arg1, arg2):
	result = 1;
	for numMult in range(1, arg2):
		result = result * arg1;
	return result



def calculate(arg):
	stack = list()
	for operand in arg.split():
		try:
			operand = float(operand)
			stack.append(operand)
		except:
			arg2 = stack.pop()
			arg1 = stack.pop()
			operator_fn = OPERATORS[operand]
			result = operator_fn(arg1, arg2)
			
			stack.append(result)
	return stack.pop()

def main():
	while True:
		result = calculate(input('rpn calc> '))
		print("Result:", result)

if __name__ == '__main__':
	main()