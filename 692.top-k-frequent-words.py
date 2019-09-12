#
# @lc app=leetcode id=692 lang=python
#
# [692] Top K Frequent Words
#
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        # {key word, value freq}
        word_freq = {}
        for w in words:
            word_freq[w] = word_freq.get(w, 0) + 1
        
        # max heap with tuple (freq, word)
        import heapq
        heap = []
        for word, freq in word_freq.items():
            heapq.heappush(heap, (-freq, word))
          
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res
          
            


