import inspect
import tkinter
print(type(tkinter))

print(inspect.ismodule(tkinter))
print(inspect.isclass(tkinter))
print(inspect.isfunction(tkinter))
print(inspect.getmodule(tkinter))

for method in dir(tkinter):
    print(method)

print(hasattr(tkinter,'revers'))
print(hasattr(tkinter,'__spec__'))
print(getattr(tkinter,'reverse', None))