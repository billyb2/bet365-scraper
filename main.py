from scrape import get_data

data = get_data("Table Tennis", True)
if data is not None:
    for players in data:
        if 1.05 <= float(data[players]) <= 1.1:
            print(players + ": " + data[players])

