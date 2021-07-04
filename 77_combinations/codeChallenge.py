class Solution:
    def is_a_solution(self,subset,k_required,max_kth,kth):
        return len(subset)==k_required or max_kth == kth

    def process_solution(self,subset,final_collection, k_required):
        if len(subset) == k_required:
            final_collection.append(subset.copy())

    def get_candidates(self):
        return [True,False]

    def backtracking(self, original_array,subset,final_collection,k_required,max_kth,kth):
        if self.is_a_solution(subset,k_required,kth,max_kth):
            self.process_solution(subset,final_collection,k_required)
        else:
            options = self.get_candidates()
            for option in options:
                if option:
                    subset.append(original_array[kth])
                self.backtracking(original_array,subset,final_collection,k_required,max_kth,kth+1)
                if option:
                    subset.pop()

    def combine(self, n: int, k: int) -> List[List[int]]:
        if n==k:
            original_array = [element for element in range(1,n+1)]
            return [original_array]
        if k == 1:
            result = []
            for element in range(1,n+1):result.append([element])
            return result
        original_array = [element for element in range(1,n+1)]
        final_collection = []
        self.backtracking(original_array,[],final_collection,k,len(original_array),0)
        return final_collection