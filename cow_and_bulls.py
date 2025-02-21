from dataclasses import dataclass
import random
@dataclass
class Player:
	name: str
	guess: int=1
n = input("Give your name: ")
p1 = Player(n)
def game(p):
	code = "".join(str(i) for i in random.sample(range(0,9),4))
	c = input("Code: ")
	def bulls_cows(c):a = sum([i==j for i,j in zip(code,c)]);b = sum([i in c for i in code])-a;return b,a
		 
	while code != c:
		bc=bulls_cows(c)
		print(f"{bc[0]} bulls, {bc[1]} cows")
		p.guess+=1
		c = input()
game(p1)
print(p1.guess)
