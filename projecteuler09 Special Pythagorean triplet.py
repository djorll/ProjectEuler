# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# 
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# 
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


a = 1
# comme a<b<c et a+b+c=1000 max(a)=332
while a < 333:
    b = 2
    while b < 1000 - a - b:
        # a+b = 500 mini sinon l'aire est negative
        if a + b > 500:
            if a ** 2 + b ** 2 - (1000 - a - b) ** 2 == 0:
                print(a * b * (1000 - a - b))
        b += 1
    a += 1
