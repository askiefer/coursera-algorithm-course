count = 0

def num_inversions(x):
    """Given an array, counts the number of inversions needed to sort the array"""
    midsection = len(x) / 2
    leftArray = x[:midsection]
    rightArray = x[midsection:]
    if len(x) > 1:

        num_inversions(leftArray)
        num_inversions(rightArray)
        
        i, j = 0, 0
        a = leftArray; b = rightArray
        for k in range(len(a) + len(b) + 1):
            if a[i] <= b[j]:
                x[k] = a[i]
                i += 1
                if i == len(a) and j != len(b):
                    while j != len(b):
                        k +=1
                        x[k] = b[j]
                        j += 1
                    break
            elif a[i] > b[j]:
                x[k] = b[j]
                count += (len(a) - i)
                j += 1
                if j == len(b) and i != len(a):
                    while i != len(a):
                        k+= 1
                        x[k] = a[i]
                        i += 1                    
                    break   
    return x

if __name__ == "__main__":
	with open('coursera.txt') as f:
		l = [int(x) for x in f]

		num_inversions(l)
		print count
