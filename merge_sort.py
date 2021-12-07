def merge_sort(arr):
  # base case
  if len(arr) <= 1:
    return arr
  # arr = [12 11 13 7 6 5]
  
  # find mid of the array
  mid = len(arr) // 2 # mid = 3 
  
  # divide the array into an L and R such that 
  L = arr[0:mid] # arr = [12,11, 13]
  
  R = arr[mid:len(arr)] # arr = [7, 6, 5]
  
  # handle each side of the array using merge_sort
  sorted_left = list(merge_sort(L))  # sorted_left = [11, 12, 13]
  sorted_right = list(merge_sort(R)) # sroted_right = [5, 6, 7]
  
  # sorted_left = [11, 12, 13]
  #                 l
  
  # sorted_right = [5, 6, 7]
  #                           r
  
  # arr = [5, 6, 7]
  
  
  # merge the left array with the right array in sorted order using manual iteration, writing over arr
  left_index_iterator = right_index_iterator = arr_index_iterator = 0
  
  while arr_index_iterator < len(arr) and left_index_iterator < len(sorted_left) and right_index_iterator < len(sorted_right):
    el_l = sorted_left[left_index_iterator]
    el_r = sorted_right[right_index_iterator]
    if el_l < el_r:
      arr[arr_index_iterator] = el_l
      left_index_iterator += 1
      arr_index_iterator += 1
    else:
      arr[arr_index_iterator] = el_r
      right_index_iterator += 1
      arr_index_iterator += 1
    
  # sorted_left = [11, 12, 13]
  #                         l
  # # arr = [5, 6, 7, 11, 12, 13]
  while left_index_iterator < len(sorted_left):
      arr[arr_index_iterator] = sorted_left[left_index_iterator]
      left_index_iterator += 1
      arr_index_iterator += 1
      
  while right_index_iterator < len(sorted_right):
      arr[arr_index_iterator] = sorted_right[right_index_iterator]
      right_index_iterator += 1
      arr_index_iterator += 1
    
  return arr
  
  
arr = merge_sort([12, 11, 13, 7, 6, 5])
print(arr)
