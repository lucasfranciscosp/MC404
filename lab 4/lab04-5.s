main:
    addi t0, zero, 4   # escolhe a operacao de leitura de inteiro
    ecall              # efetua a operacao de leitura de inteiro

    addi s1, zero, 16
    bge a0, s1, fim
    blt a0, zero, fim

    add s0, zero, a0

    addi s2, zero, 10
    bge s0, s2, char
    addi s0, s0, 48

    #imprime numero
    add a0, s0, zero

    addi t0, zero, 2
    ecall

    j fim

char:
    # s0 += 55
    addi s0, s0, 55
    add a0, s0, zero

    addi t0, zero, 2
    ecall

fim:
    ret


