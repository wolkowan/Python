import numpy
import create_massive_uniq
numbers=numpy.random.randint(1, size=(5,10))
create_massive_uniq.print_matrix(numbers)

a=numpy.array(numbers)
print(2 in a)
print(len(a))

a = numpy.array(a).reshape((2,25))
print(a)

