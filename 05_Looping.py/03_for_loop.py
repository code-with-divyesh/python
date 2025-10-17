# 03_for_loop.py
# Examples of using for i in range(50)

# 1) Simple loop: print 0..49
for i in range(50):
  print(i,end=" ")

# 2) If you want 1..50 instead:
print()
for i in range(1, 51):
  print(i,end=" ")

# 3) Aggregate example: sum of 0..49
total = sum(range(50))
print("sum 0..49 =", total)