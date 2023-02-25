are_you_playing_banjo = lambda name: f"{name} plays banjo" if name[0] == "R" or name[0] == "r" else f"{name} does not play banjo"
print(are_you_playing_banjo("rafael"))