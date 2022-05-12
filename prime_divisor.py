"""
レポート２　素数ゼネレータ
"""



def divisors(n):
    divisors_list = []
    for a in range(1 ,n + 1):
        if n % a == 0:
            divisors_list.append(a)
    return divisors_list

def prime():
    for b in range(2, 101):
        if len(divisors(b)) == 2:
            yield b

o = iter(prime())

prime_list = []

for c in o:
    prime_list.append(c)
    
prime_list = map(str, prime_list)
result = " ".join(prime_list)
print(result)