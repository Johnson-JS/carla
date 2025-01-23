import pygame

# Initialize Pygame's joystick module
pygame.init()
pygame.joystick.init()

# Ensure a joystick is connected
if pygame.joystick.get_count() == 0:
    print("No joystick connected!")
    exit()

# Initialize the first joystick
joystick = pygame.joystick.Joystick(0)
joystick.init()

print(f"Joystick Name: {joystick.get_name()}")
print(f"Number of Axes: {joystick.get_numaxes()}")
print(f"Number of Buttons: {joystick.get_numbuttons()}")

# Event loop to display the mappings
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.JOYAXISMOTION:
            print(f"Axis {event.axis} value: {event.value}")
        elif event.type == pygame.JOYBUTTONDOWN:
            print(f"Button {event.button} pressed")
        elif event.type == pygame.JOYBUTTONUP:
            print(f"Button {event.button} released")
