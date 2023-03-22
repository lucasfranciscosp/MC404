main:
  #read a number
  addi t0, zero, 4
  ecall
  
  #s0 receives 1 if a0 is odd, else s0 receives 0
  andi s0, a0, 1
  
  #s1 = 1
  addi s1, zero, 1
  
  #if s0!=s1, it means that s0 is pair, because is equal to 0, so we go to pair
  bne s0, s1 , pair

odd:
  #if its odd, takes the letter I which is from "impar" that means odd in portuguese to
  #output it
  addi a0, zero, 73
  addi t0, zero, 2
  ecall
  j end
pair:
  #else takes the letter P which is from "par" that means par in portuguese to output it
   addi a0, zero, 80
   addi t0, zero, 2
   ecall
end:
   ret

