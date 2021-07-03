from typing import List

class Solution:
    def generate_candidates(self, permuted_indexes:List[int] ,required_elements:int)->List[int]:
        available_positions = [True]*required_elements

        for index in permuted_indexes:
            available_positions[index] = False

        available_index = []
        for index in range(required_elements):
            if available_positions[index]:
                available_index.append(index)

        return available_index

    def is_valid_solution(self, permuted_indexes:List[int], required_size:int)->bool:
        return len(permuted_indexes) == required_size

    def process_solution(self, permuted_indexes:List[int], all_permutations:List[int], original_set:List[int]):
        permutate_elements = []
        for index in permuted_indexes:
            permutate_elements.append(original_set[index])
        all_permutations.append(permutate_elements)

    def backtrack(self, permuted_indexes:List[int], all_permutations: List[int], original_set:List[int], required_elements: int):
        if self.is_valid_solution(permuted_indexes,required_elements):
            self.process_solution(permuted_indexes,all_permutations,original_set)
        else:
            candidates = self.generate_candidates(permuted_indexes,required_elements)
            for candidate in candidates:
                permuted_indexes.append(candidate)
                self.backtrack(permuted_indexes,all_permutations,original_set,required_elements)
                permuted_indexes.pop()

    def permute(self, nums: List[int]) -> List[List[int]]:
        cardinal = len(nums)
        if cardinal == 1:
            return [nums]
        all_permutations = []
        self.backtrack([],all_permutations,nums,cardinal)
        return all_permutations

if __name__ == '__main__':
    s = Solution()
    test = [1,2]
    print(s.permute(test))