main:
    #read a number
    addi t0, zero, 4
    ecall
    
    #s0 = a0
    add s0 , zero, a0
    
    #read another number
    addi t0, zero, 4
    ecall
    
    #s1 = a0
    add s1, zero, a0
    
    #xor beetwheen s1 and s0 , s2 = s1 xor s0
    xor s2, s1, s0

    #a0 = s2
    add a0, zero, s2

    #print a0
    addi t0, zero, 1
    ecall

