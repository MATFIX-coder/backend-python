class SpaceShip:
    def __init__(self, name, fuel, korpus, speed):
        self.name = name
        self.fuel = fuel
        self.korpus = korpus
        self.speed = speed

    def speed_up(self, value):
        self.speed += value
        self.fuel -= value

    def get_damage(self, damage):
        self.korpus -= damage

class CrewMember:
    def __init__(self, name, role, health, skill):
        self.name = name
        self.role = role
        self.health = health
        self.skill = skill

    def get_hurt(self, damage):
        self.health -= damage

    def train(self, points):
        self.skill += points

class Mission:
    def __init__(self, name, goal, resources):
        self.name = name
        self.goal = goal
        self.resources = resources

    def asteroid_boom(self, ship):
        ship.get_damage(30)

    def oxygen_minus(self, crew_member):
        self.resources -= 10
        crew_member.get_hurt(15)
