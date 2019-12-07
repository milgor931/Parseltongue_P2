lst_1 = [False,True,True,None,True,None,None,False,False,None,True,False]
lst_2 = ["or","or","or","==","!=","==","and","==","!=","and","==","or"]
lst_3 = [False,False,None,None,True,True,False,True,None,False,True,None]

for x in range(len(lst_1)):
  evaluated = str(lst_1[x]) + " " + lst_2[x] + " " + str(lst_3[x])
  print(str(lst_1[x]) + " " + lst_2[x] + " " + str(lst_3[x]) + " => " + str(eval(evaluated)))
