def solution(inp_str):
    out_str = ''
    ascii = [' ', 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    braille = ['000000','100000','110000','100100','100110','100010','110100','110110','110010','010100','010110','101000','111000','101100','101110','101010','111100','111110','111010','011100','011110','101001','111001','010111','101101','101111','101011']
    
    for i in range(len(inp_str)):
        if inp_str[i].isupper():
            out_str = out_str + '000001'
        
        out_str = out_str+braille[ascii.index(inp_str[i].lower())]

    return out_str

print(type(solution('The quick brown fox jumps over the lazy dog')))