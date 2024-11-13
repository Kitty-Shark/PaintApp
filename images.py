#Image module

from pygame import image, transform

#Load images
#Image for icon/logo
iconImage = image.load("images/icon.png")

#Image for mouse
mouse = image.load("images/Mouse.png")
mouse_text = image.load("images/Mouse_Text.png")



#Images for tools
menu = image.load("images/Menu.png")
clear = image.load("images/Clear.png")
save = image.load("images/Save.png")
load_image = image.load("images/Plus.png")
undo = image.load("images/Undo.png")
redo = image.load("images/Redo.png")
pencil = image.load("images/Pencil.png")
eraser = image.load("images/Eraser.png")
bucket = image.load("images/Bucket.png")
brush = image.load("images/Brush.png")
rectangles_1 = image.load("images/rectangle_1.png")
rectangles_2 = image.load("images/rectangle_2.png")
rectangle_filled = image.load("images/Rectangle_Filled.png")
rectangle_unfilled = image.load("images/Rectangle_Unfilled.png")
ellipse_1 = image.load("images/ellipse_1.png")
ellipse_2 = image.load("images/ellipse_2.png")
ellipse_filled = image.load("images/Ellipse_Filled.png")
ellipse_unfilled = image.load("images/Ellipse_Unfilled.png")
line = image.load("images/Line.png")
eyedropper = image.load("images/EyeDropper.png")
marker = image.load( "images/Marker.png")
pen = image.load( "images/Pen.png")
text = image.load("images/Text.png")
spray_paint = image.load("images/SprayPaint.png")
magic_eraser = image.load("images/Magic_Eraser.png")
slide = image.load("images/Slide.png")

#Images for lockscreen
navigation_gradient = image.load("images/NavigationBarGradient.png")
notification_gradient = image.load("images/NotificationBarGradient.png")
arrow = image.load("images/Arrow.png")

#Images for color picker and stamps
color_picker = image.load("images/ColorPicker.png")


#Icons for menu
reset_menu = image.load("images/Reset.png")
help_menu = image.load("images/Help.png")
shutdown_menu = image.load("images/Shutdown.png")

#Transform images
iconImage = transform.scale(iconImage, (52,52))
navigation_gradient = transform.scale(navigation_gradient, (500, 750))
notification_gradient = transform.scale(notification_gradient, (500, 750))
color_picker = transform.scale(color_picker, (370, 240))