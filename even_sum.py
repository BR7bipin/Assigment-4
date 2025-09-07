def main():
    n = int(input("Enter a positive number: ")))
    if n < 0:
        print("Number not a positive number");
        return
    print(f"Total sum of even numbers from range 1 to {n}:", sum_of_evens(n))

def sum_of_evens(n):
    res = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            res += i    
    return res  
main()
