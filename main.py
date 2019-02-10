from solve import solve
from mainGUI import start_game
import sys

if __name__ == '__main__':
	if(len(sys.argv) == 1):	
		start_game()
	elif(len(sys.argv) != 3):
		print('Please pass 2 arguments')
	else:
		inputFile = sys.argv[1]
		outputFile = sys.argv[2]
		orig_stdout = sys.stdout
		orig_stdin = sys.stdin
		fin = open(inputFile, 'r')
		fout = open(outputFile, 'w')
		sys.stdin = fin
		sys.stdout = fout
		a,b,c,d = map(int, input().split())
		solve([a,b,c,d])
		sys.stdout = orig_stdout
		sys.stdin = orig_stdin
		fin.close()
		fout.close()
		
