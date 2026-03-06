import pickle

with open('../files/employee.txt', 'rb') as file:
    obj = pickle.load(file)

obj.display()  # Output: 1    Uday    50000
