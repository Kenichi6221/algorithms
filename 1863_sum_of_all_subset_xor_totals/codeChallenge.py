from typing import List

class Solution:
    def process_solution(self,subset, totalized_array:List[int]):
        if subset:
            size_subset = len(subset)-1
            result = subset[0]

            while size_subset>0:
                result^=subset[size_subset]
                size_subset-=1

            totalized_array[0]+=result


    def is_a_solution(self, k, required_k)->bool:
        return k == required_k

    def get_candidates(self)->List[bool]:
        return [True, False]

    def backtraking(self, subset: List[int], nums: List[int], totalized_array:List[int], original_set_size:int,current_element:int):
        if self.is_a_solution(current_element,original_set_size):
            self.process_solution(subset,totalized_array)
        else:
            options = self.get_candidates()
            for option in options:
                if option:
                    subset.append(nums[current_element])
                self.backtraking(subset,nums,totalized_array,original_set_size,current_element+1)
                if option:
                    subset.pop()

    def subsetXORSum(self, nums: List[int]) -> int:
        totalized_elements = [0]
        self.backtraking([],nums,totalized_elements,len(nums),0)
        return totalized_elements[0]