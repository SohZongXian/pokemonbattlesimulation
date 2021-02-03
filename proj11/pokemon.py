"""
    SOURCE HEADER GOES HERE!
"""

from random import randint


#DO NOT CHANGE THIS!!!
# =============================================================================
is_effective_dictionary = {'bug': {'dark', 'grass', 'psychic'}, 
                           'dark': {'ghost', 'psychic'},
                           'dragon': {'dragon'}, 
                           'electric': {'water', 'flying'}, 
                           'fairy': {'dark', 'dragon', 'fighting'},
                           'fighting': {'dark', 'ice', 'normal', 'rock', 'steel'}, 
                           'fire': {'bug', 'grass', 'ice', 'steel'}, 
                           'flying': {'bug', 'fighting', 'grass'}, 
                           'ghost': {'ghost', 'psychic'}, 
                           'grass': {'water', 'ground', 'rock'}, 
                           'ground': {'electric', 'fire', 'poison', 'rock', 'steel'}, 
                           'ice': {'dragon', 'flying', 'grass', 'ground'}, 
                           'normal': set(), 
                           'poison': {'fairy', 'grass'}, 
                           'psychic': {'fighting', 'poison'}, 
                           'rock': {'bug', 'fire', 'flying', 'ice'},
                           'steel': {'fairy', 'ice', 'rock'},
                           'water': {'fire', 'ground', 'rock'}
                           }

not_effective_dictionary = {'bug': {'fairy', 'flying', 'fighting', 'fire', 'ghost','poison','steel'}, 
                            'dragon': {'steel'}, 
                            'dark': {'dark', 'fairy', 'fighting'},
                            'electric': {'dragon', 'electric', 'grass'},
                            'fairy': {'fire', 'poison', 'steel'},
                            'fighting': {'bug', 'fairy', 'flying', 'poison', 'psychic'}, 
                            'fire': {'dragon', 'fire', 'rock', 'water'}, 
                            'flying': {'electric', 'rock', 'steel'}, 
                            'ghost': {'dark'}, 
                            'grass': {'bug', 'dragon', 'grass', 'fire', 'flying', 'poison', 'steel'}, 
                            'ground': {'bug','grass'}, 
                            'ice': {'fire', 'ice', 'steel', 'water'}, 
                            'normal': {'rock', 'steel'}, 
                            'poison': {'ghost', 'ground', 'poison', 'rock'}, 
                            'psychic': {'psychic', 'steel'}, 
                            'rock': {'fighting', 'ground', 'steel'}, 
                            'steel': {'electric', 'fire', 'steel', 'water'},
                            'water': {'dragon','grass', 'ice'}
                            }

no_effect_dictionary = {'electric': {'ground'}, 
                        'dragon': {'fairy'},
                        'fighting': {'ghost'}, 
                        'ghost': {'normal', 'psychic'}, 
                        'ground': {'flying'}, 
                        'normal': {'ghost'}, 
                        'poison': {'steel'},
                        'psychic': {'dark'}, 
                        
                        'bug': set(), 'dark': set(), 'fairy': set(),'fire': set(), 
                        'flying': set(), 'grass': set(), 'ice': set(), 
                        'rock': set(), 'steel': set(), 'water': set()
                        }

# Dictionaries that determine element advantages and disadvantages
# =============================================================================

class Move(object):
    def __init__(self, name = "", element = "normal", power = 20, accuracy = 80,
                 attack_type = 2):
        """ Initialize attributes of the Move object """
        
        self.name = name
        self.element = element
        self.power = power
        
        self.accuracy = accuracy
        self.attack_type = attack_type  #attack_type is 1, 2 or 3 
        # 1 - status moves, 2 - physical attacks, 3 - special attacks
        
    def __str__(self):
            
        '''
            Returns just the name of the move (used for printing).
        '''        
        return self.name

    def __repr__(self):
        '''
            Returns just the name of the move
        '''
        return self.__str__()
    
    def get_name(self):
        '''
            Returns the name attribute
        '''
        return self.name
    
    def get_element(self):
        '''
            Returns the element attribute.
        '''
        return self.element
    
    def get_power(self):
        '''
            Returns the power attribute.
        '''
        return self.power
    
    def get_accuracy(self):
        '''
            Returns the accuracy attribute.
        '''
        return self.accuracy
    
    def get_attack_type(self):
        '''
            Returns the attack_type attribute.
        '''
        return self.attack_type

    def __eq__(self,m):
        '''return True if all attributes are equal; False otherwise'''
        return self.name == m.get_name() and self.element == m.get_element() and\
                self.power == m.get_power() and self.accuracy == m.get_accuracy() and\
                self.attack_type == m.get_attack_type()
        
        
class Pokemon(object):
    def __init__(self, name = "", element1 = "normal", element2 = "", moves = None,
                 hp = 100, patt = 10, pdef = 10, satt = 10, sdef = 10):
        ''' initializes attributes of the Pokemon object '''
        
        self.name = name
        self.element1 = element1
        self.element2 = element2
        
        self.hp = hp
        self.patt = patt
        self.pdef = pdef
        self.satt = satt
        self.sdef = sdef
        
        self.moves = moves
        
        try:
            if len(moves) > 4:
                self.moves = moves[:4]
                
        except TypeError: #For Nonetype
            self.moves = list()

    def __eq__(self,p):
        '''return True if all attributes are equal; False otherwise'''
        return self.name == p.name and \
            self.element1 == p.element1 and \
            self.element2 == p.element2 and \
            self.hp == p.hp and \
            self.patt == p.patt and \
            self.pdef == p.pdef and \
            self.satt == p.satt and \
            self.sdef == p.sdef and \
            self.moves == p.moves

    def __str__(self):
        '''
            Returns a string containing the parts of the pokemon object divided into three lines.
            The first line will display in this order: name, hp, patt, pdef, satt and sdef,
            followed by a newline character directly after sdef with no space inbetween sdef
            and the newline character. The second line will display the element1 and element2
            with a newline character after element2. The third line will display all the moves
            of that pokemon.
        '''
        string = "{:<15}{:<15}{:<15}{:<15}{:<15}{:<15}\n{:<15}{:<15}\n".format(self.name,str(self.hp),str(self.patt),str(self.pdef),str(self.satt),str(self.sdef),self.element1,self.element2)
        for each in self.moves:
            string+="{:<15}".format(str(each))
        return string

    def __repr__(self):
        '''
            Returns the same value as the __str__() method to.
        '''
        return self.__str__()


    def get_name(self):
        '''
            Returns the name attribute
        '''
        return self.name
    
    def get_element1(self):
        '''
           Returns the element1 attribute.
        '''
        return self.element1
    
    def get_element2(self):
        '''
            Returns the element2 attribute.
        '''
        if self.element2=='':
            return None
        else:
            return self.element2
    
    def get_hp(self):
        '''
            Returns the hp attribute.
        '''
        return self.hp
    
    def get_patt(self):
        '''
           Returns the patt attribute.
        '''
        return self.patt

    def get_pdef(self):
        '''
            Returns the pdef attribute.
        '''
        return self.pdef

    def get_satt(self):
        '''
            Returns the satt attribute.
        '''
        return self.satt

    def get_sdef(self):
        '''
            Returns the sdef attribute.
        '''
        return self.sdef
    
    def get_moves(self):
        '''
            Returns the moves attribute.
        '''
        return self.moves

    def get_number_moves(self):
        '''
            Returns the number of moves.
        '''
        return len(self.moves)

    def choose(self,index):
        '''
            Takes an index and returns the corresponding move from the moves list. If there is an IndexError returns None.
        '''
        try:
            return self.moves[index]
        except IndexError:
            return None

        
    def show_move_elements(self):
        '''
            Displays the elements of the pokemon’s moves (each in a 15-space field, left justified). This function does not return anything.
        '''
        string = ""
        for each in self.moves:
            string+="{:<15}".format(str(each.get_element()))
        print(string)

    def show_move_power(self):
        '''
            Displays the power of the pokemon’s moves (each in a 15-space field, left justified). This function does not return anything.
        '''
        string = ""
        for each in self.moves:
            string += "{:<15}".format(str(each.get_power()))
        print(string)

    def show_move_accuracy(self):
        '''
            Displays the accuracy of the pokemon’s moves (each in a 15-space field, left justified). This function does not return anything.
        '''
        string = ""
        for each in self.moves:
            string += "{:<15}".format(str(each.get_accuracy()))
        print(string)
        
        
    def add_move(self, move):
        '''
            Adds the move parameter to the list of moves for this pokemon if this pokemon has three or less moves. This function does not return anything.
        '''
        if len(self.moves)<=3:
            self.moves.append(move)

            
        
    def attack(self, move, opponent):
        '''
            This method takes the move used by the attacker (self) and deals damage to the opponent (who should also be an instance of class Pokemon). It does not return anything.
        '''
        if isinstance(move,Move) and isinstance(opponent,Pokemon):
            mp=move.get_power()
            A=None
            D=None
            modifier=1.0
            damage = 0


            power = move.get_power()
            attack_type = move.get_attack_type()

            if attack_type==2:
                A=self.patt
                D=opponent.get_pdef()
            elif attack_type==3:
                A=self.satt
                D=opponent.get_sdef()
            else:
                print("Invalid attack_type, turn skipped.")
                return
            accuracy_random = randint(1,100)
            accuracy_move = move.get_accuracy()
            if accuracy_random>accuracy_move:
                print("Move missed!")
                return
            element1_opp = opponent.get_element1()
            element2_opp = opponent.get_element2()
            element_move = move.get_element()
            if element1_opp in is_effective_dictionary[element_move]:
                modifier=modifier*2
            elif element1_opp in not_effective_dictionary[element_move]:
                modifier=modifier/2
            elif element1_opp in no_effect_dictionary[element_move]:
                modifier=0
            if element2_opp:
                if element2_opp in is_effective_dictionary[element_move]:
                    modifier = modifier * 2
                elif element2_opp in not_effective_dictionary[element_move]:
                    modifier = modifier / 2
                elif element2_opp in no_effect_dictionary[element_move]:
                    modifier=0

            if modifier>1:
                print("It's super effective!!!!")
            elif modifier<1:
                print("Not very effective...")
            elif modifier==0:
                print("No effect!")
            if element_move==self.element1 or element_move==self.element2:
                modifier=modifier*1.5

            damage = int((((mp*(A/D)*20)/50)+2)*modifier)

            opponent.subtract_hp(damage)


    def subtract_hp(self,damage):
        '''
           This method takes the damage variable and subtracts it from the hp of the Pokemon object
        '''
        hp = 0 if (self.hp-damage)<0 else self.hp-damage
        self.hp=hp

    

        