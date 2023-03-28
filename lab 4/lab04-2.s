main:
    addi t0, zero, 5   # escolhe a operacao de leitura de char
    ecall              # efetua a operacao de leitura de char

    add s0, a0, zero

    # passando para letra maiscula na ascii

    addi s0, s0, 32

    # imprimindo o char minusculo

    add a0, s0, zero

    addi t0, zero, 2
    ecall

    ret


