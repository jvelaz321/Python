class Settings():
    """A class to store all setiings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed_factor = 1.5

        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255
        self.bullets_allowed = 10

        #Alien settings
        self.alien_speed_factor = 1
        
        #fleet_direction of 1 represents right; -1 represents left/
        self.fleet_direction = 1
        self.fleet_drop_speed = 10