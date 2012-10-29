# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(raw_input())
for i in range(0,T): # Run through # of test cases
    iterator = 0
    N = int(raw_input())
    # Read in N elements per line;... Crap, how to do?!
    arr = []
    arr = raw_input().split()
    for j in range (0,N):
		arr[j] = int(arr[j])
    for j in range (1,N): # Insertion sort
        k = j
        #print "%d'th iteration of loop gives us k: " % j, k
        while ((k > 0) and (arr[k] < arr[k-1])):
			#print "compared: %d < %d" %(arr[k], arr[k-1])
			temp = arr[k]
			arr[k] = arr[k-1]
			arr[k-1] = temp
			k = k - 1
			#print "Swap made! Iterator increased."
			iterator += 1
     #      	 print "K: ", k
	#print "J: ", j
	#print "N: ", N
	#print arr
    print iterator # Should be T iterators, increment if sort operation performed
