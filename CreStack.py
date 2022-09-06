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

print(" *** Stack implement by Python list***")
lst = [e for e in input("Enter data to stack : ").split()]
s = Stack()
# ใส่ข้อมูลลง stack
for i in range(len(lst)):
    s.push(lst[i])
print(s.size(),"Data in stack : ",s.items)

while not s.isEmpty():
    # เอาค่าจากบนสุด(หรือที่เข้าใจคือท้ายสุดออกจาก stack)
    s.pop()
print(s.size(),"Data in stack : ",s.items)