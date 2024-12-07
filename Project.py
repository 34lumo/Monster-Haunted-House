import random

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.location = 'Entrance' #Se empieza siempre en la entrada

    def move(self, direction): # Funcion que define la transicion de habitaciones dependendiendo en que direccion se mueva
        room_map = { #Diccionario en el que aparece el sito en el que estas y al que te mueves dependiendo a donde elijas ir
            'Entrance': {'north': 'Hallway'},
            'Hallway': {'south': 'Entrance', 'east': 'Armory', 'west': 'Monster Room'},
            'Armory': {'west': 'Hallway'},
            'Monster Room': {'east': 'Hallway'}, #you fighting the monster
        }
        if direction in room_map[self.location]: #si la direccion se encuentra en el mapa de direcciones, te mueves.
            self.location = room_map[self.location][direction] #Se actualiza la direccion en la que te mueves
            print(f"You moved to {self.location}.")
        else:
            print("You can't go that way!")

    def attack(self, monster):
        damage = random.randint(5, 15) #al atacar al mounstro, le podemos hacer entre 5 y 15 de daño
        monster.take_damage(damage)
        print(f"You dealt {damage} damage to the {monster.name}.")

    def pick_up_item(self, item):
        self.inventory.append(item) #guarda en el array de inventario un item
        print(f"You picked up {item}.") #Explica por pantaña que item es

    def heal(self, amount):
        self.health += amount
        print(f"You healed {amount} health.")

class Monster:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, amount):
        self.health -= amount #se le resta a su vida la cantidad de daño que le hayan hecho al atacarle
        if self.health <= 0:
            self.alive = False
            print(f"The {self.name} has been defeated!")
        else: #mientras que no le hayan matado, informa de la vida que le queda.
            print(f"The {self.name} has {self.health} health left.")

def fight_monster(player, monster):
    while monster.health > 0 and player.health > 0:
        action = input("Do you want to attack (a) or flee (f)? ").lower()
        if action == 'a': #si el usuario quiere atacar, le hará daño entre 5-15
            player.attack(monster)
            if monster.health > 0: #pero si no consigue matar al mounstro, este contrataca, pudiendo hacer daño entre 5-10
                damage = random.randint(5, 10)
                player.health -= damage
                print(f"The {monster.name} dealt {damage} damage to you.")
                if player.health <= 0:
                    print("You died!")
                    break
        elif action == 'f': #si se caga, no se lleva a cabo la pelea
            print("You fled the battle!")
            break
        else:
            print("Invalid action.")

def save_game(player):
    try:
        with open('savegame.txt', 'w') as f: #guardamos en un txt la info necesaria.
            f.write(f"Name: {player.name}\n")
            f.write(f"Health: {player.health}\n")
            f.write(f"Location: {player.location}\n")
            f.write(f"Inventory: {', '.join(player.inventory)}\n")#Esto lo hacemos para poder guardar con comas el inventario
        print("Game saved.")
    except Exception as e: #mostramos un mensaje de error en caso de que lo haya
        print(f"Error saving the game: {e}")

def load_game():
    try:
        with open('savegame.txt', 'r') as f:
            lines = f.readlines()
            name = lines[0].strip().split(": ")[1]
            health = int(lines[1].strip().split(": ")[1])
            location = lines[2].strip().split(": ")[1]
            inventory = lines[3].strip().split(": ")[1].split(', ') if lines[3].strip().split(": ")[1] else []
          #guardamos la información
            player = Player(name)
            player.health = health
            player.location = location
            player.inventory = inventory
            print("Game loaded.")
            return player
    except Exception as e:
        print(f"Error loading the game: {e}")
        return None

def main():
    print("Welcome to Lumo's monster Haunted House!")
    player_name = input("Enter your name: ")
    player = Player(player_name)

    while True:
        monsterAlive = True
        print(f"\nYou are in {player.location}.")
        action = input("Choose an action: (m)ove, (i)nventory, (s)ave, (q)uit: ").lower()

        if action == 'm':
            direction = input("Move (north/south/east/west): ").lower()
            player.move(direction)

            if player.location == "Monster Room":
                monster = Monster('MAKUMBA', 30)
                fight_monster(player, monster)

        elif action == 'i':
            print(f"Inventory: {player.inventory}")
        elif action == 's':
            save_game(player)
        elif action == 'q':
            print("Goodbye!")
            break
        else:
            print("Invalid action.")

if __name__ == "__main__":
    main()
