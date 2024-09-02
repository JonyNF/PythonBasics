def regenerate(current_health, max_health, enemy_distance):
    while current_health < max_health:
        current_health+=1
        print(f"Current health is: ¨{current_health}")
        enemy_distance-=2
        print(f"Enemy distance is: ¨{enemy_distance}")
        if enemy_distance <= 3 :
            print("ENEMY IS TO CLOSE TO REGENERATE!")
            break

    return current_health

def main():
    health = regenerate(10, 20, 12)
    print(health)
main()