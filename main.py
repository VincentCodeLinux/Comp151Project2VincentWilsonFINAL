vgsales_filehandle = open("vgsales.csv", "r")
vgsales_file = vgsales_filehandle.readlines()
current_year = int(2025)
for line in vgsales_file[1:]:
    name = line.strip().split(',')
    game_name = name[1]
    rank_of_game = name[0]
    year_of_game = name[3]
    year = int(year_of_game)
    total_sales = float(name[10])
    how_long_has_it_been = current_year - year
    average_per_year = total_sales / how_long_has_it_been
    print(f"{rank_of_game} {game_name}  -  {average_per_year:.2f} was the average amount of copies sold per year")




