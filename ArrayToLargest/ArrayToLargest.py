from collections import defaultdict

input = [1, 34, 3, 98, 9, 76, 45, 4]

def checksimilar(lendict, lengths, j, strin):
	for k in lendict[lengths[j]]:
		if strin[-1] == str(k)[0]:
			return str(k)[0]
	return -1

def normaliseinput(input):
	norminput = []
	lendict = defaultdict(list)
	lengths = []
	# All input numbers
	for i in input:
		# Append the length to dictionary
		lendict[len(str(i))].append(i)
		# Get all the lengths for sorted order
		if len(str(i)) not in lengths:
			lengths.append(len(str(i)))
			
	lengths = sorted(lengths)
	# Start to normalise
	for i in range(len(lengths)):
		for number in lendict[lengths[i]]:
			strin = str(number)
			for j in range(i+1,(len(lengths))):
				if checksimilar(lendict, lengths, j, strin) != -1:
					strin += str(checksimilar(lendict, lengths, j, strin))
				else:
					# Add max first number in length dict
					strin += str(max(lendict[lengths[j]]))[0]
			norminput.append([int(strin),number])
			
	norminput = sorted(norminput, reverse=True)
	ans = ""
	for i in norminput:
		ans += str(i[1])
	return int(ans)

print(normaliseinput(input))