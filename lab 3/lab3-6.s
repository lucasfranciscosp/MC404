main:
    #read a number
    addi t0, zero, 4
    ecall

    add s0, zero, zero
    add s1, zero, a0
jump:
    #s0 += 1
    addi s0, s0, 1
    
    
    #print a0
    addi t0, zero, 1
    ecall

end:
    ret


