import pygame, sys
from game import button, states, utils, constants, settings, imageslider


def options_menu(screen):
    # Load settings
    game_settings = settings.load_settings()

    pygame.display.set_caption("Menu")
    #options_background = pygame.image.load("assets/Temp Assets/Settings_Menu.png")
    options_background = pygame.image.load("assets/New Assets/Settings Menu/Settings_Background_with_headings.png")
    options_background = pygame.transform.scale(options_background, screen.get_size()).convert()

    # Attribute headings
    fullscreen_text = utils.get_font(utils.scale_y(constants.SIZE_MEDIUM_SMALL)).render("- TOGGLE FULLSCREEN", True, "Black")
    fullscreen_text_rect = fullscreen_text.get_rect(topleft=(utils.scale_x(175), utils.scale_y(240)))
    
    resolution_text = utils.get_font(utils.scale_y(constants.SIZE_MEDIUM_SMALL)).render("- CHANGE RESOLUTION", True, "Black")
    resolution_text_rect = resolution_text.get_rect(topleft=(utils.scale_x(175), utils.scale_y(315)))
    
    musicvol_text = utils.get_font(utils.scale_y(constants.SIZE_MEDIUM_SMALL)).render("- MUSIC VOLUME", True, "Black")
    musicvol_text_rect = musicvol_text.get_rect(topleft=(utils.scale_x(175), utils.scale_y(460)))
    
    soundvol_text = utils.get_font(utils.scale_y(constants.SIZE_MEDIUM_SMALL)).render("- HIT SOUND VOLUME", True, "Black")
    soundvol_text_rect = soundvol_text.get_rect(topleft=(utils.scale_x(175), utils.scale_y(535)))
    
    audioDel_text = utils.get_font(utils.scale_y(constants.SIZE_MEDIUM_SMALL)).render("- AUDIO DELAY", True, "Black")
    audioDel_text_rect = audioDel_text.get_rect(topleft=(utils.scale_x(175), utils.scale_y(610)))
    
    # Button base sprites
    buttonBase_normal = pygame.image.load("assets/New Assets/Settings Menu/SettingsMenuButton_Normal.png").convert_alpha()
    button_w, button_h = buttonBase_normal.get_size()
    buttonBase_normal = pygame.transform.scale(buttonBase_normal, (utils.scale_x(button_w), utils.scale_y(button_h)))
    
    buttonBase_highlighted = pygame.image.load("assets/New Assets/Settings Menu/SettingsMenuButton_Highlighted.png").convert_alpha()
    buttonBase_highlighted = pygame.transform.scale(buttonBase_highlighted, (utils.scale_x(button_w), utils.scale_y(button_h)))
    
    # Display Settings Buttons
    fullscreen_displaytext = "ON" if game_settings["fullscreen"] else "OFF"
    fullscreen_button = button.Button(image=buttonBase_normal, h_image=buttonBase_highlighted, pos=(utils.scale_x(1645), utils.scale_y(265)),
                                text_input=fullscreen_displaytext, font=utils.get_font(utils.scale_y(constants.SIZE_MEDIUM_TINY)), 
                                base_color="Black", hovering_color="White")
    
    resolution_displaytext = str(game_settings["resolution"][0]) + " x " + str(game_settings["resolution"][1])
    resolution_button = button.Button(image=buttonBase_normal, h_image=buttonBase_highlighted, pos=(utils.scale_x(1645), utils.scale_y(340)),
                                text_input=resolution_displaytext, font=utils.get_font(utils.scale_y(constants.SIZE_MEDIUM_TINY)), 
                                base_color="Black", hovering_color="White")
    
    # Sliders
    slider_bg = pygame.image.load("assets/New Assets/Settings Menu/Slider_Empty.png").convert_alpha()
    slider_w, slider_h = slider_bg.get_size()
    slider_bg = pygame.transform.scale(slider_bg, (utils.scale_x(slider_w), utils.scale_y(slider_h)))
    slider_fill = pygame.image.load("assets/New Assets/Settings Menu/Slider_Fill.png").convert_alpha()
    slider_fill = pygame.transform.scale(slider_fill, (utils.scale_x(slider_w), utils.scale_y(slider_h)))

    slider_w, slider_h = slider_bg.get_size()

    musicvol_slider = imageslider.ImageSlider(
        x=utils.scale_x(1050), y=utils.scale_y(465), width=slider_w, height = slider_h, size = constants.SIZE_SMALL, color = "Black",
        min_val=-1, max_val=1, current_val=0.5,
        label="",
        bg_image=slider_bg,
        fill_image=slider_fill
    )
    
    soundvol_slider = imageslider.ImageSlider(
        x=utils.scale_x(1050), y=utils.scale_y(545), width=slider_w, height = slider_h, size = constants.SIZE_SMALL, color = "Black",
        min_val=-1, max_val=1, current_val=0.5,
        label="",
        bg_image=slider_bg,
        fill_image=slider_fill
    )
    
    audiodel_slider = imageslider.ImageSlider(
        x=utils.scale_x(1050), y=utils.scale_y(625), width=slider_w, height = slider_h, size = constants.SIZE_SMALL, color = "Black",
        min_val=-1, max_val=1, current_val=0.5,
        label="",
        bg_image=slider_bg,
        fill_image=slider_fill
    )
    
    # Keybind Buttons
    rotateL_displaytext = pygame.key.name(game_settings["key_CCW"]).upper()
    rotateL_button = button.Button(image=buttonBase_normal, h_image=buttonBase_highlighted, pos=(utils.scale_x(387), utils.scale_y(830)),
                                text_input=rotateL_displaytext, font=utils.get_font(utils.scale_y(constants.SIZE_MEDIUM_TINY)), 
                                base_color="Black", hovering_color="White")
                                
    rotateR_displaytext = pygame.key.name(game_settings["key_CW"]).upper()
    rotateR_button = button.Button(image=buttonBase_normal, h_image=buttonBase_highlighted, pos=(utils.scale_x(387), utils.scale_y(935)),
                                text_input=rotateR_displaytext, font=utils.get_font(utils.scale_y(constants.SIZE_MEDIUM_TINY)), 
                                base_color="Black", hovering_color="White")
                                
    leftKey_displaytext = pygame.key.name(game_settings["key_1"]).upper()
    leftKey_button = button.Button(image=buttonBase_normal, h_image=buttonBase_highlighted, pos=(utils.scale_x(387), utils.scale_y(1035)),
                                text_input=leftKey_displaytext, font=utils.get_font(utils.scale_y(constants.SIZE_MEDIUM_TINY)), 
                                base_color="Black", hovering_color="White")
                                
    middleKey_displaytext = pygame.key.name(game_settings["key_2"]).upper()
    middleKey_button = button.Button(image=buttonBase_normal, h_image=buttonBase_highlighted, pos=(utils.scale_x(1550), utils.scale_y(935)),
                                text_input=middleKey_displaytext, font=utils.get_font(utils.scale_y(constants.SIZE_MEDIUM_TINY)), 
                                base_color="Black", hovering_color="White")
                                
    rightKey_displaytext = pygame.key.name(game_settings["key_3"]).upper()
    rightKey_button = button.Button(image=buttonBase_normal, h_image=buttonBase_highlighted, pos=(utils.scale_x(1550), utils.scale_y(1035)),
                                text_input=rightKey_displaytext, font=utils.get_font(utils.scale_y(constants.SIZE_MEDIUM_TINY)), 
                                base_color="Black", hovering_color="White")
    
    # Keybinds map
    keybinds_image = pygame.image.load("assets/New Assets/Settings Menu/Keybinds_Map.png").convert_alpha()
    original_w, original_h = keybinds_image.get_size()
    keybinds_image = pygame.transform.scale(keybinds_image, (utils.scale_x(original_w), utils.scale_y(original_h)))

    set_keybinds_button = button.Button(image=None, pos=(utils.scale_x(640), utils.scale_y(250)), 
                             text_input="SET KEYBINDS", font=utils.get_font(utils.scale_y(constants.SIZE_MEDIUM_SMALL)), 
                             base_color="#d7fcd4", hovering_color="White")
    set_resolution_button = button.Button(image=None, pos=(utils.scale_x(640), utils.scale_y(400)), 
                             text_input="SET RESOLUTION", font=utils.get_font(utils.scale_y(constants.SIZE_MEDIUM_SMALL)), 
                             base_color="#d7fcd4", hovering_color="White")
    audio_settings_button = button.Button(image=None, pos=(utils.scale_x(640), utils.scale_y(550)), 
                             text_input="AUDIO SETTINGS", font=utils.get_font(utils.scale_y(constants.SIZE_MEDIUM_SMALL)), 
                             base_color="#d7fcd4", hovering_color="White")
        
    back_button = button.Button(image=None, pos=(utils.scale_x(150), utils.scale_y(650)), 
                             text_input="Back", font=utils.get_font(utils.scale_y(constants.SIZE_MEDIUM_SMALL)), 
                             base_color="#d7fcd4", hovering_color="White")

    
    # Keybind vars
    waiting_for_key = False
    key_to_bind = None
    button_to_update = None
    
    # Keybinds select key overlay
    keybinds_overlay_image = pygame.image.load("assets/New Assets/Settings Menu/Keybinds_SelectKey_Bg.png").convert()
    keybinds_overlay_image = pygame.transform.scale(keybinds_overlay_image, screen.get_size()).convert()
    
    while True:
        
        screen.blit(options_background, (0, 0))

        options_mouse_pos = pygame.mouse.get_pos()

        # Buttons
        for b in [fullscreen_button, resolution_button, rotateL_button, rotateR_button, leftKey_button, middleKey_button, rightKey_button]:
            b.change_color(options_mouse_pos)
            b.update(screen)
            
        # Draw sliders
        for s in [musicvol_slider, soundvol_slider, audiodel_slider]:
            s.draw(screen)

        # Keybinds image 
        screen.blit(keybinds_image, (utils.scale_x(253), utils.scale_y(775)))

        for text, rect in [(fullscreen_text, fullscreen_text_rect), (resolution_text, resolution_text_rect), (musicvol_text, musicvol_text_rect), (soundvol_text, soundvol_text_rect), (audioDel_text, audioDel_text_rect)]:
            screen.blit(text, rect)
        
        #screen.blit(fullscreen_text, fullscreen_text_rect)

        for b in [set_keybinds_button, back_button, set_resolution_button, audio_settings_button]:
            b.change_color(options_mouse_pos)
            b.update(screen)

        for event in pygame.event.get():
            # Sliders
            for s in [musicvol_slider, soundvol_slider, audiodel_slider]:
                s.check_event(event)
        
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not waiting_for_key:
                if set_keybinds_button.check_for_input(options_mouse_pos):
                    return states.SET_KEYBINDS
                elif set_resolution_button.check_for_input(options_mouse_pos):
                    return states.SET_RESOLUTION
                elif audio_settings_button.check_for_input(options_mouse_pos):
                    return states.AUDIO_SETTINGS
                elif back_button.check_for_input(options_mouse_pos):
                    return states.MENU
                elif fullscreen_button.check_for_input(options_mouse_pos):
                    
                    if game_settings["fullscreen"] == True:
                        game_settings["fullscreen"] = False
                        screen = pygame.display.set_mode(game_settings["resolution"])
                        
                    else:
                        game_settings["fullscreen"] = True
                        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                        
                    
                    settings.save_settings(game_settings)
                    constants.SCALE_X = screen.get_width() / constants.BASE_W
                    constants.SCALE_Y = screen.get_height() / constants.BASE_H
                    return states.OPTIONS
                    
                elif resolution_button.check_for_input(options_mouse_pos):
                    print("Resolution Button clicked")
                    
                    if game_settings["fullscreen"] == False:
                        res_w, res_h = screen.get_size()
                        if res_w == 1280 and res_h == 720:
                            res_w = 1920
                            res_h = 1080
                        elif res_w == 1920 and res_h == 1080:
                            res_w = 2560
                            res_h = 1440
                        else:
                            res_w = 1280
                            res_h = 720
                    
                        game_settings["fullscreen"] = False
                        game_settings["resolution"] = [res_w, res_h]
                        settings.save_settings(game_settings)
                        screen = pygame.display.set_mode((res_w, res_h))
                        constants.SCALE_X = res_w / constants.BASE_W
                        constants.SCALE_Y = res_h / constants.BASE_H
                        
                        return states.OPTIONS
                        
                elif rotateL_button.check_for_input(options_mouse_pos):
                    print("Rotate Left button clicked")
                    waiting_for_key = True
                    key_to_bind = "key_CCW"
                    button_to_update = rotateL_button
                    
                elif rotateR_button.check_for_input(options_mouse_pos):
                    print("Rotate Right button clicked")
                    waiting_for_key = True
                    key_to_bind = "key_CW"
                    button_to_update = rotateR_button

                elif leftKey_button.check_for_input(options_mouse_pos):
                    print("Left Key Button Clicked")
                    waiting_for_key = True
                    key_to_bind = "key_1"
                    button_to_update = leftKey_button

                elif middleKey_button.check_for_input(options_mouse_pos):
                    print("Middle Key Button Clicked")
                    waiting_for_key = True
                    key_to_bind = "key_2"
                    button_to_update = middleKey_button

                elif rightKey_button.check_for_input(options_mouse_pos):
                    print("Right Key Button Clicked")
                    waiting_for_key = True
                    key_to_bind = "key_3"
                    button_to_update = rightKey_button

            if event.type == pygame.KEYDOWN:
                if waiting_for_key:
                    if event.key == pygame.K_ESCAPE:
                        waiting_for_key = False
                    else:
                        game_settings[key_to_bind] = event.key
                        button_to_update.text_input = pygame.key.name(event.key).upper()
                        settings.save_settings(game_settings)
                        waiting_for_key = False
            
                elif event.key == pygame.K_ESCAPE:
                    return states.MENU

        if waiting_for_key:
            screen.blit(keybinds_overlay_image, (0, 0))
            

        pygame.display.flip()

                    


