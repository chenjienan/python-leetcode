import re
import heapq
# assumming topToys
def topK(numToys, topToys, toys, numQuotes, quotes):
    # numToys and numQuotes are not quite useful

    

    counter_map = countWords(toys, quotes)
    
    # remove toy that's not in the map
    for toy in toys:
        if counter_map[toy][0] == 0:
            del counter_map[toy]

    heap = []
    for k, v in counter_map.items():
        heapq.heappush(heap, (-v[0], -v[1], k))

    res = []
    for i in range(topToys):
        res.append(heapq.heappop(heap)[2])
        if not heap:
            break

    return res

# ignore case => lower()
# ignore special characters => regex
def countWords(toys, quotes):
    # key: toy (str) value: [occurance count, quote count] 
    counter_map = {toy: [0, 0] for toy in toys}

    for line in quotes:        
        word_in_cur_line = {toy: False for toy in toys}
        processed_line = re.sub("[^a-z ]", "", line.lower())
        for word in processed_line.split():
            if word in counter_map:
                counter_map[word][0] += 1

                if not word_in_cur_line[word]:
                    counter_map[word][1] += 1
                    word_in_cur_line[word] = True
    
    return counter_map


numToys = 6
topToys = 2
toys = ["elmo", "elsa", "legos", "drone", "tablet", "warcraft"]
numQuotes = 6
quotes = [
"Elmo is the hottest of the season! Elmo will be on every kid's wishlist!",
"The new Elmo dolls are super high quality",
"Expect the Elsa dolls to be very popular this year, Elsa!",
"Elsa and Elmo are the toys I'll be buying for my kids, Elsa is good",
"For parents of older kids, look into buying them a drone",
"Warcraft is slowly rising in popularity ahead of the holiday season"
]


print(topK(numToys, topToys, toys, numQuotes, quotes))