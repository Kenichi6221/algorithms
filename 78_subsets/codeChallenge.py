class Solution:
    def get_candidates(self):
        return [True,False]

    def is_a_solution(self, kth_element, original_set_size):
        return kth_element==original_set_size

    def process_solution(self,subset, final_collection):
        final_collection.append(subset.copy())

    def backtrack(self,original_array,subset,final_collection,original_set_size,kth_element):
        if self.is_a_solution(kth_element,original_set_size):
            self.process_solution(subset,final_collection)
        else:
            options = self.get_candidates()
            for option in options:
                if option:
                    subset.append(original_array[kth_element])
                self.backtrack(original_array,subset,final_collection,original_set_size,kth_element+1)
                if option:
                    subset.pop()

    def subsets(self, nums: List[int]) -> List[List[int]]:
        final_collection = []
        self.backtrack(nums,[],final_collection,len(nums),0)
        return final_collection