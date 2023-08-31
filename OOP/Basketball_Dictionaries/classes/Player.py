class Player:
    def __init__(self, player):
        self.name = player["name"]
        self.age = player["age"]
        self.position = player["position"]
        self.team = player["team"]

    @classmethod
    def get_team(cls, team_list):
        new_team = []
        for playas in team_list:
            new_team.append(cls(playas))
        return new_team