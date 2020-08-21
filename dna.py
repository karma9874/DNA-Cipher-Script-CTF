import sys

bin_dna = {'00':'A','10':'C','01':'G','11':'T'}
mapping = {
        'AAA':'a','AAC':'b','AAG':'c','AAT':'d','ACA':'e','ACC':'f', 'ACG':'g','ACT':'h','AGA':'i','AGC':'j','AGG':'k','AGT':'l','ATA':'m','ATC':'n','ATG':'o','ATT':'p','CAA':'q','CAC':'r','CAG':'s','CAT':'t','CCA':'u','CCC':'v','CCG':'w','CCT':'x','CGA':'y','CGC':'z','CGG':'A','CGT':'B','CTA':'C','CTC':'D','CTG':'E','CTT':'F','GAA':'G','GAC':'H','GAG':'I','GAT':'J','GCA':'K','GCC':'L','GCG':'M','GCT':'N','GGA':'O','GGC':'P','GGG':'Q','GGT':'R','GTA':'S','GTC':'T','GTG':'U','GTT':'V','TAA':'W','TAC':'X','TAG':'Y','TAT':'Z','TCA':'1','TCC':'2','TCG':'3','TCT':'4','TGA':'5','TGC':'6','TGG':'7','TGT':'8','TTA':'9','TTC':'0','TTG':' ','TTT':'.'}

def bin_2_code(string):
	string = string.replace(" ","")
	string = string.replace("\n","")
	final=""
	for j in range(0,len(string),2):
		final+=bin_dna[string[j:j+2]]
	return final

def decode_dna(string):
    final=""
    for i in range(0,len(string),3):
        final+=mapping[string[i:i+3]]
    return final

if len(sys.argv) < 2:
	print("Usage: python dna.py [file_name]")
else:
	input_string = open(sys.argv[1]).read().replace(" ","")
	print(" ")
	print(decode_dna(bin_2_code(input_string)))