main:
    #s2 = sumpair , s3 = sumodd
    add s2, zero, zero
    add s3, zero, zero

jump:
    #read a number
    addi t0, zero, 4
    ecall
   
    #if number == 0, go finish the code
    beq a0, zero, end

    #check if a0 is odd
    andi s0, a0, 1

    #s1 = 1
    addi s1, zero, 1

    #if s0!=s1 means that s0 == 0 and is pair
    bne s0, s1 , pair

odd:
    #s3+= input
    add s3, s3, a0
    j jump

pair:
    #s2+= input
    add s2, s2, a0
    j jump

end:
    #print a0
    addi t0, zero, 1

    #a0 = s3 - s2
    sub a0, s3, s2
   
    ecall
    ret

