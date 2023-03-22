
main:
  #read a num
  addi t0, zero, 4
  ecall
  
  #do operation and with 3, if its not multiply it will return 1
  andi s0, a0, 3

  #s1 = 1
  addi s1, zero, 1

  #if s0 != s1 , means that its multiply because s0 == 0
  bne s0, s1 , mult

notmult:
  #output the letter "S" that is from "Sim" in portuguese which means "Yes"
  addi a0, zero, 78
  addi t0, zero, 2
  ecall
  j end
mult:
  #output the letter "N" that is from "Nao" in portuguese which means "No"
   addi a0, zero, 83
   addi t0, zero, 2
   ecall
end:
   ret



