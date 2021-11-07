from sys import argv
from re import match

fml = [
	'Bin: 0b{0:0>4b}',
	'Hex: 0x{0:x}',
	'Dec: {0:d}',
	'Oct: 0o{0:o}'
]

help = f'''
Convert number to hex, oct, dec and bin bases.

Usage:

{argv[0]} <format>

Where format must be:
0b<binnumber> - A binary number
0x<hexnumber> - A hexadecimal number
0o<octnumber> - A octal number

Or just using a normal number will be considered as decimal number.
'''

d = {
	r'^\d+$': ((0, 1, 3), 10, 'decimal'),
	r'^0b(0|1)+$': ((1, 2, 3), 2, 'binary'),
	r'^0x[0-9a-f]+$': ((0, 2, 3), 16, 'hexadecimal'),
	r'^0o[1-7]+$': ((0, 1, 2), 8, 'octal')
}

if len(argv) == 1:
	exit('No enough arguments')

for x in argv[1:]:

	if x in ('-h', '--help'):
		exit(help)

op = argv[1]

for x in d:

	if match(x, op):

		print('Converting from %s\n' % d[x][2])

		exit('\n'.join(fml[i] for i in d[x][0]).format(int(op, d[x][1])))

print('No pattern found, try -h to show help.')
