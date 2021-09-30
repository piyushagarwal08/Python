print("Let's practice everything")
print("You\'d need to know \'bout escapes with \\that do:")
print("\nnew lines and \t tabs")

poem = """
\t all this is useless chutiyapa
and none to be of use.
"""
print("------------=====>")
print(poem)
print("------------")

five = 10 - 2 + 3 - 6
print(f"this should be five {five}")

def secret_formula(started):
    jelly_beans = started * 5000
    jars = jelly_beans / 10000
    crates = jars / 1000
    return jelly_beans,jars,crates

start_point = 100000
beans , jars , crates = secret_formula(start_point)
print("with a starting point of: {}".format(start_point))
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point/ 10
print("We can also do that this way:")
print("We'd have {} beans, {} jars, {} crates".format(*secret_formula(start_point)))
