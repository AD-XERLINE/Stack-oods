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

def walk():
    for i in range(len(lst)):
                if lst[i][0] == "A":
                    s.push(int(lst[i][2:]))
                    # print(s.items)

                elif lst[i][0] == "B":
                    a.items = []
                    if s.items == []:
                        print("0")
                    else:
                        a.push(s.items[-1])
                        # print(s.items[-1])
                        s.items.reverse()
                        for j in range(len(s.items)):
                            if s.items[j] > a.items[-1]:
                                a.push(s.items[j])
                                # print(a.items)
                                
                        if len(a.items)==1:
                            print(len(a.items)) 
                        else:
                            print(len(a.items))
                        s.items.reverse()

                elif lst[i][0] == "S":
                    for k in range(len(s.items)):
                        if int(s.items[k]) % 2 == 1:
                            s.items[k] = int(s.items[k])+2
                        elif int(s.items[k]) % 2 == 0:
                            s.items[k] = int(s.items[k])-1
                    # print(s.items)

lst = input("Enter Input : ").split(',')
s = Stack()
a = Stack()
walk()

