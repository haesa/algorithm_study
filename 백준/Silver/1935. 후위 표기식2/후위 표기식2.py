import sys

read = sys.stdin.readline
write = sys.stdout.write

N = int(read())
postfix_notation = read().strip()
operand_list = [int(read()) for _ in range(N)]
operator_list = ['+', '-', '*', '/']

stack = []
offset = ord('A')

for char in postfix_notation:
  if char in operator_list:
    op1 = stack.pop()
    op2 = stack.pop()
    
    match char:
      case '+':
        stack.append(op2 + op1)
        pass
      case '-':
        stack.append(op2 - op1)
        pass
      case '*':
        stack.append(op2 * op1)
        pass
      case '/':
        stack.append(op2 / op1)
    
  else:  
    stack.append(operand_list[ord(char) - offset])

write(f"{stack[0]:.2f}")