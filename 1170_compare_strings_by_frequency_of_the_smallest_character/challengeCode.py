from typing import List


class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        counter = [0]*257
        query_function = []

        # storage frecuencies for each query
        for query in queries:
            val = -1
            for element in query:
                counter[ord(element)]+=1
            index = 0
            for element in counter:
                if val == -1 and element>0:
                    query_function.append(element)
                    val = element
                counter[index] = 0
                index+=1

        max_val = -1
        words_function = []
        for word in words:
            val = -1
            for element in word:
                counter[ord(element)]+=1
            index = 0
            for element in counter:
                if val == -1 and element>0:
                    words_function.append(element)
                    val = element
                    max_val = max(max_val,element)
                counter[index] = 0
                index+=1

        counter_words = [0]*(max_val+1)

        for element in words_function:
            counter_words[element] += 1

        for index in range(1, max_val+1):
            counter_words[index] += counter_words[index-1]


        for index, element in enumerate(query_function):
            if element<max_val:
                query_function[index] = counter_words[-1] - counter_words[element]
            else:
                query_function[index] = 0

        return query_function