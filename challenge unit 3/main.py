def linearSearchproduct(productlist,targetproduct):
  indices=[]

  for index, product in enumerate (productlist):
   if product == targetproduct:
    indices.append(index)

  return indices



product=["shoes","boot","loafer","shoes","sanbal","shoes"]
target="shoes"
target2='apple'
result=linearSearchproduct(product,target2)
print(result)