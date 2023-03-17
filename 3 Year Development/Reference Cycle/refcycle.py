# Ref cycle stand for a cycle that will never end
# becouse the references are keep-alived by other variables/tasks
# on the system - equal problem with the ui's

# Repository:
# https://docs.python.org/3/library/weakref.html

a = [1, 2, 3]
b = [a, 3, 4]
a.append(b)

b = None

print(a)

#Problem solved importing:
import weakref

c = [1, 2, 3]
d = [weakref.ref(c), 3, 4]
c.append(d)

d = None

print(c)