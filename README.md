# Monster-Haunted-House
#### Video Demo:  <https://youtu.be/naxNEvTUJF4>
#### Description:
Lumo Monster Haunted Houze is a text-based adventure game I built for my final project in the CS50P course. The game, written entirely in Python, puts you in the shoes of a daring adventurer exploring a creepy, haunted house. Your main goal? Survive! Along the way, you’ll need to navigate through rooms, fight monsters, manage your health, and collect useful items. The game takes full advantage of Python’s key concepts like loops, conditionals, and object-oriented programming.

When the game starts, you find yourself at the entrance of the house. You can move through different rooms by typing simple directions like "north," "south," "east," or "west." Each room has a different vibe, whether it’s a hallway, an armory where you can pick up items, or the dreaded Monster Room, where danger awaits. The transitions between rooms are built using Python’s dictionary structure, allowing for easy navigation.

One of the main challenges in the game is the combat system, which revolves around a monster named Makumba. When you enter the Monster Room, you’ll have to decide whether to attack or run away. Attacking deals random damage between 5 and 15 points, but if you don’t finish off the monster, Makumba will strike back! The monster’s retaliation makes every battle intense. If you lose all your health, it’s game over. But, there’s hope—throughout the game, you can pick up items like health potions to heal yourself and keep going.

I’ve also added a feature that lets you save and load your progress. This way, you can save your game to a .txt file and pick it back up later. The file will store details like your health, location, and items, so you don’t have to start from scratch each time.

In terms of design, I debated whether to make the game more complex, such as adding more rooms or enemies, but I chose to keep it simple to maintain a focus on core Python concepts. The code structure is built around object-oriented programming, with separate classes for the player and the monster, allowing for cleaner, reusable code.

Lumo Monster Haunted Houze showcases Python basics like conditionals, loops, file handling, and error management, all wrapped into a fun, interactive adventure. I hope you enjoy it!
