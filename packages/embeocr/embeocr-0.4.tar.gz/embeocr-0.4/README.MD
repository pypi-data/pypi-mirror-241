install with pip: pip install embeocr

code example:
from embeocr import embedding

a = input()
x = embedding.get_dense_vector(a)
print(x)