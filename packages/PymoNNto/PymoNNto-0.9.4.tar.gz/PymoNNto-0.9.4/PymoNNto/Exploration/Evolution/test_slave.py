from PymoNNto.Exploration.Evolution.Interface_Functions import *

print(sys.argv)

print('slave')

print('genes: ', get_genome())
print('gene a: ', get_gene('a', None))
print('gene b: ', gene('b', 1))

score = get_gene('a', 0) + get_gene('b', 0)

set_score(score)
