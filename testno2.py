
# Python program to remove to every second
# element until list becomes empty 
def removeSecondNumber(int_list): 
      
    # list starts with 
    # 0 index 
    pos = 2 - 1
    index = 0
    len_list = (len(int_list)) 
      
    # breaks out once the 
    # list becomes empty 
    while len_list > 0:  
      
        index = (pos + index) % len_list 
          
        # removes and prints the required 
        # element 
        print(int_list.pop(index))  
        len_list -= 1
  
# Driver code 
nums = [10, 20, 30, 40]  
removeSecondNumber(nums) 
