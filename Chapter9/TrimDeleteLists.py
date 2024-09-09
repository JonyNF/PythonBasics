def trim_strongholds(strongholds):
    del strongholds[0]
    del strongholds[-2:]
    return strongholds

def main():
    strongholds = [
            "Rivendale",
            "The Morgoth Mountains",
            "The Lonely Island",
            "Mordia",
            "Mordane",
            "Gondolin",
        ]
    print(trim_strongholds(strongholds))
main()