# -*- coding: utf-8 -*- 
import sys
def show_all_cols(line):
	cols=line.split( )
	for i in range(len(cols)):
		print str(i+1)+"--- "+cols[i]

def show_col(log_file):
	need_print_cols=sys.argv[3].split(',')
	for line in log_file:
		cols=line.split( )
		for i in range(len(cols)):
			if str(i) in need_print_cols:
				print cols[i],
		print '\n'

def main():
	if len(sys.argv) < 2: 
		print "not enough parameters"
		return

	try:
		log_file=open(sys.argv[1],"r")
	except Exception as e:
		print "can't read file "+sys.argv[1]+"."
		return

	if len(sys.argv) < 3: 
		show_all_cols(log_file.readline())
	else:
		if (sys.argv[2]=="--show-col"):#--show-col 1,3,4,5,6
			show_col(log_file)
			return
		#if (sys.argv[2]=="--xxxx"):


if __name__ == '__main__':
	main()
