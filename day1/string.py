a = 'this is "a" line'

b = "this is a line"

c = '''
this is a line
this is another line
'''

d = """
this is a line
this is another line
"""

print(a)
print(b)
print(c)
print(d)

print( ''' this is 'single' and this is "double" ''')
print( ' this is \'\'\'triple\'\'\', """triple""" ')

a = 5

s = "value of a is " + str(a)
print(s)

# f" "

s = f"value of a is {a}"
print(s)

a = 5
b = 6
c = 10
d = a + b / c

# "a=5 b=6 c=11"
print(f"a={a} b={b} c={c}")
print(f"a={a} b={b} c={(a+b)+3} d={d}")