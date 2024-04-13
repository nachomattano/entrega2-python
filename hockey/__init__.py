def generate_stats(names, goals, goals_avoided, assists):
    stats = []
    names_list = names.split(", ")
    for i in range(len(names_list)):
        player = {
            "Nombre": names_list[i],
            "Goles a favor": goals[i],
            "Goles evitados": goals_avoided[i],
            "Asistencias": assists[i]
        }
        stats.append(player)
    return stats

def max_scorer(stats):
    max_goals = max(stats, key=lambda x: x["Goles a favor"])
    return max_goals["Nombre"], max_goals["Goles a favor"]

def most_influential(stats):
    max_influential = max(stats, key=lambda x: x["Goles a favor"] * 1.5 + x["Goles evitados"] * 1.25 + x["Asistencias"])
    return max_influential["Nombre"]

def average_goals(goals):
    total = sum(goals)
    return total / 25
