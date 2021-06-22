import sys
from typing import List

class Solution:

  def __init__(self) -> None:
      self.limit = (2**32)-1
      self.stack_operators = []
      self.polish_result = []
      self.stack_opperands = []
      self.agrupation = {
        ")":"(",
        "]":"["
      }

  def __applyOperation(self, current,previous,operator):
    operate_actions = {
      "+":lambda current_value,value_to_add : current_value + value_to_add if current_value<self.limit-value_to_add else -1,
      "*": lambda current_value,value_to_multiply: current_value * value_to_multiply if current_value<self.limit//value_to_multiply else -1
    }
    return operate_actions[operator](current,previous)


  def __partial_operation(self,operator)->int:
    result = self.__applyOperation(
                                self.stack_opperands.pop(),
                                self.stack_opperands.pop(),
                                operator)
    self.stack_opperands.append(result)
    return result

  def get_priority(self,operator):
    priority_dic = {
      "[":0,
      "(":0,
      "+":1,
      "*":2
    }
    return priority_dic[operator]

  def __polish_notation(self,equation:List[str])->None:
    size = len(equation)
    for _ in range(size):
      element = equation.pop(0)
      if element.isalnum():
        self.polish_result.append(element)
      elif element =="[" or element =="(":
        self.stack_operators.append(element)
      elif element in self.agrupation :
            operator = self.stack_operators.pop()
            open_sign = self.agrupation[element]
            while self.stack_operators and operator!=open_sign:
              self.polish_result.append(operator)
              operator = self.stack_operators.pop()
      else:
        while (self.stack_operators and
              self.get_priority(self.stack_operators[-1])>=self.get_priority(element)):
              self.polish_result.append(self.stack_operators.pop())
        self.stack_operators.append(element)

    while self.stack_operators:
      self.polish_result.append(self.stack_operators.pop())

  def __evaluate_result(self):
    size = len(self.polish_result)
    for index in range(size):
      element = self.polish_result[index]
      if element.isalnum():
        self.stack_opperands.append(int(element))
      elif len(self.stack_opperands)>1:
        result = self.__partial_operation(element)
        if result == -1:
          return "OVERFLOW!!!"
    return self.stack_opperands[0]

  def catch_overflow(self, equation:List[str])->str:
    self.__polish_notation(equation)
    return self.__evaluate_result()


if __name__ == '__main__':
    s = Solution()
    total_users = int(sys.stdin.readline())
    prefix_expresion = []

    counter = 0
    for _ in range(total_users):
      instruction = sys.stdin.readline().rstrip()
      if "for" in  instruction:
        [loop, value] = instruction.split(" ")
        if counter>0:
          prefix_expresion.append(str(counter))
          prefix_expresion.append("+")
          counter = 0
        prefix_expresion.append("[")
        prefix_expresion.append(value)
        prefix_expresion.append("*")
        prefix_expresion.append("(")
      elif "add" in instruction:
          counter+=1
      elif "end" in instruction:
        prefix_expresion.append(str(counter))
        prefix_expresion.append(")")
        prefix_expresion.append("]")
        prefix_expresion.append("+")
        counter = 0
    if len(prefix_expresion) == 0:
      print(counter)
    else:
      prefix_expresion.append("0")
      sexpt = map(lambda x :str(x),prefix_expresion)
      print("".join(sexpt))
      print(s.catch_overflow(prefix_expresion))
