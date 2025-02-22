from dataclasses import dataclass
import random,string
@dataclass
class Player:
	name: str
	guess: int=1
n = input("Name: ")
def input_check():
	c = input("Code: ")
	ch = lambda c: all([i in string.digits for i in c])
	while len(c)!=4 or not ch(c) or len(c)!=len(set(c)):
		print("The length of the code is 4 digits and all digits are unique.")
		c = input("Code: ")
	return c
p1 = Player(n)
def game(p):
	code = random.sample(string.digits,4)
	c = input_check()
	def bulls_cows(c):
		a = sum([i==j for i,j in zip(code,c)])
		b = sum([i in c for i in code])-a
		return b,a
	while code != c:
		bc=bulls_cows(c)
		print(f"{bc[0]} bulls, {bc[1]} cows")
		p.guess+=1
		c = input_check()
game(p1)
print(p1.guess)
