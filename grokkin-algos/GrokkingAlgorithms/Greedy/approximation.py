radio_stations = {
    "kone": {"id", "nv", "ut"},
    "ktwo": {"wa", "id", "mt"},
    "kthree": {"or", "nv", "ca"},
    "kfour": {"nv", "ut"},
    "kfive": {"ca", "az"}
}

final_stations = set()

states_to_cover = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}

while states_to_cover:
    best_station = None
    states_covered = set()
    for radio_station, states in radio_stations.items():
        covered = states_to_cover & states
        if len(covered) > len(states_covered):
            best_station = radio_station
            states_covered = covered
    final_stations.add(best_station)
    states_to_cover -= states_covered

print(final_stations)
