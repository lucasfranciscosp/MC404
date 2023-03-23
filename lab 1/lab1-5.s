main:
    addi t0, zero, 4   # escolhe a operacao de leitura de inteiro (4)
    ecall              # efetua a operacao de leitura de inteiro
    add s0 , a0, zero  # s0 = a0

    addi t0, zero, 4   # escolhe a operacao de leitura de inteiro (4)
    ecall              # efetua a operacao de leitura de inteiro
    add s1 , a0, zero  # s1 = a0
    
    addi t0, zero, 1   # escolhe a operacao de escrita de inteiro (1)
    add a0, s1, s0
    ecall              # efetua a operacao de escrita de inteiro

    ret




