from os import environ
from time import strftime, localtime
from math import hypot
from tkinter import messagebox
from tkinter import *
from tkinter import filedialog

from pygame import *
from pygame import gfxdraw

import sys
import fonts
import images
import rects
import rdraw
import dialog

def draw_tool(tool):
    global rx, ry,user_blit_count,current_color,mouse_color_at,color_pos
    if tool == 'pencil':
        rdraw.pencil(main_copy, current_color, mx, my, ox, oy, size)
    if tool == 'eraser':
        rdraw.eraser(main_copy, mx, my, ox, oy, size)
    if tool == 'bucket':
        if not draw_canvas:
            main_copy.fill((current_color))
        mouse_color_at = main_copy.get_at((mx, my))
        rdraw.flood_fill(main_copy, mx, my, mouse_color_at, current_color, canvas)
    if tool == 'brush':
        rdraw.brush(main_copy, current_color, mx, my, ox, oy, size)
    if tool == 'rectangle_filled':
        rdraw.rectangle_filled(main, current_color, rx, ry, mx, my)
    if tool == 'rectangle_unfilled':
        rdraw.rectangle_unfilled(main, current_color, (rx, ry), (mx, my), size)
    if tool == 'ellipse_filled':
        rdraw.ellipse_filled(main, current_color, rx, ry, mx, my)
    if tool == 'ellipse_unfilled':
        rdraw.ellipse_unfilled(main, current_color, rx, ry, mx, my, size)
    if tool == "line":
        if pressed[K_LSHIFT] or pressed[K_RSHIFT]:
            lx, ly = abs(rx - mx), abs(ry - my)
            if lx > ly:
                rdraw.line(main, current_color, rx,ry, mx, ry, size)
            elif lx < ly:
                rdraw.line(main, current_color, rx,ry, rx, my, size)
        else:
            rdraw.line(main, current_color, rx, ry, mx, my, size)
    if tool == 'eyedropper' and canvas.collidepoint(mpos):
        current_color = main.get_at(mpos)
        color_pos = (431,885)
    if tool == "marker":
        rdraw.marker(main_copy, current_color, mx, my, ox, oy, size)
    if tool == 'pen':
        rdraw.pen(main_copy, current_color, mx, my, ox, oy, size)
    if tool == 'text':
        global enable_text, tx, ty
        enable_text = True
        tx, ty = mx, my
    if tool == 'spray_paint':
        rdraw.spray_paint(main_copy, current_color, mx, my, ox, oy, size)
    if tool == 'magic_eraser':
        mouse_color_at = main_copy.get_at((mx, my))
        rdraw.magic_eraser (main_copy, mx, my, mouse_color_at, (255,255,255), canvas)
    if tool == 'user_image' and user_blit_count == 1:
        global current_image
        img_height = current_image.get_height()
        img_width = current_image.get_width()
        current_image = transform.scale(current_image, (img_width + (size - 1) * 10, img_height + (size - 1) * 10))
        main_copy.blit(current_image, (mx - img_width // 2, my - img_height // 2))
        user_blit_count = 0


def draw_rect_ellipse_line(tool):
    if tool == 'rectangle_filled':
        rdraw.rectangle_filled(main_copy, current_color, rx, ry, mx,my)
    if tool == 'rectangle_unfilled':
        rdraw.rectangle_unfilled(main_copy, current_color, (rx, ry), (mx, my), size)
    if tool == 'ellipse_filled':
        rdraw.ellipse_filled(main_copy, current_color, rx, ry, mx, my)
    if tool == 'ellipse_unfilled':
        rdraw.ellipse_unfilled(main_copy, current_color, rx, ry, mx, my, size)
    if tool == "line":
        if pressed[K_LSHIFT] or pressed[K_RSHIFT]:
            dx, dy = abs(rx - mx), abs(ry - my)
            if dx > dy:
                rdraw.line(main_copy, current_color, rx,ry, mx, ry, size)
            elif dx < dy:
                rdraw.line(main_copy, current_color, rx,ry, rx, my, size)
        else:
            rdraw.line(main_copy, current_color, rx, ry, mx, my, size)


def quit_program():
    global show_dialog, current_dialog
    show_dialog = True
    current_dialog = 2


def save_work():
    global file_name
    global draw_canvas
    directory = filedialog.asksaveasfilename()
    directory_get_name = directory
    if len(directory) > 1:
        file_name = ''
        while '/' not in file_name:
            file_name += directory_get_name[-1]
            directory_get_name = directory_get_name[:-1]
        file_name = file_name[:-1][::-1]
        image.save(main_copy.subsurface(canvas), '%s.jpg' % directory)
        file_name += " - Хакатон Андройд"
        display.set_caption(file_name)
        draw_canvas = False


def filled_rects():


    draw.rect(main, (33, 33, 33), (0, 25, 1000, 56))
    draw.rect(main, (33, 33, 33), (56, 81, 944, 5))


    draw.rect(main, (33, 33, 33), (1000, 0, 45, 208))
    draw.rect(main, (33, 33, 33), (1000, 208, 45, 209))
    draw.rect(main, (33, 33, 33), (1000, 417, 45, 208))


    draw.rect(main, (0, 0, 0), (0, 0, 1068, 25))


    draw.rect(main, (33, 33, 33), (0, 625, 1045, 275))
    draw.rect(main, (33, 33, 33), (56, 625, 989, 5))


    draw.rect(main, (33, 33, 33), (0, 81, 56, 544))
    draw.rect(main, (33, 33, 33), (56, 86, 5, 959))


def load_image():
    global show_dialog, current_dialog
    user_file = filedialog.askopenfilename(filetypes=(('Images', '*.jpg;*.jpeg;*.png;*.gif;*.bmp'), ('All files', '*.*')))
    user_file_name = str(user_file)
    correct_file_type = False
    for ext in image_ext:
        if ext in user_file_name:
            correct_file_type = True
    if correct_file_type:
        global current_image
        global current_tool
        current_image = image.load(user_file)
        current_tool = 'user_image'
    elif correct_file_type == False and len(user_file_name) > 1:
        current_dialog = 4
        show_dialog = True


def hover(tool):
    draw.rect(main, (66, 66, 66), tool)


def size_font_text(color):
    r = color[0]
    g = color[1]
    b = color[2]
    text_color = (255, 255, 255)
    if r > 200 or g > 200 or b > 200:
        text_color = (0, 0, 0)
    return text_color


def color_picker():
    global current_color
    draw.rect(main, (255, 255, 255), (0, 625, 1045, 275))
    main.blit(images.color_picker, (15, 640))
    if mb[0] == 1 and rects.color_picker_rect.collidepoint(mpos):
        current_color = main.get_at(mpos)


def reset():
    global size, current_color, current_tool, current_tool_selected, draw_canvas
    size = 4
    current_color = (0, 0, 0)
    current_tool = 'pencil'
    current_tool_selected = rects.pencil_rect
    main_copy.fill((255,255,255))
    draw_canvas = False


def undo():
    global undo_list, redo_list
    try:
        redo_list.append(undo_list.pop()) 
        main_copy.blit(undo_list[-1], (0,0))
    except:
        pass


def redo():
    global undo_list, redo_list
    try:
        main_copy.blit(redo_list[-1], (0,0))
        undo_list.append(redo_list.pop())
    except:
        pass


file_name = 'Drawing app'
display.set_icon(images.iconImage)
display.set_caption(file_name)
environ['SDL_VIDEO_WINDOW_POS'] = '0,0'

running = True
lockscreen = True
drag_lock_icon = False
draw_canvas = False
show_dialog = False
ask_save = False
click = False
drawing = False
show_rect = False
show_ellipse = False
enable_text = False

lock_count = 1
lock_icon_pos_x = 210
lock_icon_pos_y = 500
user_blit_count = 0
main_count = 1
size = 4
saves = 1
current_tool = 'pencil'
old_tool = current_tool
current_color = (0, 0, 0, 255)
current_tool_selected = rects.pencil_rect
(ox, oy) = mouse.get_pos()
tx, ty = mouse.get_pos()
canvas = Rect(61, 86, 939, 539)
background_color = (255, 255, 255, 255)
rect_ellipse_line_count = 0
stamp_count = 0
color_pos = (431,885)
user_text = ''
load_success_text = ["Your selected image has been successfully",  "loaded. Click anywhere on the screen to", "place the image there. Note: Size 1 will", "be the original image size. Increasing the", "size will increase the width and height of", "the image by 10px."]
load_fail_text = ['Sorry, looks like you are trying to load', 'an unsupported image. Acceptable file', 'types are: JPG, PNG, GIF, and BMP']

img = [
    images.clear,
    images.save,
    images.pencil,
    images.eraser,
    images.bucket,
    images.load_image,
    images.brush,
    images.rectangles_1,
    images.rectangles_2,
    images.ellipse_1,
    images.ellipse_2,
    images.line,
    images.eyedropper,
    images.color_picker,
    images.slide,
    images.marker,
    images.pen,
    images.text,
    images.spray_paint,
    images.magic_eraser,
    images.redo,
    images.undo,
    images.iconImage,
]

img_location = [
    (892, 29),
    (836, 29),
    (4, 85),
    (4, 141),
    (4, 197),
    (780, 29),
    (4, 253),
    (18, 322),
    (4, 309),
    (18, 378),
    (4, 365),
    (4, 421),
    (4, 477),
    (61, 645),
    (-20, 35),
    (4, 531),
    (4, 589),
    (4, 645),
    (4, 701),
    (4, 757),
    (724,29),
    (668,29),
    (23,27),
]

# Rects list

rects_list = [
    rects.pencil_rect,
    rects.eraser_rect,
    rects.bucket_rect,
    rects.brush_rect,
    rects.rectangle,
    rects.ellipse,
    rects.line_rect,
    rects.eyedropper_rect,
    rects.load_image_rect,
    rects.save_rect,
    rects.clear_rect,
    rects.marker_rect,
    rects.pen_rect,
    rects.text_rect,
    rects.spray_paint_rect,
    rects.magic_eraser_rect,
    rects.redo_rect,
    rects.undo_rect,
]


#
undo_list = []
redo_list = []


image_ext = ['jpg', 'jpeg', 'png', 'gif', 'bmp']


dialog_list = ["save", "load_fail"]


app = Tk()
app.withdraw()
while running:

    if main_count == 1:
        main = display.set_mode((1045, 900))
        main.fill(background_color)
        main_count = 0
        main_copy = main.copy()
        undo_list.append(main_copy.copy())
        reset()


    mx, my = mouse.get_pos()
    mb = mouse.get_pressed()
    mpos = mouse.get_pos()


    pressed = key.get_pressed()
    ctrl_held = pressed[K_LCTRL] or pressed[K_RCTRL]

    for e in event.get():
        if e.type == QUIT:
            quit_program()

        if e.type == MOUSEBUTTONUP and e.button == 1 and canvas.collidepoint(mpos):
            undo_list.append(main_copy.copy())

        if e.type == KEYDOWN and enable_text and not show_dialog:
            letter = e.unicode
            if e.key != 8 and not ctrl_held:
                user_text += letter
            if e.key == K_BACKSPACE:
                try:
                    user_text = user_text[:-1]
                except:
                    pass
            if e.key == K_SPACE:
                user_text += ' '
            if e.key == K_RETURN:
                rdraw.text(main_copy, current_color, tx, ty, size, user_text)
                enable_text = False
                user_text = ''
            if e.key == K_ESCAPE:
                user_text = ''
                enable_text = False

        elif e.type == KEYDOWN and not show_dialog:

            # Keyboard shortcuts

            if e.key == K_q and ctrl_held:
                quit_program()
            if e.key == K_s and ctrl_held:
                save_work()
            if e.key == K_r and ctrl_held:
                reset()
            if e.key == K_z and ctrl_held:
                undo()
            if e.key == K_y and ctrl_held:
                redo()
            if e.key == K_p:
                current_tool = "pencil"
                current_tool_selected = rects.pencil_rect
            if e.key == K_e:
                current_tool = "eraser"
                current_tool_selected = rects.eraser_rect
            if e.key == K_b:
                current_tool = "brush"
                current_tool_selected = rects.brush_rect
            if e.key == K_l:
                current_tool = "line"
                current_tool_selected = rects.line_rect
            if e.key == K_f:
                current_tool = "bucket"
                current_tool_selected = rects.bucket_rect
            if e.key == K_m:
                current_tool = "magic_eraser"
                current_tool_selected = rects.magic_eraser_rect
            if e.key == K_s:
                current_tool = "spray_paint"
                current_tool_selected = rects.spray_paint_rect
            if e.key == K_k:
                current_tool = "marker"
                current_tool_selected = rects.marker_rect
            if e.key == K_c:
                current_tool = "pen"
                current_tool_selected = rects.pen_rect
            if e.key == K_t:
                current_tool = "text"
                current_tool_selected = rects.text_rect
            if e.key == K_d:
                current_tool = "eyedropper"
                current_tool_selected = rects.eyedropper_rect

            # Size shortcut

            if e.key == K_1: size = 1
            if e.key == K_2: size = 2
            if e.key == K_3: size = 3
            if e.key == K_4: size = 4
            if e.key == K_5: size = 5
            if e.key == K_6: size = 6
            if e.key == K_7: size = 7
            if e.key == K_8: size = 8
            if e.key == K_9: size = 9
            if e.key == K_0: size = 10

        if e.type == MOUSEBUTTONDOWN and not canvas.collidepoint(mpos) and not rects.color_picker_rect.collidepoint(mpos):
            rdraw.text(main_copy, current_color, tx, ty, size, user_text)
            enable_text = False
            user_text = ''

        if e.type == MOUSEBUTTONDOWN and not show_dialog:
            if e.button == 5:
                size -= 1
            if e.button == 4:
                size += 1

        if e.type == MOUSEBUTTONDOWN and not show_dialog and e.button == 1:
            # Tools collidepoint

            if not show_dialog:
                if rects.clear_rect.collidepoint(mpos):
                    main_copy.fill((255, 255, 255))
                    undo_list.append(main_copy.copy())
                    draw_canvas = False
                    click = False
                if rects.save_rect.collidepoint(mpos):
                    save_work()
                    click = False
                if rects.load_image_rect.collidepoint(mpos):
                    load_image()
                    user_blit_count = 1
                    click = False
                if rects.pencil_rect.collidepoint(mpos):
                    current_tool = 'pencil'
                    current_tool_selected = rects.pencil_rect
                    click = False
                if rects.eraser_rect.collidepoint(mpos):
                    current_tool = 'eraser'
                    current_tool_selected = rects.eraser_rect
                    click = False
                if rects.bucket_rect.collidepoint(mpos):
                    current_tool = 'bucket'
                    current_tool_selected = rects.bucket_rect
                    click = False
                if rects.brush_rect.collidepoint(mpos):
                    current_tool = 'brush'
                    current_tool_selected = rects.brush_rect
                    click = False
                if rects.rectangle.collidepoint(mpos) and e.type == MOUSEBUTTONDOWN:
                    show_rect = not show_rect
                elif rects.ellipse.collidepoint(mpos) and e.type == MOUSEBUTTONDOWN:
                    show_ellipse = not show_ellipse
                if rects.line_rect.collidepoint(mpos):
                    current_tool = "line"
                    current_tool_selected = rects.line_rect
                    rect_ellipse_line_count = 1
                    click = False
                if rects.eyedropper_rect.collidepoint(mpos):
                    current_tool = 'eyedropper'
                    current_tool_selected = rects.eyedropper_rect
                    click = False
                if rects.pen_rect.collidepoint(mpos):
                    current_tool = "pen"
                    current_tool_selected = rects.pen_rect
                    click = False
                if rects.text_rect.collidepoint(mpos):
                    current_tool = "text"
                    current_tool_selected = rects.text_rect
                    user_text = ''
                    click = False
                    tx, ty = mx, my
                if rects.spray_paint_rect.collidepoint(mpos):
                    current_tool = "spray_paint"
                    current_tool_selected = rects.spray_paint_rect
                    click = False
                if rects.marker_rect.collidepoint(mpos):
                    current_tool = "marker"
                    current_tool_selected = rects.marker_rect
                    click = False
                if rects.magic_eraser_rect.collidepoint(mpos):
                    current_tool = "magic_eraser"
                    current_tool_selected = rects.magic_eraser_rect
                    click = False
                if rects.undo_rect.collidepoint(mpos):
                    undo()
                if rects.redo_rect.collidepoint(mpos):
                    redo()
        if e.type == MOUSEBUTTONDOWN and e.button == 1:
            click = True

    if len(undo_list) > 20:
        undo_list = undo_list[1:]
    if len(redo_list) > 20:
        redo_list = redo_list[1:]

    if size > 10:
        size -= 1
    elif size < 1:
        size += 1

    main.blit(main_copy, (0, 0))


    if current_tool == "eraser" and canvas.collidepoint(mpos) and not show_dialog:
        draw.circle(main, background_color, (mx, my), size * 6)
        draw.circle(main, (0,0,0), (mx, my), size * 6, 1)

    if current_tool == "brush" and canvas.collidepoint(mpos) and not show_dialog:
        draw.circle(main, (0,0,0), (mx, my), size * 3, 1)
        rdraw.brush(main, current_color, mx, my, ox, oy, size)

    if current_tool == "marker" and canvas.collidepoint(mpos) and not show_dialog:
        draw.circle(main, current_color, (mx, my), size * 2)
        draw.circle(main, (0,0,0), (mx, my), size * 2, 1)

    if enable_text:
        rdraw.text(main, current_color, tx, ty, size, user_text)

    if mb[0] == 1 and canvas.collidepoint(mpos) and not show_dialog:
        if rect_ellipse_line_count == 1 and ('rectangle' in current_tool or 'ellipse' in current_tool or current_tool == "line"):
            rx, ry = mx, my
            rect_ellipse_line_count = 0
        if stamp_count == 1 and "stamp" in current_tool or "droid" in current_tool:
            rx,ry = mx, my
            stamp_count = 0
        draw_tool(current_tool)
        drawing = True
        draw_canvas = True
    elif mb[0] == 0:
        if rect_ellipse_line_count == 0 and ('rectangle' in current_tool or 'ellipse' in current_tool or current_tool == "line"):
            draw_rect_ellipse_line(current_tool)
            rect_ellipse_line_count = 1
        drawing = False

    filled_rects()

    if show_rect:
        draw.rect(main, (221,221,221), rects.rectangle_filled_rect)
        draw.rect(main, (221,221,221), rects.rectangle_unfilled_rect)
        if rects.rectangle_filled_rect.collidepoint(mpos):
            hover(rects.rectangle_filled_rect)
            if mb[0] == 1:
                current_tool = 'rectangle_filled'
                current_tool_selected = rects.rectangle
                rect_ellipse_line_count = 1
                click = False
                show_rect = False

        if rects.rectangle_unfilled_rect.collidepoint(mpos):
            hover(rects.rectangle_unfilled_rect)
            if mb[0] == 1:
                current_tool = 'rectangle_unfilled'
                current_tool_selected = rects.rectangle
                rect_ellipse_line_count = 1
                click = False
                show_rect = False
        main.blit(images.rectangle_filled, (60,309))
        main.blit(images.rectangle_unfilled, (60,365))
        if mb[0] == 1 and not rects.rectangle.collidepoint(mpos) and not rects.rectangle_filled_rect.collidepoint(mpos) and not rects.rectangle_unfilled_rect.collidepoint(mpos):
            show_rect = False
            click = False
    elif show_ellipse:
        draw.rect(main, (221,221,221), rects.ellipse_filled_rect)
        draw.rect(main, (221,221,221), rects.ellipse_unfilled_rect)
        if rects.ellipse_filled_rect.collidepoint(mpos):
            hover(rects.ellipse_filled_rect)
            if mb[0] == 1:
                current_tool = 'ellipse_filled'
                current_tool_selected = rects.ellipse
                rect_ellipse_line_count = 1
                click = False
                show_ellipse = False

        if rects.ellipse_unfilled_rect.collidepoint(mpos):
            hover(rects.ellipse_unfilled_rect)
            if mb[0] == 1:
                current_tool = 'ellipse_unfilled'
                current_tool_selected = rects.ellipse
                rect_ellipse_line_count = 1
                click = False
                show_ellipse = False
        main.blit(images.ellipse_filled, (60,365))
        main.blit(images.ellipse_unfilled, (60,421))
        if mb[0] == 1 and not rects.ellipse.collidepoint(mpos) and not rects.ellipse_filled_rect.collidepoint(mpos) and not rects.ellipse_unfilled_rect.collidepoint(mpos):
            show_ellipse = False
            click = False



    file_name_font = fonts.status_bar_project_name_font.render(file_name, True, (255, 255, 255))
    app_title_font = fonts.app_title_font.render("Paint app", True, (255,255,255))


    main.blit(file_name_font, (4, 4))
    main.blit(app_title_font, (80,40))

    for r in rects_list:
        if r.collidepoint(mpos) and not show_dialog:
            hover(r)
        else:
            hover(current_tool_selected)




    for blit_img in range(len(img)):
        main.blit(img[blit_img], img_location[blit_img])


    draw.circle(main, current_color, (950, 595), 20)
    size_text_color = size_font_text(current_color)
    size_text = fonts.size_text_font.render(str(size), True, size_text_color)
    draw.circle(main, (0, 0, 0), (950, 595), 20, 2)
    if size < 10:
        main.blit(size_text, (945, 584))
    else:
        main.blit(size_text, (940, 584))

    if rects.color_picker_rect.collidepoint(mpos) and mb[0] == 1 and not show_dialog and not drawing:
        current_color = main.get_at(mpos)
        color_pos = mpos
    draw.circle(main, background_color, (color_pos), 3)
    draw.circle(main, (0,0,0), (color_pos), 3, 1)

    if show_dialog:
        if dialog_list[current_dialog] == "save":
            get_click = dialog.create(main, 'Save?', ['Do you want to save your masterpiece?'], 150, 2, "Yes", "No", mpos)
            if get_click and click:
                save_work()
                sys.exit()
            elif get_click == False and click:
                sys.exit()
        elif dialog_list[current_dialog] == "load_fail":
            get_click = dialog.create(main, "Unsupported File", load_fail_text, 200, 1, "OK", None, mpos)
            if get_click and mb[0] == 1:
                show_dialog = False


    if current_tool == "text" and canvas.collidepoint(mpos) and not show_dialog:
        mouse.set_visible(False)
        main.blit(images.mouse_text, (mx-16,my-16))
    elif canvas.collidepoint(mpos) and not show_dialog:
        mouse.set_visible(False)
        if not(current_tool == "eraser") and not(current_tool == "brush") and not(current_tool == "marker"):
            main.blit(images.mouse, (mx-16,my-16))
    else:
        mouse.set_visible(True)

    ox, oy = mx, my

    display.flip()
quit()
