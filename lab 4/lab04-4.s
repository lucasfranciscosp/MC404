main:
    addi t0, zero, 5   # escolhe a operacao de leitura de char
    ecall              # efetua a operacao de leitura de char

    add s0, a0, zero

    # verifica primeira condicao maiscula

    addi s1, zero, 65

    bge s0, s1, letra
    blt s0, s1, naoletra

letra:

    addi s2, zero, 91
    addi s3, zero, 97
    blt s0, s2, maiscula
    bge s0, s3, minusculo
    j naoletra
    
maiscula:
    addi s0, s0, 32
    j imprimeletra

minusculo:
    addi s4, zero, 123
    bge s0, s4 , naoletra
    addi s0, s0, -32

imprimeletra:

    add a0, s0, zero
    
    #imprime s0

    addi t0, zero, 2
    ecall

    j fim

naoletra:

    #imprime o que veio na entrada

    addi t0, zero, 2
    ecall

    j fim

fim:
    ret


