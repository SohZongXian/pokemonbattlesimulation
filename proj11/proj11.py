"""
    SOURCE HEADER GOES HERE!
"""
import csv
from random import randint
from random import seed
from copy import deepcopy

from pokemon import Pokemon
from pokemon import Move

seed(1) #Set the seed so that the same events always happen


#DO NOT CHANGE THIS!!!
# =============================================================================
element_id_list = [None, "normal", "fighting", "flying", "poison", "ground", "rock", 
                   "bug", "ghost", "steel", "fire", "water", "grass", "electric", 
                   "psychic", "ice", "dragon", "dark", "fairy"]

#Element list to work specifically with the moves.csv file.
#   The element column from the moves.csv files gives the elements as integers.
#   This list returns the actual element when given an index
# =============================================================================
    
def read_file_moves(fp):  
    '''
        WRITE DOCSTRING HERE!!!
    '''
    csv_reader = csv.reader(fp)
    next(csv_reader)
    moves_list = []
    for move in csv_reader:
        name = move[1]
        attack_type = int(move[9])
        power = int(move[4]) if move[4] != '' else None
        accuracy = int(move[6]) if move[6] != '' else None
        generation_id = int(move[2])
        if generation_id == 1 and attack_type != 1 and power != None and accuracy != None:
            element = element_id_list[int(move[3])]
            move_obj = Move(name, element, power, accuracy, attack_type)
            moves_list.append(move_obj)
    return moves_list


def read_file_pokemon(fp):
    '''
        WRITE DOCSTRING HERE!!!
    '''
    csv_reader = csv.reader(fp)
    next(csv_reader)
    pokemon_list = []
    ids_read = []
    for pokemon in csv_reader:
        if int(pokemon[0]) not in ids_read:
            ids_read.append(int(pokemon[0]))
            name = pokemon[1].lower()
            element1 = pokemon[2].lower()
            element2 = pokemon[3].lower()
            hp = int(pokemon[5])
            patt = int(pokemon[6])
            pdef = int(pokemon[7])
            satt = int(pokemon[8])
            sdef = int(pokemon[9])

            if int(pokemon[11]) == 1:
                pokemon_obj = Pokemon(name, element1, element2, None, hp, patt, pdef, satt, sdef)
                pokemon_list.append(pokemon_obj)
    return pokemon_list

def choose_pokemon(choice,pokemon_list):
    '''
        WRITE DOCSTRING HERE!!!
    '''
    try:
        choice=int(choice)
    except:
        pass
    if type(choice) == int:
        index = int(choice)-1
        try:
            pokemon_obj = deepcopy(pokemon_list[index])
            pokemon_list.remove(pokemon_list[index])
            return pokemon_obj
        except IndexError:
            return None
    else:
        name = choice.lower()
        pokemon_obj = None
        for pokemon in pokemon_list:
            if pokemon.get_name().lower() == name:
                pokemon_obj = deepcopy(pokemon)
        pokemon_list.remove(pokemon_obj)
        return pokemon_obj

def add_moves(pokemon,moves_list):
    '''
        WRITE DOCSTRING HERE!!!
    '''
    max_range = len(moves_list) - 1
    first_random_index = randint(0, max_range)

    pokemon.add_move(deepcopy(moves_list[first_random_index]))
    moves_list_added = []
    moves_list_added.append(deepcopy(moves_list[first_random_index]))

    count = 0
    while count <= 200 and len(moves_list_added) < 4:
        random_index = randint(0, max_range)
        move = deepcopy(moves_list[random_index])
        if (move.element == pokemon.element1 or move.element == pokemon.element2) and move not in moves_list_added:
            moves_list_added.append(move)
            pokemon.add_move(deepcopy(move))
        count += 1
    if len(moves_list_added) != 4:
        return False
    else:
        return True

def turn (player_num, player_pokemon, opponent_pokemon):
    '''
        WRITE DOCSTRING HERE!!!
    '''
    print("Player {}'s turn".format(str(player_num)))
    print(player_pokemon)
    other = 1 if player_num == 2 else 2
    user_input = input("Show options: 'show ele', 'show pow', 'show acc'\nSelect an attack between 1 and {} or show option or 'q': ".format(player_pokemon.get_number_moves()))
    while user_input.isnumeric() == False:
        if user_input.lower() == 'show ele':
            player_pokemon.show_move_elements()
            user_input = input(
                "Show options: 'show ele', 'show pow', 'show acc'\nSelect an attack between 1 and {} or show option or 'q': ".format(
                    player_pokemon.get_number_moves()))

        elif user_input.lower() == 'show pow':
            player_pokemon.show_move_power()
            user_input = input(
                "Show options: 'show ele', 'show pow', 'show acc'\nSelect an attack between 1 and {} or show option or 'q': ".format(
                    player_pokemon.get_number_moves()))

        elif user_input.lower() == 'show acc':
            player_pokemon.show_move_accuracy()
            user_input = input(
                "Show options: 'show ele', 'show pow', 'show acc'\nSelect an attack between 1 and {} or show option or 'q': ".format(
                    player_pokemon.get_number_moves()))

        elif user_input.lower() == 'q':

            print("Player {} quits, Player {} has won the pokemon battle!".format(str(player_num), str(other)))
            return False
    selected_move = player_pokemon.get_moves()[int(user_input) - 1]
    print("selected move:",selected_move)
    print("\n{} hp before:{}".format(opponent_pokemon.get_name(), opponent_pokemon.get_hp()))
    player_pokemon.attack(selected_move, opponent_pokemon)
    print("{} hp after:{}\n".format(opponent_pokemon.get_name(), opponent_pokemon.get_hp()))

    if opponent_pokemon.get_hp() <= 0:
        print("Player {}'s pokemon fainted, Player {} has won the pokemon battle!".format(str(other), str(player_num)))
        return False
    else:
        return True

def main():
        
    usr_inp = input("Would you like to have a pokemon battle?").lower()
    while usr_inp != 'n' and usr_inp != 'q' and usr_inp != 'y':
        usr_inp = input("Invalid option! Please enter a valid choice: Y/y, N/n or Q/q:").lower()



    while usr_inp.lower()=='y':
        pokemon_file = open('pokemon.csv')
        moves_file = open('moves.csv')
        moves_list = read_file_moves(moves_file)
        pokemons_list = read_file_pokemon(pokemon_file)
        choice_1 = input("Player {}, choose a pokemon by name or index: ".format("1"))
        player_1_pokemon = choose_pokemon(choice_1,pokemons_list)
        while isinstance(player_1_pokemon,Pokemon)==False and player_1_pokemon==None:
            choice_1 = input("Invalid option, choose a pokemon by name or index: ")
            player_1_pokemon = choose_pokemon(choice_1, pokemons_list)
        print("pokemon{}:\n".format("1"))
        print(player_1_pokemon)
        moves_1 = add_moves(player_1_pokemon,moves_list)
        while moves_1==False:
            print("Insufficient moves; choose a different pokemon.")
            choice_1 = input("Player {}, choose a pokemon by name or index: ".format("1"))
            player_1_pokemon = choose_pokemon(choice_1, pokemons_list)
            while  isinstance(player_1_pokemon,Pokemon)==False and player_1_pokemon==None:
                choice_1 = input("Invalid option, choose a pokemon by name or index: ")
                player_1_pokemon = choose_pokemon(choice_1, pokemons_list)
            moves_1 = add_moves(player_1_pokemon, moves_list)


        choice_2 = input("Player {}, choose a pokemon by name or index: ".format("2"))
        player_2_pokemon = choose_pokemon(choice_2, pokemons_list)
        while  isinstance(player_2_pokemon,Pokemon)==False and player_2_pokemon==None:
            choice_2 = input("Invalid option, choose a pokemon by name or index: ")
            player_2_pokemon = choose_pokemon(choice_2, pokemons_list)
        print("pokemon{}:\n".format("2"))
        print(player_2_pokemon)
        moves_2 = add_moves(player_2_pokemon, moves_list)
        while moves_2 == False:
            print("Insufficient moves; choose a different pokemon.")
            choice_2 = input("Player {}, choose a pokemon by name or index: ".format("2"))
            player_2_pokemon = choose_pokemon(choice_2, pokemons_list)
            while  isinstance(player_2_pokemon,Pokemon)==False and player_2_pokemon==None:
                choice_2 = input("Invalid option, choose a pokemon by name or index: ")
                player_2_pokemon = choose_pokemon(choice_2, pokemons_list)
            moves_2 = add_moves(player_2_pokemon, moves_list)

        turn_out = True
        while turn_out:
            turn_out = turn(1,player_1_pokemon,player_2_pokemon)
            if turn_out==False:
                break
            turn_out = turn(2,player_2_pokemon,player_1_pokemon)
            print("Player 1 hp after: ",player_1_pokemon.get_hp())
            print("Player 2 hp after: ",player_2_pokemon.get_hp())
            print()
        usr_inp = input("Battle over, would you like to have another? ")
        while usr_inp.lower() not in "ynq":
            usr_inp = input("Invalid option! Please enter a valid choice: ")


    if usr_inp != 'y':
        print("Well that's a shame, goodbye")
        return
    
    else:
        pass
    
if __name__ == "__main__":
    main()
