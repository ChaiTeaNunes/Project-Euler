# Largest Prime Factor
def is_prime(n):
   for i in range(2, n-1):
      if n % i == 0:
         return False
   return True
   
def factors(n):
   output = tuple()
   if is_prime(n):
      output += (n,)
   else:
      for i in range(2, n-1):
         if n % i == 0:
            output += factors(i)
            n /= i
            output += factors(n)
   return output
         

print(set(factors(13195)))
