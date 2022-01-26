import wrap,time

x_mario=170
y_mario=40

x_enemy=30
y_enemy=40

speed_mario=2
speed_enemy=1

wrap.world.create_world(200,400,50,50)
wrap.world.set_back_color(120, 82, 255)

mario=wrap.sprite.add("mario-1-small",x_mario,y_mario,"dead")

blue=wrap.sprite.add("mario-enemies",x_enemy,y_enemy,"beetle_blue_dead")

timeset=0
timeset=str(timeset)
while 1==1:
    wrap.sprite.add_text(timeset,100,200, "Arial")
    wrap.sprite.move(0,0,speed_mario)
    wrap.sprite.move(1,0,speed_enemy)
    kym=wrap.sprite.get_bottom(0)
    kye=wrap.sprite.get_bottom(1)
    if kym == 400:
        speed_mario=-2
    if kye == 400:
        speed_enemy=-1
    kym=wrap.sprite.get_top(0)
    kye=wrap.sprite.get_top(1)
    if kym == 0:
        speed_mario=2
    if kye == 0 :
        speed_enemy = 1



