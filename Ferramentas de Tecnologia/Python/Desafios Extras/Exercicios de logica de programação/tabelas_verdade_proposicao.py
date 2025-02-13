A = True
B = True

print(f'A ou B : {A or B}')  # A ∨ B
print(f'A e B: {A and B}')  # A ∧ B
print(f'A implica B: {not A or B}')  # A → B, equivalente a ¬A ∨ B
print(f'Não (A e B) é equivalente não A ou não B: {(not (A and B)) == (not A or not B)}')  # ¬(A ∧ B) ⇔ ¬A ∨ ¬B
print(f'Não (A ou B) é equivalente não A e não B: {(not (A or B)) == (not A and not B)}')  # ¬(A ∨ B) ⇔ ¬A ∧ ¬B
