import sys

class Character:
    """
    Represents a game character with core attributes.
    """
    def __init__(self, name="Unnamed", race="Human", char_class="Warrior"):
        self.name = name
        self.race = race
        self.char_class = char_class
        self.health = 100
        self.attack = 10
        self.defense = 10
        self.level = 1
        self.inventory = [] #

    def get_stats(self):
        """Returns a string summary of the character's stats."""
        return (f"Name: {self.name}\nRace: {self.race}\nClass: {self.char_class}\n"
                f"Level: {self.level}\nHealth: {self.health}\nAttack: {self.attack}\n"
                f"Defense: {self.defense}\nInventory: {', '.join(self.inventory) or 'Empty'}")

    def add_item(self, item):
        """Adds an item to the character's inventory."""
        self.inventory.append(item)
        print(f"{item} added to {self.name}'s inventory.")

def create_new_character():
    """Guides the user through creating a new character."""
    print("--- Character Creation ---")
    name = input("Enter your character's name: ")
    while not name:
        name = input("Name cannot be empty. Enter your character's name: ")

    races = ["Human", "Elf", "Dwarf", "Halfling", "Gnome", "Kobold"]
    print(f"Available races: {', '.join(races)}")
    race = input(f"Choose a race ({'/'.join(races)}): ").capitalize()
    while race not in races:
        race = input("Invalid race. Choose again: ").capitalize()

    classes = ["Warrior", "Mage", "Rogue", "Cleric", "Monk", "Druid"]
    print(f"Available classes: {', '.join(classes)}")
    char_class = input(f"Choose a class ({'/'.join(classes)}): ").capitalize()
    while char_class not in classes:
        char_class = input("Invalid class. Choose again: ").capitalize()

    # Create character object
    new_char = Character(name, race, char_class)
    
    # Add a default item based on class
    if char_class == "Warrior":
        new_char.add_item("Sword")
        new_char.attack += 5
    elif char_class == "Mage":
        new_char.add_item("Staff")
        new_char.health -= 10 # Example of class-based stat modification
    
    print("\nCharacter created successfully!")
    print(new_char.get_stats())
    return new_char

if __name__ == "__main__":
    try:
        player_character = create_new_character()
    except EOFError:
        print("\nExiting character creator due to input error.")
        sys.exit(0)
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        sys.exit(1)

