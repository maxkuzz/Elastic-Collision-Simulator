def draw_static_info(screen, font, cube1, cube2):
    info1_mass = f"mass: {cube1.mass:.1f} kg"
    info1_vel = f"velocity: {cube1.velocity:.2f} m/s"
    info2_mass = f"mass: {cube2.mass:.1f} kg"
    info2_vel = f"velocity: {cube2.velocity:.2f} m/s"

    screen.blit(font.render(info1_mass, True, (128, 0, 128)), (100, 50))
    screen.blit(font.render(info1_vel,  True, (128, 0, 128)), (100, 75))
    screen.blit(font.render(info2_mass, True, (0, 128, 0)), (700, 50))
    screen.blit(font.render(info2_vel,  True, (0, 128, 0)), (700, 75))
