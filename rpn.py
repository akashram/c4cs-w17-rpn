#!usr/bin/env python3

operators = {
	"+" : add
	"-" : subtract
}

def add(arg1, arg2):
	return arg1 + arg2

def subtract(arg1, arg2)
	return arg1 - arg2

def calculate(arg):
	stack = list()
	for operand in arg.split():
		try:
			operand = float(operand)
			stack.append(operand)
		except ValueError:
			arg2 = stack.pop()
			arg1 = stack.pop()
			stack.append(operators[operand, arg1, arg2])
			if operand == "+":
				stack.append(arg1 + arg2)
			elif operand == "-":
				stack.append(arg1 - arg2)
		
	return stack.pop()

def main():
	while True:
		result = calculate(input("rpn calc> "))
		print("result", result)

if __name__ == "__main__":
	main()
