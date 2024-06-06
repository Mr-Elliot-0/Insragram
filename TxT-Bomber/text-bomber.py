import os
from src import Banner

Banner.banner()

input("Ready ?")

num = 0 

while True:
    os.system(f"touch > {num}.txt")
    num += 1
