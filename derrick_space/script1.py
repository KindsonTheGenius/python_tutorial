# Excercise 1.1
a = 3 + 1
print(a)
# 4

b = 3 * 3
print(b)
# 9

c = 2 ** 3
print(c)

d = 'Hello, world!'
print(d)

# Excercise 1.3
a = 'py' + 'thon'
print(a)
#Python

b = 'py' * 3 + 'thon'
print(b)
#pypypython

c = 'py' - 'py'
print(c)
#TypeError: unsupported operand type(s)

d = '3' + 3
print(d)
#TypeError: can only  concatenate str (not "int) to str

e = 3 * '3'
print(e)
#333

f = a
print(f)
#python

g = a = 3
print(g)
#3

h = a
print(h)
#3

# Excercise 1.4
a = 1 == 1
print(a)
#True

b = 1 == True
print(b)
#true

c = 0 == True
print(c)
#False

d = 0 == False
print(d)
#true

e = 3 == 1 * 3
print(e)
#true

f = (3 == 1) * 3
print(f)
# 0

g = (3 == 3) * 4 + 3 == 1
print(g)
#False

h = 3 ** 5 >= 4 ** 4
print(h)
#False

# Excercise 1.5
a = 5 / 3
print(a)
# 1.6666666666666667

b = 5 % 3
print(b)
# 2

c = 5.0 / 3
print(c)
# 1.6666666666666667

d = 5 / 3.0
print(d)
# 1.6666666666666667

e = 5.2 % 3
print(e)
# 2.2

f = 2001 ** 200
print(f)
# 1775896810483121914350934797871501063452843428843794422323202530887281536545210629921129898113201749875234297340507804201761453596034016264189501186924066128377025843892373608427790859511135990682732202975330824797118808624727351608183194154557208730494440110429635650057431833674286462463508755276302896154336475782768613964332764108132533925570342220340698973761380541294970139762186212823359128790706292900765512137078550033912252338262922477518858757114840012576514724742388124595061301502222934806074032688691170880996881967426442947828261057852871032366879179996122216385870273020506079240103910728766397733398071775041745854959302025036249707279600400001

#Excercise 1.6
a = 2000.3 ** 200
print (a)
#OverflowError: (34, result too large)

b = 1.0 + 1.0 - 1.0
print(b)
# 1.0

c = 1.0 + 1.0e20 - 1.0e20
print(c)
# 0.0

#Excercise 1.7
name = "Derrick"
greeting = "Hello," + name + "!"