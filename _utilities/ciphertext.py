cipher = "Dnsbosgem qgqymucu cu ixs vnhesuu hd slqfcgcgz xhk hdisg ysiisnu hn umfwhyu qvvsqn cg q ecvxsnisli ih ogehjsn asiqcyu qwhoi ixs ogasnymcgz vyqcgisli. Ixcu fsixha ysjsnqzsu ixs dqei ixqi esniqcg ysiisnu hn umfwhyu heeon fhns dnsbosgiym ixqg hixsnu cg qgm zcjsg yqgzoqzs. Dhn cguiqges, cg Sgzycux, ixs ysiisnu S, I, Q, H, qga C qns ixs fhui ehffhg, kxcys ysiisnu ycts P, B, qga L qns nqnsn. Wm casgicdmcgz ixs fhui dnsbosgi exqnqeisnu, dnsbosgem qgqymucu eqg nsjsqy vqiisngu qga vhisgicqyym qca cg asenmvicgz ixs fsuuqzs."
cipher = cipher.upper()

replacement_dict = {
    'S' : 'E',
    'I' : 'T',
    'X' : 'H',
    'D' : 'F',
    'N' : 'R',
    'B' : 'Q',
    'O' : 'U',
    'G' : 'N',
    'E' : 'C',
    'M' : 'Y',
    'Q' : 'A',
    'Y' : 'L',
    'U' : 'S',
    'C' : 'I',
    'V' : 'P',
    'H' : 'O',
    'L' : 'X',
    'A' : 'D',
    'F' : 'M',
    'J' : 'V',
    'W' : 'B',
    'Z' : 'G',
    'K' : 'W',
    'T' : 'K'
}

plaintext = ""
for char in cipher:
    plaintext += replacement_dict.get(char, char)

print(cipher)
print()
print(plaintext)