def get_quest_status(character):
    pass

def main():
    progress = {
            "entity": {
                "character": {
                    "name": "Sir Galahad",
                    "quests": {
                        "Dragon_Slayer": {
                            "status": "In Progress",
                        },
                        "Goblin_Hunter": {
                            "status": "Completed",
                        },
                    },
                }
            }
        }

    get_quest_status(progress)
main()