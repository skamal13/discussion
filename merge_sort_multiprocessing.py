import multiprocessing
from heapq import merge

def merge_sort(arr,send_end=None):
  # base case
  if len(arr) <= 1:
    return arr
  # arr = [12 11 13 7 6 5]
  
  # find mid of the array
  mid = len(arr) // 2 # mid = 3 
  
  # divide the array into an L and R such that 
  L = arr[0:mid] # arr = [12,11, 13]
  
  R = arr[mid:len(arr)] # arr = [7, 6, 5]

  inputs = [L, R]
  pipes = [multiprocessing.Pipe(False) for _ in inputs]
  processes = [multiprocessing.Process(target=merge_sort, args=(input, send_end))
        for input, (recv_end, send_end) in zip(inputs, pipes)]
  for process in processes: process.start()
  for process in processes: process.join()
  results = [recv_end.recv() for recv_end, send_end in pipes]

  #merge results array
  result = list(merge(*results))

  if send_end:
    send_end.send(result)
  else:
    return result
 
  
arr = merge_sort([12, 11, 13, 7, 6, 5])
print(arr)
