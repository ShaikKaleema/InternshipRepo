'''Problem : Add two numbers
Problem Statement
Every problem starts with a Problem Statement. It tells you in detail about the task to be solved.
Shivam is the youngest programmer in the world, he is just 12 years old. Shivam is learning programming and today he is writing his first program.
The task is very simple: given two integers A and B, write a program to add these two numbers and output it.'''
# Code :
T = int(input())
for tc in range(T):
	# Read integers a and b.
	(a, b) = map(int, input().split(' '))
	
	ans = a + b
	print(ans)
