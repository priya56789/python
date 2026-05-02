import importlib
pack1=input("Enter module name:")
try:
    module=importlib.import_module(pack1)
except ModuleNotFoundError:
    print("Module not found")
