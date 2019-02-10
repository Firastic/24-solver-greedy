def dist(x):
	return abs(24-x)

def solve(arr):
	op = []
	vall = 0
	flag = False

	#Mengurutkan angka-angka
	arr.sort()
	total = sum(arr)
	cur = arr[3]
	
	#Menukar angka kedua terbesar dan ketiga terbesar jika kondisi memenuhi
	if(total <= 20 and arr[3]*arr[2] >= 32 and arr[1] != 1):
		arr[1],arr[2] = arr[2],arr[1]

	#Menjalankan algoritma pemberian operasi
	for j in range(2,-1,-1):
		#Jika perkalian akan memberikan hasil yang cukup optimal untuk saat ini, lakukan
		if(cur*arr[j] >= 6 and cur*arr[j] <= 35 and ((arr[j] != 1 and not flag) or (cur == 24 and j == 0))):
			op.append('*');
			vall += 3;
			cur *= arr[j];
		else:
			flag = True;
			if(dist(cur+arr[j]) <= dist(cur-arr[j])): #Melakukan operasi penambahan
				op.append('+');
				vall += 5;
				cur += arr[j];
			else: #Melakukan operasi pengurangan
				op.append('-');
				vall += 4;
				cur -= arr[j];		

	arr.reverse()
	#Output
	for j in range(4):
		print(arr[j],end=' ')
		if(j < 3):
			print(op[j],end=' ')


