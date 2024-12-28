def perm(n):  
    p = []  
    return permNext(n, p)  

def permNext(n, p):  
    i = len(p)
    if i == n:  
        print(p)  
        return

    for x in range(n): 
        if x not in p:  
            p.append(x)  
            permNext(n, p)  
            p.pop()  

if __name__ == "__main__":
    for num in range(2, 6):  
        print(f"Permutations of {num}:")
        perm(num)
        print()  
