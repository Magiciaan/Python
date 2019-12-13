#wap to solve quadratic equation
import cmath
a = int(input('enter a no.'))
b = int(input('enter a no.'))
c = int(input('enter a no.'))
d = (b * cmath.sqrt(b**2 - 4 * a * c))/(2*a)
e = (b * (-cmath.sqrt(b**2 - 4 * a * c)))/(2*a)
print (d,e)