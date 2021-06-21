import sys
class Solution:

  def __init__(self) -> None:
      self.users_dictionary = {}

  def regitstrate_user(self, name:str)->str:
    restult = "OK"
    if name in self.users_dictionary:
      counter = self.users_dictionary[name]+1
      restult = f"{name}{counter}"
      self.users_dictionary[name]+=1
    else:
      self.users_dictionary[name] = 0
    return restult

if __name__ == '__main__':
    s = Solution()
    total_users = int(sys.stdin.readline())
    for _ in range(total_users):
      name = sys.stdin.readline().rstrip()
      print(s.regitstrate_user(name))
