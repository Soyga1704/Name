class Game():
    def __init__(self):
        self.screen_width = 720
        self.screen_height = 460

        self.red = pygame.Color(255, 0, 0)
        self.green = pygame.Color(0, 255, 0)
        self.black = pygame.Color(0, 0, 0)
        self.white = pygame.Color(255, 255, 255)
        self.brown = pygame.Color(165, 42, 42)
        self.blue = pygame.Color(50, 153, 213)

        self.fps_controller = pygame.time.Clock()

        self.score = 0

    def init_and_check_for_errors(self):
        '''Начальная функция для инициализации и проверки как запустится pygame'''
        check_errors = pygame.init()
        if check_errors[1] > 0:
            sys.exit()
        else:
            print('Ok')
  
    def set_surface_and_title(self):
        '''Задаем surface (поверхность поверх которой будет все рисоваться) и устанавливаем загаловок окна'''
        self.play_surface = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Snake Game')

    def event_loop(self, change_to):
        '''Функция для отслеживания нажатий клавиш игроком'''
 
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    change_to = "RIGHT"
                elif event.key == pygame.K_LEFT or event.key == ord('a'):
                    change_to = "LEFT"
                elif event.key == pygame.K_UP or event.key == ord('w'):
                    change_to = "UP"
                elif event.key == pygame.K_DOWN or event.key == ord('s'):
                    change_to = "DOWN"
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
        return change_to

    def refresh_screen(self):
        '''обновляем экран'''
        pygame.display.flip()
        game.fps_controller.tick(23)

    def show_score(self, choice=1):
        '''Отображение результата'''
        s_font = pygame.font.SysFont('monaco', 24)
        s_surf = s_font.render(
            'Score: {0}'.format(self.score), True, self.black)
        s_rect = s_surf.get_rect()
        if choice == 1:
            s_rect.midtop = (80, 10)
        else:
            s_rect.midtop = (360, 120)
        self.play_surface.blit(s_surf, s_rect)

    def game_over(self):
        '''Функция для вывода надписи Game Over и результатов в случае завершения игры и выход из игры'''
        go_font = pygame.font.SysFont('monaco', 72)
        go_surf = go_font.render('Game over', True, self.red)
        go_rect = go_surf.get_rect()
        go_rect.midtop = (360, 15)
        self.play_surface.blit(go_surf, go_rect)
        self.show_score(0)
        pygame.display.flip()
        time.sleep(3)
        pygame.quit()
        sys.exit()
