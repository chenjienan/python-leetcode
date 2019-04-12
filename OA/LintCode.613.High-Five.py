# 613. High Five

# There are two properties in the node student id and scores, to ensure that 
# each student will have at least 5 points, find the average of 5 highest 
# scores for each person.

# 样例
# Example 1:

# Input: 
# [[1,91],[1,92],[2,93],[2,99],[2,98],[2,97],[1,60],[1,58],[2,100],[1,61]]
# Output:
# 1: 72.40
# 2: 97.40

# Example 2:

# Input:
# [[1,90],[1,90],[1,90],[1,90],[1,90],[1,90]]
# Output: 
# 1: 90.00
import heapq
'''
Definition for a Record
class Record:
    def __init__(self, id, score):
        self.id = id
        self.score = score
'''
class Solution:
    # @param {Record[]} results a list of <student_id, score>
    # @return {dict(id, average)} find the average of 5 highest scores for each person
    # <key, value> (student_id, average_score)
    def highFive(self, results):
        if not results: return 0.0

        # d is a dictionary storing student id as key 
        # and a heap of top five scores
        ret, d = {}, {}

        for std in results:
            if std.id not in d:
                d[std.id] = [std.score]
            else:
                heapq.heappush(d[std.id], std.score)
                if len(d[std.id]) > 5:
                    heapq.heappop(d[std.id])

        # sum up the scores for each student and put it
        # into a dictionary
        for id, scores in d.items():
            ret[id] = sum(scores) / 5.0

        return ret