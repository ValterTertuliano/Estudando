from calculadora import soma

print(soma(5, 5))
print(soma(-5, -5))
print(soma(5, -5))

try:
    print(soma("10", 3))
except AssertionError as error:
    print(f"Erro de tipagem: {str(error)}")
