import random

numbers = range(1, 46)

lotto = random.sample(numbers, 6)
print(lotto)
print(f"오늘 행운의 로또는 {sorted(lotto)}입니다.")
