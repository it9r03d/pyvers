from platform import python_version
from re import search

py_version = python_version()
mo = search(r'\d+.\d+.\d+', py_version)
gr_version = mo.group()

l = [int(x, 10) for x in gr_version.split('.')]
l.reverse()
int_version = sum(x * (100 ** i) for i, x in enumerate(l))

if 30000 > int_version:
	print(py_version + ' is 2.z.z')
else:
	print(py_version + ' is 3.z.z')
