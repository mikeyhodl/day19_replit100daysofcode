# counter = 0
# while counter < 10:
#   print(counter)
#   counter += 1

# for counter in range(10):
#   print(counter)

# total = 0
# for number in range(100):
#     total += number
#     print(total)

# for days in range(7):
#     print("Day", days)

# total = 10
# for counter in range(100):
#     total += 10
#     print("total")

loan = 1000
rate = 0.05
for apr in range(10):
    loan += (loan * rate)
    print("Year", apr + 1, "total loan is", round(loan, 2))
