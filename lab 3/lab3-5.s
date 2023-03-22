
main:
    #read a number
    addi t0, zero, 4
    ecall
    
    #s0 = a0
    add s0, zero, a0

    #if a0 == 0 , go to end
    beq a0, zero, end

jump:

    #read a number
    addi t0, zero, 4
    ecall

    #if a0 == 0 , go to end
    beq a0, zero, end

    #s1 = s0 xor a0
    xor s1, s0, a0

    #a0 = s1
    add a0, s1, zero

    #print a0
    addi t0, zero, 1
    ecall
    j jump

end:
    ret

