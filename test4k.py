import pygame
import numpy
import math
import random

# Initialize Pygame
pygame.init()

# Sound synthesis parameters
SAMPLE_RATE = 44100

def synthesize_sound(duration, frequency, waveform='sine'):
    """Generate a waveform-based sound."""
    num_samples = int(SAMPLE_RATE * duration)
    buffer = numpy.zeros((num_samples, 2), dtype=numpy.int16)
    max_int16 = 2**15 - 1

    for i in range(num_samples):
        t = float(i) / SAMPLE_RATE
        if waveform == 'sine':
            value = math.sin(2 * math.pi * frequency * t)
        elif waveform == 'square':
            value = 1.0 if math.sin(2 * math.pi * frequency * t) > 0 else -1.0
        elif waveform == 'triangle':
            value = 2.0 * abs(2 * (t * frequency % 1) - 1) - 1.0
        elif waveform == 'noise':
            value = random.uniform(-1.0, 1.0)
        buffer[i] = int(max_int16 * value), int(max_int16 * value)

    sound = pygame.sndarray.make_sound(buffer)
    return sound

# Create sounds
snd1 = synthesize_sound(0.2, 880, 'square')  # High-pitched square wave
snd2 = synthesize_sound(0.3, 440, 'triangle')  # Soft triangle wave
eat_sound = synthesize_sound(0.2, 600, 'sine')  # Simple beep
game_over_sound = synthesize_sound(0.5, 120, 'triangle')  # Falling pitch sound
annoying_cat_sound = synthesize_sound(0.5, 880, 'noise')  # Noise effect

# Simple sound test interface
def sound_test():
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("Sound Test: Retro Engine")
    font = pygame.font.SysFont(None, 40)

    sounds = [
        ("1: SND1", snd1),
        ("2: SND2", snd2),
        ("3: Eat", eat_sound),
        ("4: Game Over", game_over_sound),
        ("5: Annoying Cat", annoying_cat_sound),
    ]

    running = True
    while running:
        screen.fill((0, 0, 0))
        y_offset = 50
        for text, _ in sounds:
            label = font.render(text, True, (255, 255, 255))
            screen.blit(label, (50, y_offset))
            y_offset += 40
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    snd1.play()
                elif event.key == pygame.K_2:
                    snd2.play()
                elif event.key == pygame.K_3:
                    eat_sound.play()
                elif event.key == pygame.K_4:
                    game_over_sound.play()
                elif event.key == pygame.K_5:
                    annoying_cat_sound.play()

    pygame.quit()

# Run the sound test
sound_test()
