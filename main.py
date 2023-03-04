from random import randint

problem_list = [
  "Living Giant Tree", "Alien Flying Saucer",
  "Monster Spirit from the Parallel Universe", "Evil Artificial Intelligence",
  "Parasites That Capture the Brain", "Mutant Centipede", "Mad Godzilla",
  "Black Dragon", "Titanium"
]

problem = problem_list[randint(0, len(problem_list) - 1)]
print("The threat we faced -", problem)

list_of_heroes =[input(), input(), input()]
print("This Superheroes", list_of_heroes,
 "went on a mission")