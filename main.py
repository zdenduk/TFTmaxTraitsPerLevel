import itertools

# Define the champions (their traits + cost/tier)
champions = {
    "Aatrox": {"traits": ["Darkin", "Slayer", "Juggernaut"], "cost": 5},
    "Ahri": {"traits": ["Ionia", "Sorcerer"], "cost": 5},
    "Aphelios": {"traits": ["Targon", "Gunner"], "cost": 4},
    "Ashe": {"traits": ["Freljord", "Vanquisher"], "cost": 2},
    "Azir": {"traits": ["Shurima", "Strategist"], "cost": 4},
    "Bel'Veth": {"traits": ["Void", "Empress"], "cost": 5},
    "Cassiopeia": {"traits": ["Noxus", "Shurima", "Invoker"], "cost": 1},
    "Cho'Gath": {"traits": ["Void", "Bruiser"], "cost": 1},
    "Darius": {"traits": ["Noxus", "Juggernaut", "Vanquisher"], "cost": 3},
    "Ekko": {"traits": ["Zaun", "Piltover", "Rogue"], "cost": 3},
    "Fiora": {"traits": ["Demacia", "Challenger"], "cost": 4},
    "Galio": {"traits": ["Demacia", "Invoker"], "cost": 2},
    "Gangplank": {"traits": ["Bilgewater", "Gunner", "Reaver King"], "cost": 5},
    "Graves": {"traits": ["Bilgewater", "Gunner", "Rogue"], "cost": 1},
    "Heimerdinger": {"traits": ["Piltover", "Technogenius"], "cost": 5},
    "Illaoi": {"traits": ["Bilgewater", "Bastion"], "cost": 1},
    "Irelia": {"traits": ["Ionia", "Challenger"], "cost": 1},
    "Jarvan IV": {"traits": ["Demacia", "Strategist"], "cost": 4},
    "Jayce": {"traits": ["Piltover", "Gunner"], "cost": 3},
    "Jhin": {"traits": ["Ionia", "Vanquisher"], "cost": 1},
    "Jinx": {"traits": ["Zaun", "Gunner"], "cost": 2},
    "Kai'Sa": {"traits": ["Void", "Challenger"], "cost": 4},
    "Karma": {"traits": ["Ionia", "Invoker"], "cost": 3},
    "Kassadin": {"traits": ["Void", "Bastion"], "cost": 2},
    "Katarina": {"traits": ["Noxus", "Rogue"], "cost": 3},
    "Kayle": {"traits": ["Demacia", "Slayer"], "cost": 1},
    "K'Sante": {"traits": ["Shurima", "Bastion"], "cost": 5},
    "Malzahar": {"traits": ["Void", "Sorcerer"], "cost": 1},
    "Milio": {"traits": ["Ixtal", "Invoker"], "cost": 1},
    "Miss Fortune": {"traits": ["Bilgewater", "Strategist"], "cost": 3},
    "Mordekaiser": {"traits": ["Noxus", "Slayer"], "cost": 4},
    "Naafiri": {"traits": ["Darkin", "Shurima", "Challenger"], "cost": 2},
    "Nautilus": {"traits": ["Bilgewater", "Juggernaut"], "cost": 3},
    "Neeko": {"traits": ["Ixtal", "Bastion"], "cost": 3},
    "Nilah": {"traits": ["Bilgewater", "Vanquisher"], "cost": 4},
    "Orianna": {"traits": ["Piltover", "Sorcerer"], "cost": 1},
    "Poppy": {"traits": ["Demacia", "Bastion"], "cost": 1},
    "Qiyana": {"traits": ["Ixtal", "Slayer", "Rogue"], "cost": 2},
    "Quinn": {"traits": ["Demacia", "Slayer"], "cost": 3},
    "Rek'Sai": {"traits": ["Void", "Bruiser", "Slayer"], "cost": 3},
    "Renekton": {"traits": ["Shurima"], "cost": 1},
    "Ryze": {"traits": ["Wanderer", "Invoker"], "cost": 5},
    "Samira": {"traits": ["Noxus", "Challenger"], "cost": 1},
    "Sejuani": {"traits": ["Freljord", "Bruiser"], "cost": 4},
    "Sett": {"traits": ["Ionia", "Juggernaut"], "cost": 2},
    "Shen": {"traits": ["Ionia", "Bastion", "Invoker"], "cost": 4},
    "Silco": {"traits": ["Zaun", "Sorcerer"], "cost": 4},
    "Sion": {"traits": ["Noxus", "Bruiser"], "cost": 5},
    "Sona": {"traits": ["Demacia", "Multicaster"], "cost": 3},
    "Soraka": {"traits": ["Targon", "Invoker"], "cost": 2},
    "Swain": {"traits": ["Noxus", "Strategist", "Sorcerer"], "cost": 2},
    "Taliyah": {"traits": ["Shurima", "Multicaster"], "cost": 2},
    "Taric": {"traits": ["Targon", "Bastion", "Sorcerer"], "cost": 3},
    "Twisted Fate": {"traits": ["Bilgewater", "Multicaster"], "cost": 2},
    "Vel'Koz": {"traits": ["Void", "Multicaster", "Sorcerer"], "cost": 3},
    "Vi": {"traits": ["Piltover", "Bruiser"], "cost": 2},
    "Warwick": {"traits": ["Zaun", "Juggernaut", "Challenger"], "cost": 2},
    "Xayah": {"traits": ["Ionia", "Vanquisher"], "cost": 4},
}

# Champion availability by player level
champion_availability = {
    1: {
        "Tier1": True,
        "Tier2": False,
        "Tier3": False,
        "Tier4": False,
        "Tier5": False
    },
    2: {
        "Tier1": True,
        "Tier2": False,
        "Tier3": False,
        "Tier4": False,
        "Tier5": False
    },
    3: {
        "Tier1": True,
        "Tier2": True,
        "Tier3": False,
        "Tier4": False,
        "Tier5": False
    },
    4: {
        "Tier1": True,
        "Tier2": True,
        "Tier3": True,
        "Tier4": False,
        "Tier5": False
    },
    5: {
        "Tier1": True,
        "Tier2": True,
        "Tier3": True,
        "Tier4": True,
        "Tier5": False
    },
    6: {
        "Tier1": True,
        "Tier2": True,
        "Tier3": True,
        "Tier4": True,
        "Tier5": False
    },
    7: {
        "Tier1": True,
        "Tier2": True,
        "Tier3": True,
        "Tier4": True,
        "Tier5": True
    },
    8: {
        "Tier1": True,
        "Tier2": True,
        "Tier3": True,
        "Tier4": True,
        "Tier5": True
    },
    9: {
        "Tier1": True,
        "Tier2": True,
        "Tier3": True,
        "Tier4": True,
        "Tier5": True
    },
    10: {
        "Tier1": True,
        "Tier2": True,
        "Tier3": True,
        "Tier4": True,
        "Tier5": True
    },
    11: {
        "Tier1": True,
        "Tier2": True,
        "Tier3": True,
        "Tier4": True,
        "Tier5": True
    }
}

trait_activation = {
    "Bilgewater": [3, 5, 7, 9],
    "Darkin": [1, 2],
    "Demacia": [3, 5, 7, 9],
    "Freljord": [2, 3],
    "Ionia": [3, 6, 9],
    "Ixtal": [2, 3, 4],
    "Noxus": [3, 5, 7, 9],
    "Piltover": [3, 6],
    "Shurima": [2, 4, 6, 9],
    "Targon": [2, 3, 4],
    "Void": [3, 6, 8],
    "Zaun": [2, 4, 6],
    "Bastion": [2, 4, 6, 8],
    "Bruiser": [2, 4, 6],
    "Challenger": [2, 4, 6, 8],
    "Empress": [1],
    "Gunner": [2, 4, 6],
    "Invoker": [2, 4, 6, 8],
    "Juggernaut": [2, 4, 6],
    "Multicaster": [2, 3, 4],
    "Reaver King": [1],
    "Wanderer": [1],
    "Rogue": [2, 4],
    "Slayer": [2, 4, 6],
    "Sorcerer": [2, 4, 6, 8],
    "Strategist": [2, 3, 4, 5],
    "Technogenius": [1],
    "Vanquisher": [2, 4, 6]
}


def most_traits_for_level_any_units(level):
    max_traits = 0
    best_combination = []

    # Iterate over all combinations of champions for the given level
    for combo in itertools.combinations(champions.keys(), level):
        # Collect all traits for the current combination
        traits = set()
        for champ in combo:
            traits.update(champions[champ])

        # Update the best combination if the current one has more traits
        if len(traits) > max_traits:
            max_traits = len(traits)
            best_combination = combo

    return best_combination, max_traits


def active_traits_for_combination(combination):
    trait_counts = {}
    for champ in combination:
        for trait in champions[champ]["traits"]:
            if trait not in trait_counts:
                trait_counts[trait] = 0
            trait_counts[trait] += 1

    active_traits = 0
    for trait, count in trait_counts.items():
        for activation in trait_activation[trait]:
            if count >= activation:
                active_traits += 1
                break

    return active_traits


def max_active_traits(level):
    available_champs = [champ for champ, details in champions.items() if
                        champion_availability[level]["Tier" + str(details["cost"])]]
    max_traits = 0
    best_combination = []

    for combination in itertools.combinations(available_champs, level):
        traits = active_traits_for_combination(combination)
        if traits >= max_traits:
            max_traits = traits
            best_combination.append(combination)

    return best_combination, max_traits


def get_active_traits(board, champions):
    trait_counts = {}
    for champ in board:
        for trait in champions[champ]['traits']:
            trait_counts[trait] = trait_counts.get(trait, 0) + 1

    active_traits = 0
    for trait, count in trait_counts.items():
        for activation in sorted(trait_activation[trait]):
            if count >= activation:
                active_traits += 1
                break

    return active_traits


def backtrack(level, board, champions, best_boards, best_count):
    if len(board) == level:
        active_count = get_active_traits(board, champions)
        if active_count == best_count[0]:
            best_boards.append(board.copy())
        elif active_count > best_count[0]:
            best_count[0] = active_count
            best_boards.clear()
            best_boards.append(board.copy())
        return

    for champ in list(champions.keys()):
        if champ not in board:
            board.append(champ)
            if get_active_traits(board, champions) + (level - len(board)) >= best_count[0]:
                backtrack(level, board, champions, best_boards, best_count)
            board.pop()


def optimize_board(level, champions):
    best_boards = []  # List of optimal boards
    best_count = [0]  # Maximum active trait count
    backtrack(level, [], champions, best_boards, best_count)
    return best_boards, best_count[0]


if __name__ == "__main__":
    f = open("combinations.txt", "w")
    level_traitcount = {}
    for level in range(3, 9):
        combination, traits = max_active_traits(level)
        for board in combination:
            level_traitcount[level] = traits
            f.write(f"Level {level}: {traits} active traits with combination {board}\n")
    #for level in range(7, 10):
    #    optimized_board, optimized_traits_count = optimize_board(level, champions)
    #    for board in optimized_board:
    #        level_traitcount[level] = optimized_traits_count
    #        f.write(f"Level {level}: {optimized_traits_count} active traits with combination {board}\n")

    f.flush()
    f.close()
    #f = open("level_traitcount.txt", "w")
    #f.write(str(level_traitcount))
    #f.flush()
    #f.close()
