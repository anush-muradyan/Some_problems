def tower_of_hanoi(n,source,destination,aux):
    '''Tower of Hanoi consists of three pegs or towers with n disks placed one over the other.
    The objective of the puzzle is to move the stack to another peg following these simple rules.
    Only one disk can be moved at a time.
    No disk can be placed on top of the smaller disk. 2^N-1 step are required.
    '''
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    tower_of_hanoi(n-1,source,aux,destination)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n-1,aux,destination,source)

tower_of_hanoi(2,"A","C","B")


def reverse_print(n):
    '''Print numbers in reverse order'''
    if not n:
        return 
    num = input()
    reverse_print(n-1)
    print(num)
        
def reverse_list(l):
    if not l:
        return []
    return reverse_list(l[1:]) + [l[0]]

def reverse_list_tail(l, reversed_l=[]):
    if not l:
        return reversed_l
    return reverse_list_tail(l[:-1],reversed_l + [l[-1]])

def fib(n):
    a,b = 1,1
    for _ in range(2,n+1):
        c = a + b
        a,b = b,c
    return b

def fib_rec(n):
    if n == 0 or n == 1:
        return 1
    return fib_rec(n-1) + fib_rec(n-2)
