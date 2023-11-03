def arrayManipulation(n, queries):
  
  for a, b, k in queries:
      prefix_sum[a] += k
      prefix_sum[b + 1] -= k
  
  running_total = 0
  maximum_value = 0
  
  for i in prefix_sum:
      running_total += i
      maximum_value = max(running_total, maximum_value)
  
  return maximum_value
