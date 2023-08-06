
# PrimeNumber library
<br>

## Documentation

### Check if a number is prime:
>from PrimeNumber import Prime<br><br>
print(Prime().is_prime(n=15))<br><br>
False

### Generate the first 100 prime numbers:
>from PrimeNumber import Prime<br><br>
gen = Prime().generator()<br>
for _ in range(100):<br>
&nbsp;&nbsp;&nbsp;&nbsp;print(next(gen))<br><br>
2<br>
3<br>
5<br>
...<br>
523<br>
541

### Decompose a whole number in prime factors:
>from PrimeNumber import Prime<br><br>
print(Prime().prime_factors(n=546))<br><br>
[2, 3, 7, 13]
