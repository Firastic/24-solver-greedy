def dist(x):
	return abs(24-x)

def solve(arr):
	arr.sort()
	total = sum(arr)
	cur = arr[3]
	vall = 0
	flag = False
	v = []
	if(total <= 20 and arr[3]*arr[2] > 35):
		if(arr[0] != 1):
			arr[0],arr[2] = arr[2],arr[0]
		else:
			arr[1],arr[2] = arr[2],arr[1]
	for j in range(2,-1,-1):
		if(cur*arr[j] >= 6 and cur*arr[j] <= 35 and (arr[j] != 1 or cur == 24) and not flag):
			v.append('*');
			vall += 3;
			cur *= arr[j];
		else:
			flag = True;
			if(dist(cur+arr[j]) <= dist(cur-arr[j])):
				v.append('+');
				vall += 5;
				cur += arr[j];
			else:
				v.append('-');
				vall += 4;
				cur -= arr[j];			
	arr.reverse()
	for j in range(4):
		print(arr[j],end=' ')
		if(j < 3):
			print(v[j],end=' ')


