import pygame
import sys
import random



pygame.init()

WIDTH, HEIGHT = 900, 600  # 게임 창의 가로, 세로 크기
CARD_WIDTH, CARD_HEIGHT = 71, 96  # 카드의 가로, 세로 크기
FPS = 60  # 초당 프레임 수
BLACK = (0, 0, 0)  # 검은색
WHITE = (255, 255, 255)  # 흰색
RED = (255, 0, 0)  # 빨간색
GREEN = (20, 75, 20)  # 초록색
FONT_SIZE = 36  # 폰트 크기

screen = pygame.display.set_mode((WIDTH, HEIGHT))  # 게임 창 생성
pygame.display.set_caption("BLACKJACK")  # 게임 창 타이틀
clock = pygame.time.Clock()  # 시간을 제어하기 위한 Clock 객체 생성

def load_card_images(): #카드 이미지를 불러와 크기를 조정하여 딕셔너리에 저장하는 함수
    card_images = {}
    for suit in ['hearts', 'diamonds', 'clubs', 'spades']:
        for rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']:
            image = pygame.image.load(f"{rank}_{suit}.png")
            card_images[(rank, suit)] = pygame.transform.scale(image, (CARD_WIDTH, CARD_HEIGHT))
    return card_images

card_images = load_card_images()  # 카드 이미지 로드

player_hand = []  # 플레이어 손패
dealer_hand = []  # 딜러 손패
deck = [('2', 'hearts'), ('3', 'hearts'), ('4', 'hearts'), ('5', 'hearts'), ('6', 'hearts'), ('7', 'hearts'),
        ('8', 'hearts'), ('9', 'hearts'), ('10', 'hearts'), ('J', 'hearts'), ('Q', 'hearts'), ('K', 'hearts'), ('A', 'hearts'),
        ('2', 'diamonds'), ('3', 'diamonds'), ('4', 'diamonds'), ('5', 'diamonds'), ('6', 'diamonds'), ('7', 'diamonds'),
        ('8', 'diamonds'), ('9', 'diamonds'), ('10', 'diamonds'), ('J', 'diamonds'), ('Q', 'diamonds'), ('K', 'diamonds'), ('A', 'diamonds'),
        ('2', 'clubs'), ('3', 'clubs'), ('4', 'clubs'), ('5', 'clubs'), ('6', 'clubs'), ('7', 'clubs'),
        ('8', 'clubs'), ('9', 'clubs'), ('10', 'clubs'), ('J', 'clubs'), ('Q', 'clubs'), ('K', 'clubs'), ('A', 'clubs'),
        ('2', 'spades'), ('3', 'spades'), ('4', 'spades'), ('5', 'spades'), ('6', 'spades'), ('7', 'spades'),
        ('8', 'spades'), ('9', 'spades'), ('10', 'spades'), ('J', 'spades'), ('Q', 'spades'), ('K', 'spades'), ('A', 'spades')]

font = pygame.font.SysFont(None, FONT_SIZE)  # 폰트 설정

def draw_text(text, color, x, y): #화면에 텍스트를 그림
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

def shuffle_deck(): #덱을 섞음
    random.shuffle(deck)

def deal_initial_cards(): #초기 카드를 나눔
    for _ in range(2):
        player_hand.append(deck.pop())
        dealer_hand.append(deck.pop())

def display_hand(hand, y, is_player=True):
    x = 50
    for card in hand:
        screen.blit(card_images[card], (x, y))
        x += 40
        pygame.time.wait(600)

    if is_player:
        pygame.draw.rect(screen, GREEN, pygame.Rect(0, HEIGHT - CARD_HEIGHT - 80, WIDTH // 2, FONT_SIZE))
        total_text = f"Player: {get_hand_value(player_hand)}"
        draw_text(total_text, WHITE, WIDTH // 4, HEIGHT - CARD_HEIGHT - 50)
    else:
        pygame.draw.rect(screen, GREEN, pygame.Rect(0, y + CARD_HEIGHT + 10, WIDTH // 2, FONT_SIZE))
        total_text = f"Dealer: {get_hand_value(dealer_hand)}"
        draw_text(total_text, WHITE, WIDTH // 4, y + CARD_HEIGHT + 40)


def get_hand_value(hand): #손의 카드 값 계산
    value = 0
    num_aces = 0

    for card in hand:
        if card[0] in ['K', 'Q', 'J']:
            value += 10
        elif card[0] == 'A':
            value += 11
            num_aces += 1
        else:
            value += int(card[0])

    while value > 21 and num_aces:
        value -= 10
        num_aces -= 1

    return value

def game_over(message): #게임 종료 화면을 표시하고 잠시 후에 게임을 재설정
    draw_text(message, RED, WIDTH // 2, HEIGHT // 2)
    pygame.display.flip()
    pygame.time.wait(3000)
    reset_game()

def reset_game(): #게임을 재설정
    player_hand.clear()
    dealer_hand.clear()
    shuffle_deck()
    deal_initial_cards()

def run_game():
    game_state = "playing"  
    shuffle_deck()
    deal_initial_cards()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(GREEN)

        if game_state == "playing":
            # 플레이어
            display_hand(player_hand, HEIGHT - CARD_HEIGHT - 20)

            if get_hand_value(player_hand) == 21:
                game_state = "game_over"
                game_over("Blackjack! Player Win!")

            elif get_hand_value(player_hand) > 21:
                game_state = "game_over"
                game_over("Player Bust! Dealer Win!")

            else:
                draw_text("Press 'h' to hit or 's' to stand", WHITE, WIDTH // 2, HEIGHT - CARD_HEIGHT)
                pygame.display.flip()

                waiting_for_input = True
                while waiting_for_input:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_h:
                                player_hand.append(deck.pop())
                                display_hand(player_hand, HEIGHT - CARD_HEIGHT - 20)
                                pygame.display.flip()  # 화면 업데이트
                            elif event.key == pygame.K_s:
                                waiting_for_input = False
                # 딜러
                while get_hand_value(dealer_hand) < 17:
                    dealer_hand.append(deck.pop())

                display_hand(dealer_hand, 30, is_player=False)

                pygame.time.wait(1000)

                if get_hand_value(dealer_hand) == 21:
                    game_state = "game_over"
                    game_over("Blackjack! Dealer Win!")

                elif get_hand_value(dealer_hand) > 21:
                    if get_hand_value(player_hand) > 21:
                        game_state = "game_over"
                        game_over("Draw!")
                    else:
                        game_state = "game_over"
                        game_over("Dealer Bust! Player Win!")

                elif get_hand_value(player_hand) > 21:
                    game_state = "game_over"
                    game_over("Player Bust! Dealer Win!")

                elif 21 > get_hand_value(player_hand) > get_hand_value(dealer_hand):
                    game_state = "game_over"
                    game_over("Player Win!")

                elif get_hand_value(player_hand) < get_hand_value(dealer_hand):
                    game_state = "game_over"
                    game_over("Dealer Win!")
                elif get_hand_value(player_hand) ==21:
                    game_state = "game_over"
                    game_over("Blackjack! Player Win!!")
                else:
                    game_state = "game_over"
                    game_over("Draw!")

        elif game_state == "game_over":
            draw_text("Do you want to play again? (y/n)", WHITE, WIDTH // 2, HEIGHT // 2)
            pygame.display.flip()

            waiting_for_input = True
            while waiting_for_input:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_y:
                            reset_game()
                            game_state = "playing"
                            waiting_for_input = False
                        elif event.key == pygame.K_n:
                            pygame.quit()
                            sys.exit()

        pygame.display.flip()
        clock.tick(FPS)

run_game()  # 게임 실행