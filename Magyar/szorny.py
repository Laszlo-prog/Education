import random

monster_number = 5
                    
monster_hp=[100] * monster_number
print(monster_hp)
player_number = 3
player_hp = [150] * 3
print(player_hp)
monster_dmgmin =10
monster_dmgmax = 20
player_dmgmin = 50
player_dmgmax = 100

def monster_life(monster_hp):
    for i in range(len(monster_hp)):
        if monster_hp[i]>0:
            return True
    return False

    

while monster_life(monster_hp):
     for i in range(len(monster_hp)):
        player_dmg=random.randint(player_dmgmin, player_dmgmax)
        monster_hp[i]-=player_dmg
        print(f"A {i+1} monster life: {monster_hp[i]}")
     for i in range(len(player_hp)):
         monster_dmg=random.randint(monster_dmgmin, monster_dmgmax)
         player_hp[i]=monster_dmg
         print(f"B{i+1}, player life: {player_hp[i]}")

 

#To be continued: https://www.youtube.com/watch?v=6Iav_4ApFqs&t=1384s





