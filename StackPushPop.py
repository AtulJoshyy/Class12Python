#Menu driven program to implement a Stack

#function for PUSH operation
def push():      
    while True:

        bookId=str(input("enter bookID : "))
        bookName=str(input("Enter bookName : "))
        author=str(input("Enter Author : "))
        L=[bookId,bookName,author]
        stack.append(L)
        print(stack)

        ch = str(input("Do you want to add more (Y/N) : "))
        if ch in 'Nn':
            break

#function for POP operation
def Pop():
    if stack == []:            #to check if the stack is empty or not
        print("Stack is Empty")
        ch=str(input("Do you want to push stack (Y/N) : "))
        if ch in 'yY':
            push()
        elif ch in 'nN':       #***THIS PART IS OPTIONAL***
            q=str(input("Press Q to quit : "))
            while True:
                if q in 'qQ':
                    break
                
        else:
            print("INVALID!!")

    else:
        stack.pop()
        print(stack)

#Main Program
def main():
    print('''
    1.Push Stack
    2.Pop stack''')
    choice = int(input("Enter your choice : "))
    
    if choice == 1 :
        push()
    elif choice == 2 :
        Pop()
    else:
        print("INVALID SELECTION !!!!")

stack = []      #This is the STACK which we are using
main()