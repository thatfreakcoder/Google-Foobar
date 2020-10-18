def solution(n):
  n = int(n)
  count = 0
  
  while n > 1:
    # if n is even, divide by 2 using bit manipulation
    if n & 1 == 0:
      n >>= 1
    else:
      # Use bit manipulation to create as many 0 from LSB as possible
      n = (n - 1) if (n == 3 or n % 4 == 1) else (n + 1)

    count += 1
  return steps