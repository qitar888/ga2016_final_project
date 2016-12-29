import cost_function as cf
import pic_sk as pic
import genetic_programming as gp
from random import random, randint, choice
import MonteCarlo as mc

horizontal = gp.cut('H',2)
vertical = gp.cut('V',2)

def examplefun(x, y):
    return x+2*y

def constructcheckdata(count=10):
  checkdata = []
  for i in range(0, count):
    dic = {}
    x = randint(0, 10)
    y = randint(0, 10)
    dic['x'] = x
    dic['y'] = y
    dic['result'] = examplefun(x, y)
    checkdata.append(dic)
  return checkdata


checkdata = constructcheckdata(count = 10)

x = 50
y = 50

# gp
target_image = pic.pic2rgb("../data/img03.jpg", x, y)
cf.set_target_image(target_image)
env = gp.enviroment([horizontal, vertical], ["L color"],
                    [-3, -2, -1, 1, 2, 3], checkdata, target_image, size = 1, maxcut = 15, maxdepth = 3)
s = env.envolve(maxgen = 1)
rgbmatrix = cf.to_array(s, x, y, 1)
pic.rgb2pic(rgbmatrix, 'LAB')

# monte carlo
# min_cost = -1
# answer = None

# for i in range(10):
#     candidate = cf.to_array(mc.random_tree(5, target_image, x, y, 1), x, y, 1)
    
#     candidate_cost = cf.cost(candidate, target_image)
#     if min_cost == -1 or candidate_cost < min_cost:
#         answer = candidate
#         min_cost = candidate_cost

#pic.rgb2pic(answer, "../data/output03_mc.jpg")
    
