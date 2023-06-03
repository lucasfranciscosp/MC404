# Nome: Lucas Francisco Silva Paiva
# RA: 248390

def converter_int_bin(n):
    binario_string = bin(n)[2:]
    binario_12 = binario_string.zfill(12)
    return binario_12

def converter_int_bin_32(n):
    binario_string = bin(n)[2:]
    binario_12 = binario_string.zfill(32)
    return binario_12

def lui(rd, imm):
    saida_aux = converter_int_bin_32(imm)
    saida = ""
    for i in range(19):
        saida += saida_aux[i]
    saida += registradores[rd]
    saida += "0110111"
    return saida

def li(rd, imm):
    if  imm < 2048 and imm >= -2048:
        saida = addi(rd, "zero", imm)
    else:
        imm_aux = converter_int_bin_32(imm)
        if imm_aux[11] == 1:
            imm += pow(2,12)
        saida = lui(rd, imm)
    return saida

def mul(rd, rs1, rs2):
    saida = "0000001"
    saida += registradores[rs2]
    saida += registradores[rs1]
    saida += "000"
    saida += registradores[rd]
    saida += "0110011"
    return saida

def sw(rs1, rs2, imm):
    saida_aux = converter_int_bin(imm)
    saida = ""
    for i in range(7):
        saida += saida_aux[1 + i]
    saida += registradores[rs2]
    saida += registradores[rs1]
    saida += "010"
    for i in range(5):
        saida += saida_aux[7 + i]
    saida += "0100011"
    return saida


def lw(rd, rs1, imm):
    saida = converter_int_bin(imm)
    saida += registradores[rs1]
    saida += "010"
    saida += registradores[rd]
    saida += "0000011"
    return saida


def beq(rs1, rs2, imm):
    imm -= 1000
    imm = str(imm)
    while len(imm) < 13:
        imm = "1" + imm
    saida_aux = imm
    saida = saida_aux[0]
    for i in range(6):
        saida +=  saida_aux[2 + i]
    saida += registradores[rs2]
    saida += registradores[rs1]
    saida += "000"
    for i in range(4):
        saida += saida_aux[7 + i]
    saida += saida_aux[1]
    saida += "1100011"
    return saida



def ret():
    #JALR zero, ra, 0
    saida = "000000000000"
    saida += registradores["ra"]
    saida += "000"
    saida += registradores["zero"]
    saida += "1100111"
    return saida


def call(imm):
    #JAL ra destino com -1000 no destino
    imm -= 1000
    saida_aux = converter_int_bin_32(imm)
    saida = saida_aux[11]
    for i in range(10):
        saida += saida_aux[21 + i]
    saida += saida_aux[20]
    for i in range(8):
        saida += saida_aux[12 + i]
    saida += registradores["ra"]
    saida += "1101111"

    return saida


def xor(rd, rs1, rs2):
    saida = "0000000"
    saida += registradores[rs2]
    saida += registradores[rs1]
    saida += "100"
    saida += registradores[rd]
    saida += "0110011"
    return saida

def slli(rd, rs1, shamt):
    saida = "0000000"
    saida += converter_int_bin(shamt)
    saida += registradores[rs1]
    saida += "001"
    saida += registradores[rd]
    saida += "0010011"
    return

def addi(rd, rs1, imm):
    saida = converter_int_bin(imm)
    saida += registradores[rs1]
    saida += "000"
    saida += registradores[rd]
    saida += "0010011"
    return saida

registradores = {}
registradores["s0"] = "01000"   # s0 = x8
registradores["s1"] = "01001"   # s1 = x9
registradores["s2"] = "10010"   # s2 = x18
registradores["s3"] = "10011"   # s3 = x19
registradores["s4"] = "10100"   # s4 = x20
registradores["s5"] = "10101"   # s5 = x21
registradores["s6"] = "10110"   # s6 = x22
registradores["s7"] = "10111"   # s7 = x23
registradores["s8"] = "11000"   # s8 = x24
registradores["s9"] = "11001"   # s9 = x25
registradores["s10"] = "11010"  # s10 = x26
registradores["s11"] = "11011"  # s11 = x27

registradores["zero"] = "00000" # zero = x0
registradores["ra"] = "00001"   # ra = x1
registradores["sp"] = "00010"   # sp = x2
registradores["gp"] = "00011"   # gp = x3
registradores["tp"] = "00100"   # tp = x4
registradores["t0"] = "00101"   # t0 = x5
registradores["t1"] = "00110"   # t1 = x6
registradores["t2"] = "00111"   # t2 = x7

registradores["a0"] = "01010"   # a0 = x10
registradores["a1"] = "01011"   # a1 = x11
registradores["a2"] = "01100"   # a2 = x12
registradores["a3"] = "01101"   # a3 = x13
registradores["a4"] = "01110"   # a4 = x14
registradores["a5"] = "01111"   # a5 = x15
registradores["a6"] = "10000"   # a6 = x16
registradores["a7"] = "10001"   # a7 = x17

registradores["t3"] = "11100"   # t3 = x28
registradores["t4"] = "11101"   # t4 = x29
registradores["t5"] = "11110"   # t5 = x30
registradores["t6"] = "11111"   # t6 = x31



while True:
    entrada = input("Digite sua instrução: \n").split()
    if not entrada:
        print("Programa finalizado!")
        break
    if entrada[0] == "addi":
        entrada[1] = entrada[1][:-1]
        entrada[2] = entrada[2][:-1]
        saida = addi(entrada[1], entrada[2], int(entrada[3]))
    elif entrada[0] == "slli":
        saida = slli(entrada[1], entrada[2], int(entrada[3]))
    elif entrada[0] == "xor":
        saida = xor(entrada[1], entrada[2], entrada[3])
    elif entrada[0] == "call":
        saida = call(int(entrada[1]))
    elif entrada[0] == "ret":
        saida = ret()
    elif entrada[0] == "beq":
        entrada[1] = entrada[1][:-1]
        entrada[2] = entrada[2][:-1]
        saida = beq(entrada[1], entrada[2], int(entrada[3]))
    elif entrada[0] == "lw":
        #ler entrada no tipo x, y(z) com y podendo ser até 99
        entrada[1] = entrada[1][:-1]
        imm = 0
        registrador = ""
        if len(entrada[2]) == 5:
            registrador += entrada[2][2]
            registrador += entrada[2][3]
            imm = entrada[2][0]
        elif len(entrada[2]) == 6:
            registrador += entrada[2][3]
            registrador += entrada[2][4]
            imm = entrada[2][0]
            imm += entrada[2][1]
        saida = lw(entrada[1], registrador, int(imm))
    elif entrada[0] == "sw":
        #ler entrada no tipo x, y(z) com y podendo ser até 99
        entrada[1] = entrada[1][:-1]
        imm = 0
        registrador = ""
        if len(entrada[2]) == 5:
            registrador += entrada[2][2]
            registrador += entrada[2][3]
            imm = entrada[2][0]
        elif len(entrada[2]) == 6:
            registrador += entrada[2][3]
            registrador += entrada[2][4]
            imm = entrada[2][0]
            imm += entrada[2][1]
        saida = sw(registrador, entrada[1], int(imm))
    elif entrada[0] == "mul":
        entrada[1] = entrada[1][:-1]
        entrada[2] = entrada[2][:-1]
        saida = mul(entrada[1], entrada[2], entrada[3])
    elif entrada[0] == "lui":
        entrada[1] = entrada[1][:-1]
        saida = lui(entrada[1], int(entrada[2]))
    elif entrada[0] == "li":
        entrada[1] = entrada[1][:-1]
        saida = li(entrada[1], int(entrada[2]))
    else:
        saida = "Não é uma instrução suportada"
    saida = hex(int(saida, 2))
    saida = saida[2:].zfill(8)
    saida = "0x" + saida
    print("A instrução em hexacimal é:", saida)

