# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 07:21:06 2021

@author: Dhanajayan
"""
def  frame_sentence():
    T = int(input('Enter the number of test cases'))
    
    if T >= 1 and T<=100:
        
        N = int(input("Enter number of words for dict : "))
        word_dict = [] 
        if N >= 1 and N <= 20:
            # iterating till the range 
            
            for i in range(0, N):
                word = input("enter word")
                if len(word) <= 15:
                    word_dict.append(word) # adding the element 
                    
                else:
                    
                    word = input("enter word below the length 15")
                    word_dict.append(word) # adding the element
                    
         
        else:
            return 'Input words exceeds the limt'
                    
    else:
        return 'test cases limit exceeds'
        
        
    
    S = input('Enter the test string')
    if len(S) <= 1000:
        s = S
    else:
        
        s = input('enter the string length less than 1000')
        
        
    result = []
    word_dict_len = len(max(word_dict, key=len))
    length = len(s) + 1
    for j in range(1,length):
        i = j - 1
        flag = 0
        ans = []
        x = 0
        # Letting setting x to j - max_l optimization,
        # the code will work even if x is always set to 0
        if j > word_dict_len:
            x = j - word_dict_len
        while(i >= x):
            if s[i:j] in word_dict:
                if i > 0 and result[(i - 1)]:

                        temp = list((map(lambda x : x + " "+ s[i:j],\
                        result[(i - 1)])))
                        for elem in temp:
                            ans.append(elem)
                        flag = 2
                else:
                    flag = 1
                    result.append([s[i:j]])
            i=i-1
        if flag == 0:
            result.append([])
        if flag == 2:
            result.append(ans)
    if s in word_dict:
      result[len(s) - 1].append(s)
    
    temp = ", result [{}]: "
    
    return  result[len(s) - 1]


if __name__ == "__main__":
   frame_sentence()
