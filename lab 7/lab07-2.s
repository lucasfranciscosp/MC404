main:
  li s0, 1        # s0 = 0 + 1
  li s1, 2        # s1 = 0 + 2
  add  s2, s1, s0         # s2 = s1 + s0
  li a0, 10
  ecall