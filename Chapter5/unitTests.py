def main():
    health = 100
    resist = 5
    amp = 2
    spell_power = 20
    take_magic_damage(health, resist, amp, spell_power)

def take_magic_damage(health, resist, amp, spell_power):
    total_damage = spell_power * amp
    print(total_damage)
    new_health = health - (total_damage - resist)
    print(health)
    print(resist)
    print(new_health)
    return new_health

main()