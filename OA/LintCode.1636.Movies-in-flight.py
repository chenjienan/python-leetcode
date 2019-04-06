# In order to prevent passengers from being too bored during the flight, 
# LQ Airlines decided to play two movies during the flight. Since the movie 
# cannot be played during the take-off and landing of the aircraft, LQ 
# Airlines must ensure that the duration of the two movies to be less than 
# or equal to the flight duration minus 30 minutes, and the total length 
# of the two movies should be as long as possible. Now given t ,the flight 
# duration(minutes), and array dur[],the length of movies. Please output 
# the length of the two movies in order of length. If there are multiple 
# groups of the same length, select the one which contains the longest 
# single moive.It is guarantee that there is a least one solution.

# 30<t<=1000
# dur[i]<=1000
# 1<=len(dur)<=100000

# Have you met this question in a real interview?  
# Example
# Example 1:

# Input：t=87，dur=[20,25,19,37]
# Output：[20,37]
# Explanation:
# 87-30=57
# 20+25=45,57-45=12
# 20+19=39,57-39=19
# 20+37=57,57-57=0
# 25+19=44,57-44=13
# 25+37=62,57<62
# 19+37=56,57-56=1
# Example 2:

# Input：t=67，dur=[20,17,19,18]
# Output：[17,20]
# Explanation:
# 67-30=37
# 17+20=37,18+19=37
# The longest movie in the first group is 20，and 19 in the second grouo, so output`[17,20]`

class Solution:
    """
    @param t: the length of the flight
    @param dur: the length of movies 
    @return: output the lengths of two movies
    """
    def aerial_Movie(self, t, dur):
        # Write your code here
        if t == 0 or not dur:
            return None
            
        target = t - 30
        dur.sort()
        mindiff = sys.maxsize
        res = None
        
        start, end = 0, len(dur) - 1
        while start < end:
            sumval = dur[start] + dur[end]
            diff = target - sumval
            if diff < 0:
                end -= 1
                continue
            if diff < mindiff:
                mindiff = diff
                res = [dur[start], dur[end]]
            if diff == 0:
                start += 1
                end -= 1
            else:
                start += 1
                
        return res