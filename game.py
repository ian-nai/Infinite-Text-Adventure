import random


# setting up some global variables...
dict_of_rooms = {}
room_number = 1
player_position = room_number
x_coord = 0
y_coord = 0

# dummy value for generating first room
previous_room = 'first_room'

# list of all rooms in the dungeon
list_of_all_rooms = []
dict_of_all_rooms = {1: (0,0)}
list_of_existing_coordinates = [(0,0)]

# player
player_dict = {'name': 'Jonathan Goldtooth', 'description': 'A hero.', 'attack': 7, 'speed': 5, 'health': 70, 'equipped': 'dagger'}

# inventory - holds coins/items used to calculate score
inventory = ['a rusty dagger']

# inventory of usable items
usable_inventory = []

# item drop possibilities
tier_1_drops = ['10 gold', '1 ruby', 'small shard of diamond']
tier_2_drops = ['20 gold', '2 rubies', 'a polished brass ring']
tier_3_drops = ['30 gold', '3 rubies', 'a silver necklace']
tier_4_drops = ['40 gold', '4 rubies', 'a gold bracelet']
tier_5_drops = ['50 gold', '5 rubies', 'a platinum amulet']
rare_drops = ['100 gold', '1 blessed sapphire', 'an enchanted tiara']

# score counting variables
gold_count = 0
ruby_count = 0
jewelry_count = 0
blessed_sapphire_count = 0
enchanted_tiara_count = 0

# tracking whether the player is ambushed or not to determine turn-taking in the combat phase
ambush = False

# list of enemy dictionaries
all_enemies_list = [{'name': 'Wretched Orc', 'description': 'A common orc, fierce and bloodthirsty.', 'attack': 5, 'speed': 4, 'health': 4},
{'name': 'Dark Wizard', 'description': 'A corrupt wizard, heart blackened by his pursuit of wicked sorcery.', 'attack': 6, 'speed': 4, 'health': 5},
{'name': 'Diseased Rat', 'description': 'A rabid rat, oozing pus and eager to attack.', 'attack': 2, 'speed': 7, 'health': 2},
{'name': 'Fetid Ghoul', 'description': 'A vile spirit who haunts the dingy halls of the dungeon.', 'attack': 4, 'speed': 5, 'health': 3}]

# items that can be used to affect the player's health
usable_items = ['healing potion', 'mystery herb']

# placeholder
item_description = ''

# generating a room in the dungeon - creates a room and then adds it to the dict_of_rooms
def room_gen(previous_room):
    global player_dict
    global usable_inventory
    global item_description

    player_position = room_number

    new_room = {'directions': [], 'items': [], 'enemies': [], 'description': [], 'number': room_number, 'entered_direction': ''}


    # set the direction to return to previous room if not in the starting room
    if previous_room != 'first_room':
        entered_direction = previous_room['entered_direction']
    else:
        entered_direction = 'none'
        pass

    # generate directions of doors
    directions_to_leave = []

    if entered_direction == 'east':
        back_direction = 'west'
        directions_to_leave.append(back_direction)
    if entered_direction == 'west':
        back_direction = 'east'
        directions_to_leave.append(back_direction)
    if entered_direction == 'north':
        back_direction = 'south'
        directions_to_leave.append(back_direction)
    if entered_direction == 'south':
        back_direction = 'north'
        directions_to_leave.append(back_direction)



    if 'north' not in directions_to_leave:
        for i in range(0,1):
            coin_flip = random.choice(['heads','tails'])
            if coin_flip == 'heads':
                directions_to_leave.append('north')
            else:
                pass
    if 'east' not in directions_to_leave:
        for i in range(0,1):
            coin_flip = random.choice(['heads','tails'])
            if coin_flip == 'heads':
                directions_to_leave.append('east')
            else:
                pass
    if 'south' not in directions_to_leave:
        for i in range(0,1):
            coin_flip = random.choice(['heads','tails'])
            if coin_flip == 'heads':
                directions_to_leave.append('south')
            else:
                pass
    if 'west' not in directions_to_leave:
        for i in range(0,1):
            coin_flip = random.choice(['heads','tails'])
            if coin_flip == 'heads':
                directions_to_leave.append('west')
            else:
                pass

    list_of_directions = ['north', 'south', 'east', 'west']

    # make sure there's always a way forward, given the first room not having an entered_direction
    if not directions_to_leave:
        random_direction = (random.choice(list_of_directions))
        directions_to_leave.append(random_direction)

    if len(directions_to_leave) == 1:
        pos_dirs = []
        for dir in list_of_directions:
            if dir not in directions_to_leave:
                pos_dirs.append(dir)
        random_dir = (random.choice(pos_dirs))
        directions_to_leave.append(random_dir)

    new_room['directions'] = directions_to_leave

    #generate item drops
    item_in_room = []
    item_list = ['healing potion', 'mystery herb']

    if room_number <= 5:
        item_chance = 0.45
    elif 5 < room_number <= 10:
        item_chance = 0.25
    elif 10 < room_number <= 20:
        item_chance = 0.18
    else:
        item_chance = 0.12

    if random.random() < item_chance:
        item_in_room.append(random.choice(item_list))

    new_room['items'] += item_in_room

    # generate enemies
    global all_enemies_list
    enemies_in_room = []
    enemy_list = []
    for e in all_enemies_list:
        enemy_list.append(e['name'])

    #generate descriptive text
    list_of_room_moods = ['gloomy.', 'strangely uplifting.', 'eerily silent.', 'dingy and damp.']
    list_of_room_furniture = ['weathered wooden chair', 'empty shackles on the walls and floor', 'an old iron cot']
    list_of_room_decorations = ['a moth-easten tapestry.', 'a statue made of rusted bronze.', 'floorboards of rotted wood.', 'bare walls of mossy stone.']

    mood = random.choice(list_of_room_moods)
    furnishing = random.choice(list_of_room_furniture)
    decoration = random.choice(list_of_room_decorations)

    room_description = 'The room is ' + mood + ' You see a ' + furnishing + ' and ' + decoration

    if item_in_room:
        for item in item_in_room:
            item_description = 'You notice a ' + item.upper() + '.'

    new_room['description'] = room_description

    if room_number<= 5:
        enemy_chance = 0.45
    elif 5 < room_number <= 10:
        enemy_chance = 0.25
    elif 10 < room_number <= 20:
        enemy_chance = 0.18
    else:
        enemy_chance = 0.12

    if random.random() < enemy_chance:
        enemies_in_room.append(random.choice(enemy_list))

    new_room['enemies'] += enemies_in_room

    handle_directional_input(new_room, directions_to_leave)

# handle the user's input
def handle_directional_input(new_room, directions_to_leave):
    global inventory
    global usable_inventory
    global item_description
    global ambush
    global player_dict

    if len(new_room['enemies']) == 0:
        pass
    elif len(new_room['enemies']) == 1:
        print('--------------------------------------')
        print('There is a ' + new_room['enemies'][0] + ' in the room with you.')
    elif len(new_room['enemies']) >= 2:
        for x in new_room['enemies']:
            print('There is a ' + x +' in the room.')


    print(new_room['description'])
    if item_description:
        print(item_description)

    printable_directions_to_leave = [direction.capitalize() for direction in directions_to_leave]
    print('There are exits in the following directions: ' + ' | '.join(str(x) for x in printable_directions_to_leave))

    list_of_all_rooms.append(new_room)


    while True:
        try:
            action = input('What would you like to do? ')
            action = action.lower()
            if 'go' in action:
                action_without_go = action.replace('go ', '')
                if action_without_go in directions_to_leave:
                    ambush_num = random.randrange(101)
                    if ambush_num <= 70:
                        print('You go ' + action_without_go)
                        new_room['entered_direction'] = action_without_go
                        move_and_take_actions(new_room, action)
                    else:
                        if 'Wretched Orc' in new_room['enemies']:
                            print('You were ambushed!')
                            ambush = True
                            combat_phase('orc', room_number)
                        elif 'Dark Wizard' in new_room['enemies']:
                            print('You were ambushed!')
                            ambush = True
                            combat_phase('wizard', room_number)
                        elif 'Diseased Rat' in new_room['enemies']:
                            print('You were ambushed!')
                            ambush = True
                            combat_phase('rat', room_number)
                        elif 'Fetid Ghoul' in new_room['enemies']:
                            print('You were ambushed!')
                            ambush = True
                            combat_phase('ghoul', room_number)
                        else:
                            print('You go ' + action)
                            new_room['entered_direction'] = action
                            move_and_take_actions(new_room, action)
                else:
                    print('I can\'t go ' + action_without_go)
                    continue
            elif 'go' not in action:
                if action in directions_to_leave:
                    ambush_num = random.randrange(101)
                    if ambush_num <= 60:
                        print('You go ' + action)
                        new_room['entered_direction'] = action
                        move_and_take_actions(new_room, action)
                    else:
                        if 'Wretched Orc' in new_room['enemies']:
                            print('You were ambushed!')
                            ambush = True
                            combat_phase('orc', room_number)
                        elif 'Dark Wizard' in new_room['enemies']:
                            print('You were ambushed!')
                            ambush = True
                            combat_phase('wizard', room_number)
                        elif 'Diseased Rat' in new_room['enemies']:
                            print('You were ambushed!')
                            ambush = True
                            combat_phase('rat', room_number)
                        elif 'Fetid Ghoul' in new_room['enemies']:
                            print('You were ambushed!')
                            ambush = True
                            combat_phase('ghoul', room_number)
                        else:
                            print('You go ' + action)
                            new_room['entered_direction'] = action
                            move_and_take_actions(new_room, action)


                elif action not in directions_to_leave:
                    if 'attack' in action or 'fight' in action:
                        if 'orc' in action and 'Wretched Orc' in new_room['enemies']:
                            combat_phase('orc', room_number)
                        elif 'wizard' in action and 'Dark Wizard' in new_room['enemies']:
                            combat_phase('wizard', room_number)
                        elif 'rat' in action and 'Diseased Rat' in new_room['enemies']:
                            combat_phase('rat', room_number)
                        elif 'ghoul' in action and 'Fetid Ghoul' in new_room['enemies']:
                            combat_phase('ghoul', room_number)
                    elif action == 'i' or action == 'inventory':
                        if usable_inventory:
                            for item in usable_inventory:
                                print(item)
                        else:
                            print('Your inventory is empty.')
                    elif action == 'look':
                        print(new_room['description'])
                        if new_room['items']:
                            print(item_description)
                    elif action == 'score':
                        printable_score = score_calc()
                        print(printable_score)
                    elif action == 'health' or action == 'h':
                        print(player_dict['health'])
                    elif 'get' or 'take' in action:
                        for item in new_room['items']:
                            if item in action:
                                usable_inventory.append(item)
                                new_room['items'].remove(item)
                                print(item.upper() + ' added to inventory!')
                            else:
                                print('Sorry, I can\'t get that.')
                    elif 'use' in action:
                        if 'healing potion' in action:
                            player_dict['health'] += 10
                            usable_inventory.remove(item)
                            print('You gained 10 health! You now have ' + str(player_dict['health']) + ' HP.')
                        elif item == 'mystery herb':
                            if random.random() < 0.4:
                                player_dict['health'] += 5
                                usable_inventory.remove(item)
                                print('You gained 5 health! You now have ' + str(player_dict['health']) + ' HP.')
                            elif heal_chance < random.random() < 0.8:
                                player_dict['health'] -= 5
                                usable_inventory.remove(item)
                                print('You lost 5 health. You now have ' + str(player_dict['health']) + ' HP.')
                            else:
                                print('That is not in your inventory.')


        except ValueError:
            print("Sorry, I didn't understand that.")
            continue

# creates a new room_gen(), then moves the player into the new room
def move_and_take_actions(new_room, action):

    global room_number
    global x_coord
    global y_coord

    # tracking the room and player location using a coordinate system
    if action == 'north':
        y_coord += 1
    elif action == 'south':
        y_coord -= 1
    elif action == 'east':
        x_coord += 1
    elif action == 'west':
        x_coord -= 1

    coordinates = (x_coord, y_coord)

    if coordinates not in list_of_existing_coordinates:
        room_number += 1
        dict_of_all_rooms[room_number] = coordinates
        list_of_existing_coordinates.append(coordinates)
        room_gen(new_room)
    elif coordinates in list_of_existing_coordinates:
        for key, value in dict_of_all_rooms.items():
            if coordinates == value:
                room_to_load = key
                pre_load_room(room_to_load)


def pre_load_room(room_to_load):
    for room in list_of_all_rooms:
        if room['number'] == room_to_load:
            load_existing_room(room)

def load_existing_room_after_item_drop(room):
    room_to_fetch = list_of_all_rooms[room - 1]
    directions_to_leave = room_to_fetch['directions']
    handle_directional_input(room_to_fetch, directions_to_leave)

def load_existing_room(room):
    directions_to_leave = room['directions']
    handle_directional_input(room, directions_to_leave)


## COMBAT ##

# these are currently unused, but could be added for variable amounts of damage...
orc_attacks_list = ['Hammer Fist', 'Rotted Severed Limb', 'Rusty Dagger']
wizard_attacks_dict = ['Demonic Incantation', 'Curse of the Ancients', 'Spiritual Maelstrom']
rat_attacks_dict = ['Rabid Bite', 'Vociferous Scratch', 'Iron Tail']
ghoul_attacks_dict = ['Haunted Slap', 'Spectre Smash', 'Ghostly Gash']

# handle combat commands, turn-taking, and health tracking
def combat_phase(enemy, room_number):
    global ambush
    global player_dict

    turn = random.choice(['player','enemy'])

    if ambush == True:
        turn = 'enemy'

    player_hp = player_dict['health']

    if enemy == 'orc':
        enemy_health = 4
        enemy_dict = all_enemies_list[0]
    elif enemy == 'wizard':
        enemy_health = 5
        enemy_dict = all_enemies_list[1]
    elif enemy == 'rat':
        enemy_health = 2
        enemy_dict = all_enemies_list[2]
    elif enemy == 'ghoul':
        enemy_health = 3
        enemy_dict = all_enemies_list[3]


    while enemy_health > 0:
        if turn == 'player':
            ambush = False
            try:
                action = input('What would you like to do? a: Attack | f: Flee ')
                action = action.lower()
                if action == 'a':
                    attack_value = player_dict['attack']
                    enemy_health = enemy_health - attack_value
                    print('You deal ' + str(attack_value) + str(' damage.'))
                    print('The ' + enemy_dict['name'] + ' has ' + str(enemy_health) + ' health remaining.')
                    turn = 'enemy'
                elif action == 'f':
                    flee_num = random.randrange(101)
                    if player_dict['speed'] >= 1 <= 3:
                        if flee_num <= 75:
                            print('You couldn\'t get away!')
                            turn = 'enemy'
                        else:
                            print('You got away!')
                            break
                    elif player_dict['speed'] >= 4 <= 6:
                        if flee_num <= 60:
                            print('You couldn\'t get away!')
                            turn = 'enemy'
                        else:
                            print('You got away!')
                            break
                    elif player_dict['speed'] >= 7 <= 8:
                        if flee_num <= 20:
                            print('You couldn\'t get away!')
                            turn = 'enemy'
                        else:
                            print('You got away!')
                            break
                    elif player_dict['speed'] >= 10:
                        if flee_num <= 5:
                            print('You couldn\'t get away!')
                            turn = 'enemy'
                        else:
                            print('You got away!')
                            break
                elif action != 'a' or action != 'f':
                    print("Sorry, I didn't understand that.")
                    continue

                turn = 'enemy'

            except ValueError:
                print("Sorry, I didn't understand that.")
                continue
        elif turn == 'enemy':
            if enemy == 'orc':
                attack_num = random.randrange(101)
                if attack_num >= 33:
                    player_hp = player_hp - 4
                    print('Orc attacks for 4 damage!')
                    print('Player health:' + str(player_hp))
                    if player_hp < 0:
                        print('YOU DIED.')
                        break
                    else:
                        turn = 'player'
            elif enemy == 'wizard':
                attack_num = random.randrange(101)
                if attack_num >= 43:
                    player_hp = player_hp - 6
                    print('Orc attacks for 4 damage!')
                    print('Player health:' + str(player_hp))
                    if player_hp < 0:
                        print('YOU DIED.')
                        break
                    else:
                        turn = 'player'
            elif enemy == 'rat':
                attack_num = random.randrange(101)
                if attack_num >= 20:
                    player_hp = player_hp - 2
                    print('Orc attacks for 4 damage!')
                    print('Player health:' + str(player_hp))
                    if player_hp < 0:
                        print('YOU DIED.')
                        break
                    else:
                        turn = 'player'
            elif enemy == 'ghoul':
                attack_num = random.randrange(101)
                if attack_num >= 29:
                    player_hp = player_hp - 4
                    print('Orc attacks for 4 damage!')
                    print('Player health:' + str(player_hp))
                    if player_hp < 0:
                        print('YOU DIED.')
                        break
                    else:
                        turn = 'player'

    if enemy_health <= 0:
        print('You are victorious!')
        player_dict['health'] = player_hp
        if enemy == 'orc':
            list_of_all_rooms[room_number - 1]['enemies'].remove('Wretched Orc')
        elif enemy == 'wizard':
            list_of_all_rooms[room_number - 1]['enemies'].remove('Dark Wizard')
        elif enemy == 'rat':
            list_of_all_rooms[room_number - 1]['enemies'].remove('Diseased Rat')
        elif enemy == 'ghoul':
            list_of_all_rooms[room_number - 1]['enemies'].remove('Fetid Ghoul')
        item_handling(room_number)

# handle picking up an item
def item_handling(room_number):
    global inventory

    if room_number >= 1 <= 5:
        dropped_item = random.choice(tier_1_drops)
    elif room_number  >=  6 <= 10:
        dropped_item = random.choice(tier_2_drops)
    elif room_number  >=  11 <= 20:
        dropped_item = random.choice(tier_3_drops)
    elif room_number  >=  21 <= 35:
        dropped_item = random.choice(tier_4_drops)
    elif room_number  >=  36:
        dropped_item = random.choice(tier_5_drops)

    print('You found ' + dropped_item + ' on your enemy\'s vanquished corpse.')

    while True:
        try:
            take_item = input('Add it to your inventory? ')
            take_item = take_item.lower()
            if take_item == 'y' or take_item == 'yes':
                inventory.append(dropped_item)
                load_existing_room_after_item_drop(room_number)
            elif take_item == 'n' or take_item == 'no':
                print('You leave the loot to the rats and knaves of the dungeon.')
                load_existing_room_after_item_drop(room_number)

        except ValueError:
            print("Sorry, I didn't understand that.")
            continue

# calculate the player's current score
def score_calc():
    global inventory
    gold_count = 0
    ruby_count = 0
    jewelry_count = 0
    blessed_sapphire_count = 0
    enchanted_tiara_count = 0

    for item in inventory:
        if 'gold' in item:
            if '10' in item:
                gold_count += 10
            if '20' in item:
                gold_count += 20
            if '30' in item:
                gold_count += 30
            if '40' in item:
                gold_count += 40
            if '50' in item:
                gold_count += 50

        if 'ruby' or 'rubies' in item:
            if '1' in item:
                ruby_count += 20
            if '2' in item:
                ruby_count += 30
            if '3' in item:
                ruby_count += 40
            if '4' in item:
                ruby_count += 50
            if '5' in item:
                ruby_count += 60

        if 'diamond' in item:
            jewelry_count += 15

        if 'sapphire' in item:
            blessed_sapphire_count += 300

        if 'tiara' in item:
            enchanted_tiara_count += 500


    score = gold_count + ruby_count + jewelry_count + blessed_sapphire_count + enchanted_tiara_count
    print(score)
    return score


room_gen(previous_room)
