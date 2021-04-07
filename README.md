# Eluv-Core-Engineering-Code

This is the code for Eluv Core-Software-Engineer Challenge. Here, we have 10 files and we need to find which file names that contain the largest common strand and the byte offset where the strand occurs in each file. 

Here we take two files and find the largest common strand between them and the byte offset of that string in each file. We do this with every possible combination of files. So, the total number of comparisons that we need are - 10*(10-1)/2 which is 45 files(Since, there are 10 files and we compare two files each time).

To find the longest common string, we use dynamic programming. We take *m.n* array where m is the length of say file1 and n is the length of file2. Intially all the values in the array are zero. We iterate over the array and for any cell at (i,j) position in the array. We compare the letter at $i{th}$
