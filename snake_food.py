class Food():
    def __init__(self, screen_width, screen_height):
        '''Инит еды'''
        self.food_size_x = 10
        self.food_size_y = 10
        self.food_pos = [random.randrange(1, screen_width/10)*10,
                         random.randrange(1, screen_height/10)*10]

    def draw_food(self, play_surface):
        '''Отображение еды'''
        play_surface.blit(mushroomImg, (
                self.food_pos[0], self.food_pos[1],
                self.food_size_x, self.food_size_y))
