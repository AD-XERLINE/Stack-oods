
class Stack:
    def __init__(self, list = None): 
        if list == None: 
            self.items = []
        else:
            self.items = list

    def push(self, i): 
        self.items.append(i)

    def pop(self): 
        return self.items.pop()

    def isEmpty(self): 
        return self.items == [] 

    def size(self): 
        return len(self.items)

    
def postfix(s):
    # print(s)
    stack = Stack()
    # stack = []
    for i in range(len(s)):
        # print(s[i])
        if s[i].isdigit():
          #เช็คว่าเป็นตัวเลข
            stack.push(float(s[i]))
            # stack.append(int(s[i]))

        elif s[i]=="+":
            a=stack.pop()
            b=stack.pop()
            stack.push(float(a)+float(b))
            # stack.append(int(a)+int(b))

        elif s[i]=="*":
            a=stack.pop()
            b=stack.pop()
            stack.push(float(a)*float(b))
            # stack.append(int(a)*int(b))

        elif s[i]=="/":
            a=stack.pop()
            b=stack.pop()
            stack.push(float(b)/float(a))
            # stack.append(int(b)/int(a))

        elif s[i]=="-":
            a=stack.pop()
            b=stack.pop()
            # print("*")
            stack.push(float(b)-float(a))
            # stack.append(int(b)-int(a))
        else:
            stack.push(float(s[i]))

    return stack.pop()

print(" ***Postfix expression calcuation***")
token = list(input("Enter Postfix expression : ").split(' '))
# postFixeval(token)
print("Answer : ",'{:.2f}'.format(postfix(token)))
