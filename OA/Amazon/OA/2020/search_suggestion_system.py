


def suggestedProducts(products, searchWord):
  # assumming products and searchWord is not null or empty                
  products.sort()
  res = []
  search = ""
  for ch in searchWord:
    search += ch
    suggestion = []
    word_num = min(3, len(products))
    
    for i in range(len(products)):
      if word_num == 0:
        break
      if search == products[i][0: len(search)]:
        suggestion.append(products[i])
        word_num -= 1
    res.append(suggestion)
      
  return res