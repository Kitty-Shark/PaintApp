#Font module

from pygame import font

#Initialize fonts

font.init()

#Status Bar Fonts
status_bar_project_name_font = font.Font("fonts/Roboto-Regular.ttf", 15)


#Size Text Font
size_text_font = font.Font("fonts/Roboto-Regular.ttf", 18)


#Dialog Fonts
dialog_title_font = font.Font("fonts/Roboto-Regular.ttf", 20)
dialog_body_font = font.Font("fonts/Roboto-Regular.ttf", 15)
dialog_button_font = font.Font("fonts/Roboto-Regular.ttf", 12)

#App Font
app_title_font = font.Font("fonts/Rodondo-500.ttf", 45)