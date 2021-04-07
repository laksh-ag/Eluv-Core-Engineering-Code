filename_1 = './sample.1'
filename_2 = './sample.2'
filename_3 = './sample.3'
filename_4 = './sample.4'
filename_5 = './sample.5'
filename_6 = './sample.6'
filename_7 = './sample.7'
filename_8 = './sample.8'
filename_9 = './sample.9'
filename_10 = './sample.10'

file_arr = []
for i in range(1,11):
    file_arr.append("./Data/sample.{0}".format(i))                              # Store all the files in an array

ans = 0
files = []
index_1,index_2 = -1,-1
for l in range(10):
    file1 = open(file_arr[l],encoding = 'ISO_8859_1')                           # Pick 1st file to compare
    s1 = file1.read()
    for m in range(l+1,10):
        file2 = open(file_arr[m],encoding = 'ISO_8859_1')                       # Pick 1st file to compare
        s2 = file2.read()
        arr = [[0 for i in range(len(s1))]for j in range(len(s2))]              # Initialize array to find longest string
        d = 0
        tindex_1 = -1
        tindex_2 = -1
        for i in range(len(s1)):                                                # Evaluating the first row
            if ord(s2[0])==ord(s1[i]):
                arr[0][i] = 1
                d = 1
                tindex_1 = i

        for i in range(len(s2)):                                                # Evaluating the first column
            if ord(s1[0])==ord(s2[i]):
                arr[i][0] = 1
                d = 1
                tindex_2 = i

        for i in range(1,len(s2)):
            for j in range(1,len(s1)):
                if ord(s1[j]) == ord(s2[i]):                                    # Checking the when same letters are found in the files
                    arr[i][j] = arr[i-1][j-1]+1
                    if arr[i][j]>d:
                        d = arr[i][j]
                        tindex_1 = j-arr[i][j]+1
                        tindex_2 = i-arr[i][j]+1
        if d>ans:                                                               # Storing files and offset values for longest strand found
            ans = d
            files = [file_arr[l],file_arr[m]]
            index_1 = tindex_1
            index_2 = tindex_2
        # print(files,l,m)
        del(arr)
print('The files that contain the strands are',files[0],'and',files[1],'.')
print('The byte offset for',files[0],'is',index_1,'and for',files[1],'is',index_2)
