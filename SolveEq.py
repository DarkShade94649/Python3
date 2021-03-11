# * : Multiply, / : Divide, + : Add, - : Subtract

# rule 1: subtract (<val>) both sides
# 	map: ...+(<val>)...
# rule 2: add (<val>) both sides
# 	map: ...-(<val>)...
# rule 3: divide (<val>) both sides
# 	map: (<val>)*<var> and vise versa
# rule 4: multiply recibrockel of (<val>) both sides
# 	map 1: (<val>)/<var> => <var> = <num>
# 	map 2: <var>/(<val>) => <num> = <var>

# only one varieble in it ie. (3x + 5y + 10z = 15x +10z +6y) not allowed
# will be one term:
# (+|-)10*5/2
# (+|-)10/5
# (+|-)5^2/10
# means do addition and subtratction until division and multiplication are left

import re
equ = input("Equation: ")
equ = equ.replace(" ", "")
eqLHS = equ.split("=")[0]
eqRHS = equ.split("=")[-1]

while re.match(r"(?:.*\+|^)\d+(?:\+|\-|$)", eqLHS):
	num = re.match(r"(?:.*\+|^)(\d+)(?:\+|\-|$)", eqLHS).group(1)
	eqRHS = eval(f"{eqRHS}-{num}")
	eqLHS = re.sub(rf".{num}", '', eqLHS)

while re.match(r"(?:.*\-|^)\d+(?:\+|\-|$)", eqLHS):
    num = re.match(r"(?:.*\-|^)(\d+)(?:\+|\-|$)", eqLHS).group(1)
    eqRHS = eval(f"{eqRHS}+{num}")
    eqLHS = re.sub(rf".{num}", '', eqLHS)

print(f"{eqLHS}={eqRHS}")
