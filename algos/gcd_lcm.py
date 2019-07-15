# finding the gcd of two numbers
def gcd(a,b):
    if a > b:
        num = a
        den = b
    else:
        num = b
        den = a
    rem = num%den
    while rem != 0:
        num = den
        den = rem
        rem = num % den
    gcd = den

    return gcd


x = map(int,raw_input('Enter array of two numbers separated by space\n').split())

gcd = gcd(x[0],x[1])
print gcd
# calculating lcm after gcd
lcm = (x[0]*x[1])/gcd
print lcm
