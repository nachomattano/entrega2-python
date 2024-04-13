def generate_stats(names, goals, goals_avoided, assists):
    stats = []
    names_list = names.split(", ")
    for i in range(len(names_list)):
        jugador = {
            "Nombre": names_list[i],
            "Goles a favor": goals[i],
            "Goles evitados": goals_avoided[i],
            "Asistencias": assists[i]
        }
        stats.append(jugador)
    return stats
