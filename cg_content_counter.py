file_name = input('Please input a gene sequence file: ')
lzt = []
with open(file_name) as seq:
    for line in seq.readlines():
        if not line.startswith('>'):
            lzt.append(line.strip())

full_seq = ''.join(lzt).upper()

dik = {}
for letter in full_seq:
    dik[letter] = full_seq.count(letter)

total = len(full_seq)
cg_count = dik['C'] + dik['G']
cg_ratio = cg_count / total

print('Total nucleotides in sequence:', total)
print('CG Count:', cg_count)
print('CG Ratio:', cg_ratio)