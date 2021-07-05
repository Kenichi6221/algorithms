def get_candidates(target,power):
  start = 1
  candidates = []

  while start**power<=target:
    candidates.append(start**power)
    start+=1

  return candidates

def get_options():
  return [True,False]

def is_solution(current):
  return current == 0

def backtrac(target,candidates,kth,tracer):
  result = 0
  if is_solution(target):
    #print(f"tracer: {tracer}")
    return 1
  if kth == len(candidates):
    return 0
  if target<0:
    return 0
  else:
    options = get_options()
    for option in options:
      if option:
        target-=candidates[kth]
        tracer.append(candidates[kth])
      result+=backtrac(target,candidates,kth+1,tracer)
      if option:
        target+=candidates[kth]
        tracer.pop()
  return result

def powerSum(X, N):
    candidates = get_candidates(X,N)
    return backtrac(X,candidates,0,[])

if __name__ == '__main__':
    print(powerSum(100,2))