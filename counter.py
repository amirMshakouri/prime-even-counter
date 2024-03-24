def even(num):
    even_numbers =[]
    
    for i in range(1,num+1):
        if num % i == 0 :
            even_numbers.append(i)
    return even_numbers

def prime(num):
    prime_numbers =[]
    
    for i in range(1,num+1):
        if num % i != 0 :
            prime_numbers.append(i)
    return prime_numbers


num = int(input("enter your number :"))
print(f'prime numbers list is : {prime(num)}')
print(f'even numbers list is : {even(num)}')
