import wrap,time

x_mario=170
y_mario=40

x_enemy=30
y_enemy=40

x_star=30
y_star=40

speed_mario=7
speed_enemy=4
xfireballspeed=5

wrap.world.create_world(200,400,50,50)
wrap.world.set_back_color(120, 82, 255)

mario=wrap.sprite.add("mario-1-small",x_mario,y_mario,"dead")

mawriox = wrap.sprite.get_x(mario)
mawrioy = wrap.sprite.get_y(mario)

blue=wrap.sprite.add("mario-enemies",x_enemy,y_enemy,"beetle_blue_dead")

molot =wrap.sprite.add ("mario-enemies", x_enemy, y_enemy, "lava_ball")

timesetstart=time.time()

tecst=wrap.sprite.add_text("-",100,200,"Arial")

timesetstartt = time.time()
while 1==1:
    timesetend=time.time()
    raznica=timesetend-timesetstart
    raznica=int(raznica)
    raznica=str(raznica)
    wrap.sprite_text.set_text(tecst,raznica)

    wrap.sprite.move(0,0,speed_mario)
    wrap.sprite.move(1,0,speed_enemy)

    kym=wrap.sprite.get_bottom(0)
    kye=wrap.sprite.get_bottom(1)

    if kym >= 400:
        speed_mario=-7
    if kye >= 400:
        speed_enemy=-4

    kym=wrap.sprite.get_top(0)
    kye=wrap.sprite.get_top(1)

    if kym <= 0:
        speed_mario=7
    if kye <= 0 :
        speed_enemy = 4

   # wrap.sprite.move(molot,xfireballspeed,xfireballspeed)

    peresichenie=wrap.sprite.is_collide_sprite(molot,mario)

    raznica=int(raznica)

    timesetendd=time.time()
    minus=timesetendd-timesetstartt
    if minus >= 5 :
        mawriox=wrap.sprite.get_x(mario)
        mawrioy=wrap.sprite.get_y(mario)
        enemyx = wrap.sprite.get_x(blue)
        enemyy = wrap.sprite.get_y(blue)
        molot = wrap.sprite.add("mario-enemies", enemyx,enemyy , "lava_ball")
        timesetstartt=time.time()
    wrap.sprite.move_at_angle_point(molot, mawriox, mawrioy, 10)
    if minus >=3:
        if peresichenie == False:
            enemyx = wrap.sprite.get_x(blue)
            enemyy = wrap.sprite.get_y(blue)
            molot = wrap.sprite.add("mario-enemies", enemyx, enemyy, "lava_ball")
            wrap.sprite.remove(molot)

    if peresichenie == True:
        print("hello")
        wrap.sprite.move_to(mario,200,400)
        exit()



