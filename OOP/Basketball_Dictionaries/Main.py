from classes.Player import Player

players = [
    {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "Small Forward", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving", 
    	"age":32,
        "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard", 
    	"age":33,
        "position": "Point Guard", 
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid", 
    	"age":32,
        "position": "Power Foward", 
    	"team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }

]

kevin = {
    "name": "Kevin Durant", 
    "age": 34, 
    "position": "Small Forward", 
    "team": "Brooklyn Nets"
}
jason = {
    "name": "Jason Tatum", 
    "age": 24, 
    "position": "small forward", 
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving", 
    "age": 32,
    "position": "Point Guard", 
    "team": "Brooklyn Nets"
}


kevin = Player(kevin)
jason = Player(jason)
kyrie = Player(kyrie)

print(kevin.name + " " + kevin.position + " " + kevin.team, kevin.age)
print(jason.name + " " + jason.position + " " + jason.team, jason.age)
print(kyrie.name + " " + kyrie.position + " " + kyrie.team, kyrie.age)
print(f'Hello, my name is {kyrie.name}. I play professional Basketball for the {kyrie.team}. I play {kyrie.position} position and my age is: {kyrie.age}')

print(players)

team = Player.get_team(players)

entire_list = []
for r in players:
    entire_list.append(Player(r))
print(entire_list)