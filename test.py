a = "00000000001101110000000000101011000000000010110000000000001101100000000001011110000000000010110000000000001101100000000001011110000000000010100000000000001110110000000000100100000000000011000000000000001100110000000000101111000000000010100000000000011011000000000000110111000000000011101100000000001101110000000001001000000000000011011100000000001010110000000000101100000000000011011000000000010111100000000000101100000000000011011000000000010111100000000000110110000000000010100000000000001001100000000000110010000000000011000100000000001001110000000001011110000000000010111100000000001011000000000000110001000000000010100000000000010111100000000000110010000000000010100100000000010111100000000000110111000000000010101100000000001010000000000001011110000000000010100000000000001110110000000000100100000000000011000000000000001100110000000000101111000000000010100000000000011011000000000000110111000000000011101100000000001101110000000001001000000000000011011100000000001110110000000000110111"

b = "00000000011101000000000001101000000000000110100100000000011100110000000000100000000000000110100100000000011100110000000000100000000000000110010100000000011110000000000001100001000000000110110100000000011100000000000001101100000000000110010100000000001011100000000001110100000000000111100000000000011101000000000000001010000000000111010000000000011010000000000001101001000000000111001100000000001000000000000001101001000000000111001100000000001000000000000001110011000000000110010100000000011000110000000001101111000000000110111000000000011001000000000000100000000000000110110000000000011010010000000001101110000000000110010100000000001000000000000001101111000000000110011000000000001000000000000001110100000000000110100000000000011001010000000000100000000000000110010100000000011110000000000001100001000000000110110100000000011100000000000001101100000000000110010100000000001011100000000001110100000000000111100000000000011101000000000000001010000000000111010000000000011110000000000001110100"

for i in range(len(a)) :
    if a[i] != b[i] :
        print("ERROR", i)