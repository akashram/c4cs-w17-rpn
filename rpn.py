#!usr/bin/env python3

def calculate(arg):
	stack = list()
	for operand in arg.split():
		if operand == "+":
			stack.append(stack.pop() + stack.pop())
		
		elif operand == "-":
			stack.append((stack.pop() - stack.pop()) * -1)

		else:
			stack.append(float (operand))
	return stack.pop()

def main():
	while True:
		result = calculate(input("rpn calc> "))
		print("result", result)

if __name__ == "__main__":
	main()
