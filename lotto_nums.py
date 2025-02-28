import random

nums = [i for i in range(1, 46)]
lotto_nums = random.sample(nums,   )
lotto_nums.sort()
print(f"오늘의 로또 번호: {lotto_nums}")

lotto_nums = random.choices(nums,    )
lotto_nums.sort()
print(f"오늘의 로또 번호: {lotto_nums}")