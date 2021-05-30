@namespace
class SpriteKind:
    NPC = SpriteKind.create()
def Create_player():
    global Playa
    Playa = sprites.create(img("""
            . . . . . . . c c c . . . . . . 
                    . . . . . . c b 5 c . . . . . . 
                    . . . . c c c 5 5 c c c . . . . 
                    . . c c b c 5 5 5 5 c c c c . . 
                    . c b b 5 b 5 5 5 5 b 5 b b c . 
                    . c b 5 5 b b 5 5 b b 5 5 b c . 
                    . . f 5 5 5 b b b b 5 5 5 c . . 
                    . . f f 5 5 5 5 5 5 5 5 f f . . 
                    . . f f f b f e e f b f f f . . 
                    . . f f f 1 f b b f 1 f f f . . 
                    . . . f f b b b b b b f f . . . 
                    . . . e e f e e e e f e e . . . 
                    . . e b c b 5 b b 5 b f b e . . 
                    . . e e f 5 5 5 5 5 5 f e e . . 
                    . . . . c b 5 5 5 5 b c . . . . 
                    . . . . . f f f f f f . . . . .
        """),
        SpriteKind.player)
    Playa.say("Where am I?", 2000)
    tiles.place_on_tile(Playa, tiles.get_tile_location(1, 1))
    controller.move_sprite(Playa, 40, 40)
    scene.camera_follow_sprite(Playa) 

def on_up_pressed():   
    animation.run_image_animation(Playa,
        [img("""
                . . . . . . c c c . . . . . . . 
                        . . . . . . c 5 b c . . . . . . 
                        . . . . c c c 5 5 c c c . . . . 
                        . . c c c c 5 5 5 5 c b c c . . 
                        . c b b 5 b 5 5 5 5 b 5 b b c . 
                        . c b 5 5 b b 5 5 b b 5 5 b c . 
                        . . c 5 5 5 b b b b 5 5 5 f . . 
                        . . f f 5 5 5 5 5 5 5 5 f f . . 
                        . . f f f f f f f f f f f f . . 
                        . . f f f f f f f f f f f f . . 
                        . . . f f f f f f f f f f . . . 
                        . . . e e f f f f f f f e . . . 
                        . . e b f b 5 b b 5 b c b e . . 
                        . . e e f 5 5 5 5 5 5 f e e . . 
                        . . . . c b 5 5 5 5 b c . . . . 
                        . . . . . f f f f f f . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . c c . . . . . . 
                        . . . . . . . c 5 c . . . . . . 
                        . . . . c c c 5 5 c c c . . . . 
                        . . c c b c 5 5 5 5 c c c c . . 
                        . c b b 5 b 5 5 5 5 b 5 b b c . 
                        . c b 5 5 b b 5 5 b b 5 5 b c . 
                        . . f 5 5 5 b b b b 5 5 5 c . . 
                        . . f f 5 5 5 5 5 5 5 5 f f . . 
                        . . f f f f f f f f f f f f . . 
                        . . f f f f f f f f f f f f . . 
                        . . . f f f f f f f f f f . . . 
                        . . . e b e e f f f f b b e . . 
                        . . . e b b e b b 5 5 f e e . . 
                        . . . . c e e 5 5 5 5 5 f . . . 
                        . . . . . f f f f f f f . . . .
            """),
            img("""
                . . . . . . . c c c . . . . . . 
                        . . . . . . c b 5 c . . . . . . 
                        . . . . c c c 5 5 c c c . . . . 
                        . . c c b c 5 5 5 5 c c c c . . 
                        . c b b 5 b 5 5 5 5 b 5 b b c . 
                        . c b 5 5 b b 5 5 b b 5 5 b c . 
                        . . f 5 5 5 b b b b 5 5 5 c . . 
                        . . f f 5 5 5 5 5 5 5 5 f f . . 
                        . . f f f f f f f f f f f f . . 
                        . . f f f f f f f f f f f f . . 
                        . . . f f f f f f f f f f . . . 
                        . . . e e f f f f f f e e . . . 
                        . . e b c b 5 b b 5 b f b e . . 
                        . . e e f 5 5 5 5 5 5 f e e . . 
                        . . . . c b 5 5 5 5 b c . . . . 
                        . . . . . f f f f f f . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . c c . . . . . . . . 
                        . . . . . . c 5 c . . . . . . . 
                        . . . . c c c 5 5 c c c . . . . 
                        . . c c c c 5 5 5 5 c b c c . . 
                        . c b b 5 b 5 5 5 5 b 5 b b c . 
                        . c b 5 5 b b 5 5 b b 5 5 b c . 
                        . . c 5 5 5 b b b b 5 5 5 f . . 
                        . . f f 5 5 5 5 5 5 5 5 f f . . 
                        . . f f f f f f f f f f f f . . 
                        . . f f f f f f f f f f f f . . 
                        . . . f f f f f f f e e f . . . 
                        . . e b b f e e e e e b e . . . 
                        . . e e f 5 5 b b e b b e . . . 
                        . . . f 5 5 5 5 5 e e c . . . . 
                        . . . . f f f f f f f . . . . .
            """)],
        200,
        True)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def StartConversation():
    pass

def on_button_released():
    animation.stop_animation(animation.AnimationTypes.ALL, Playa)
controller.any_button.on_event(ControllerButtonEvent.RELEASED, on_button_released)

def on_left_pressed():
    animation.run_image_animation(Playa,
        [img("""
                . . . . . . . c c . . . . . . . 
                        . . . . . . c 5 c . . . . . . . 
                        . . . . c c 5 5 5 c c c . . . . 
                        . . c c c c 5 5 5 5 c b c c . . 
                        . c b b 5 b 5 5 5 5 b 5 b b c . 
                        . c b 5 5 b b 5 5 b b 5 5 b c . 
                        . . c 5 5 5 b b b b 5 5 5 f . . 
                        . . . f 5 5 5 5 5 5 5 5 f f . . 
                        . . . . f e e e f b e e f f . . 
                        . . . . f e b b f 1 b f f f . . 
                        . . . . f b b b b b b f f . . . 
                        . . . . . f e e e e f e e . . . 
                        . . . . . f 5 b b e b b e . . . 
                        . . . . f 5 5 5 5 e b b e . . . 
                        . . . . c b 5 5 5 5 e e . . . . 
                        . . . . . f f f f f f . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . c c . . . . . . . 
                        . . . . . . c c 5 c . . . . . . 
                        . . . . c c 5 5 5 c c c . . . . 
                        . . c c c c 5 5 5 5 c b c c . . 
                        . c b b 5 b 5 5 5 5 b 5 b b c . 
                        . c b 5 5 b b 5 5 b b 5 5 b c . 
                        . . c 5 5 5 b b b b 5 5 5 f . . 
                        . . . f 5 5 5 5 5 5 5 5 f f . . 
                        . . . . f e e e f b e e f f . . 
                        . . . . f e b b f 1 b f f f . . 
                        . . . . f b b b b e e f f . . . 
                        . . . . . f e e e b b e f . . . 
                        . . . . f 5 b b e b b e . . . . 
                        . . . . c 5 5 5 5 e e f . . . . 
                        . . . . . f f f f f f . . . . .
            """),
            img("""
                . . . . . . . c c . . . . . . . 
                        . . . . . . c 5 c . . . . . . . 
                        . . . . c c 5 5 5 c c c . . . . 
                        . . c c c c 5 5 5 5 c b c c . . 
                        . c b b 5 b 5 5 5 5 b 5 b b c . 
                        . c b 5 5 b b 5 5 b b 5 5 b c . 
                        . . c 5 5 5 b b b b 5 5 5 f . . 
                        . . . f 5 5 5 5 5 5 5 5 f f . . 
                        . . . . f e e e f b e e f f . . 
                        . . . . f e b b f 1 b f f f . . 
                        . . . . f b b b b b b f f . . . 
                        . . . . . f e e e e f e e . . . 
                        . . . . . f 5 b b e b b e . . . 
                        . . . . f 5 5 5 5 e b b e . . . 
                        . . . . c b 5 5 5 5 e e . . . . 
                        . . . . . f f f f f f . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . c c . . . . . . . 
                        . . . . . . c c 5 c . . . . . . 
                        . . . . c c 5 5 5 c c c . . . . 
                        . . c c c c 5 5 5 5 c b c c . . 
                        . c b b 5 b 5 5 5 5 b 5 b b c . 
                        . c b 5 5 b b 5 5 b b 5 5 b c . 
                        . . c 5 5 5 b b b b 5 5 5 f . . 
                        . . . f 5 5 5 5 5 5 5 5 f f . . 
                        . . . . f e e e f b e e f f . . 
                        . . . . f e b b f 1 b f f f . . 
                        . . . . f b b b b b b f f . . . 
                        . . . . . f e e e e e b b e . . 
                        . . . . f 5 5 b b b e b b e . . 
                        . . . . c 5 5 5 5 5 e e e . . . 
                        . . . . . f f f f f f . . . . .
            """)],
        200,
        True)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def Create_Plate():
    global Plate
    Plate = sprites.create(img("""
            ...............bbbbbbbbbbbbbbbbbbb...............
                    ...........bbbbdd111111111111111ddbbbb...........
                    ........bbbd1111111111111111111111111dbbb........
                    ......bbd11111111dddddddddddddd111111111dbb......
                    ....bbd1111111ddd11111111111111dddd1111111dbb....
                    ...bd111111ddd111111111111111111111ddd111111db...
                    ..bd11111ddd111ddddddddddddddddddd111ddd11111db..
                    .bd11111dd111dddd5552555255525552ddd111dd11111db.
                    .b11111d111ddd777772777277727772777ddd111d11111b.
                    bd11111d1ddd1177772777277727777277711ddd1111111db
                    b11111d1ddd116666626662666266626666611ddd1d11111b
                    b11111ddddd116666266626662666266666611ddddd11111b
                    b11111ddddd116662666266626666266666611dddbd11111b
                    b111111dddd116662666266626662666666611dddb111111b
                    bd111111dddd1172777277727772777777711dddbd11111db
                    .b1111111dddd17777777777777777777771dddbd111111b.
                    .bd1111111dbbdd5555555555555555555dddbbd111111db.
                    ..bd11111111dbbdd111111111111111dddbbd1111111db..
                    ...bd111111111dbbbbbbdddddddddddddd111111111db...
                    ....bbd11111111111dbbbbbbbbbddd11111111111dbb....
                    ......bbdd11111111111111111111111111111ddbb......
                    ........bbbdd11111111111111111111111ddbbb........
                    ...........bbbbbddd11111111111dddbbbbb...........
                    ................bbbbbbbbbbbbbbbbb................
        """),
        SpriteKind.food)
    Plate.start_effect(effects.bubbles)
    tiles.place_on_tile(Plate, tiles.get_tile_location(5, 8))
def Create_Dino():
    global Cool_new_Dino
    Cool_new_Dino = sprites.create(img("""
            . . . . c c c c c . . . . . . . 
                    . . c c 5 5 5 5 5 c . . . . . . 
                    . c 5 5 5 5 1 f 5 5 c . . . . . 
                    c 5 5 5 5 5 f f 5 5 5 c . . . . 
                    c 5 5 5 5 5 5 5 5 5 5 5 c . . . 
                    c c b b 1 b 5 5 5 5 5 5 c . . . 
                    c 5 3 3 3 5 5 5 5 5 5 5 d c . . 
                    c 5 3 3 3 5 5 5 5 5 d d d c . . 
                    . c 5 5 5 5 b 5 5 5 d d d c . . 
                    . . c b b c 5 5 b d d d d c . . 
                    . c b b c 5 5 b b d d d d c c c 
                    . c c c c c c d d d d d d d d c 
                    . . . . c c c b 5 5 b d d d c . 
                    . . . . . c d 5 5 b b c c c . . 
                    . . . . c c c c c c c . . . . . 
                    . . . . c b b b c . . . . . . .
        """),
        SpriteKind.NPC)
    tiles.place_on_tile(Cool_new_Dino, tiles.get_tile_location(7, 4))
    animation.run_image_animation(Cool_new_Dino,
        [img("""
                ........................
                        ........................
                        ..........ccc...........
                        .........cccc...........
                        .....ccccccc..ccc.......
                        ...cc555555cccccc.......
                        ..c5555555555bcc........
                        .c555555555555b..cc.....
                        c555551ff555555bccc.....
                        c55d55ff55555555bc......
                        c5555555555555555b......
                        .cbb31bb5555dd555b.cc...
                        .c5333b555ddddd55dccc...
                        .c533b55ddddddddddb.....
                        .c5555dddbb55bdddddccc..
                        ..ccccbbbb555bdddddccc..
                        ...cdcbc5555bddddddcc...
                        ....ccbc55bc5ddddddbcccc
                        .....cbbcc5555dddddddddc
                        .....ccbbb555ddbddddddc.
                        .....cdcbc55ddbbbdddcc..
                        ...ccdddccddddbcbbcc....
                        ...ccccccd555ddccc......
                        ........cccccccc........
            """),
            img("""
                ............ccc.........
                        .......cccccccc.........
                        .....cc55555cc..cc......
                        ....c555555555cccc......
                        ...c55555555555bcc......
                        ..c555551ff55555b..cc...
                        ..c55d55ff5555555bccc...
                        ..c55555555d55555bcc....
                        ..c5555d5555d55555b.....
                        ..cbbbb55555ddd555b.cc..
                        ..c555d5555ddddd55dccc..
                        ...c555dbbbdddbd5ddcc...
                        ....cccbbbbb555bdddb....
                        ....cbbbbbbc555bdddccc..
                        ...cbbbbbbc555bddddcc...
                        ...cbbbbbc555bdddddc....
                        ..ccbbbbbc55bddddddcc...
                        ..ccbbbbbbcb55dddddbcc..
                        ...cbbbbbb5555ddddddddcc
                        ....cbbbbb555ddbdddddddc
                        ....cccbbc55ddbbbddddcc.
                        ...ccdddccddddbcbbccc...
                        ...ccccccd555ddccc......
                        ........cccccccc........
            """),
            img("""
                .............ccc........
                        ........cccccccc........
                        ......cc55555cc..cc.....
                        .....c555555555cccc.....
                        ....c55555555555bcc.....
                        ...c555555ccb5555b.cc...
                        ...c55d55c55555555bcc...
                        ...c55555555dd5555bc....
                        ...c5555d5555dd5555.....
                        ...cbbbd555555dd555.cc..
                        ...c555d555555ddd55ccc..
                        ....c555d5555ddbd5dcc...
                        ....cccbbbbb555bdddb....
                        ...cbbbbbbbc555bdddccc..
                        ..cbbbbbbbc555bddddcc...
                        ..cbbbbbbc555bdddddc....
                        .ccbbbbbbc55bddddddcc...
                        .ccbbbbbbbcb55dddddbc...
                        ..cbbbbbbb5555ddddddbc..
                        ...cbbbbbb555ddbddddddc.
                        ....cccbbc55ddbbbddddddc
                        ...ccdddccddddbcbbcccccc
                        ...ccccccd555ddccc......
                        ........cccccccc........
            """),
            img("""
                ........................
                        ........................
                        ........................
                        ..........ccc...........
                        .........cccc...........
                        .....ccccccc..ccc.......
                        ...cc555555cccccc.......
                        ..c5555555555bcc........
                        .c555555555555b..cc.....
                        c555555ccb55555bccc.....
                        c55d55c555555555bc......
                        c5555555555555555b......
                        .cbbb1bb5555dd555b.cc...
                        .c533bbbb5ddddd55dcc....
                        .c533bbbb5ddddddddbcc...
                        .c533bbb55dddddddddcccc.
                        .c5333bb5bb55bdddddcccdc
                        .c5333b5bb555bddddddbddc
                        .c53335b5555bddddddddddc
                        ..c5555c55bb55dbddddddcc
                        ...cccbccc55ddbbbddddcc.
                        ....cdddccddddbcbbbcc...
                        ....cccccd555ddcccc.....
                        ........cccccccc........
            """),
            img("""
                ........................
                        ........................
                        ........................
                        ..........ccc...........
                        .........cccc...........
                        .....ccccccc..ccc.......
                        ...cc555555cccccc.......
                        ..c5555555555bcc........
                        .c555555555555b..cc.....
                        c555555ccb55555bccc.....
                        c55d55c555555555bc......
                        c5555555555555555b......
                        .cbbb1bb5555dd555b.cc...
                        .c533bbbb5ddddd55dcc....
                        .c533bbbb5ddddddddbcc...
                        .c5333bb55dddddddddcccc.
                        .c5333b55bb55bdddddcccdc
                        .c533355bb555bddddddbddc
                        ..c5555b5555bddddddddddc
                        ...cccbc55bb55dbddddddcc
                        .....cbbcc55ddbbbddddcc.
                        ....cdddccddddbcbbbcc...
                        ....cccccd555ddcccc.....
                        ........cccccccc........
            """),
            img("""
                ........................
                        ........................
                        ........................
                        ..........ccc...........
                        .........cccc...........
                        .....ccccccc..ccc.......
                        ...cc555555cccccc.......
                        ..c5555555555bcc........
                        .c555555555555b..cc.....
                        c555555ccb55555bccc.....
                        c55d55c555555555bc......
                        c5555555555555555b......
                        .cbbb1bb5555dd555b.cc...
                        .c533bbb55ddddd55dcc....
                        .c5333bb5dddddddddbcc...
                        .c5333b55ddddddddddcccc.
                        .c533355dbb55bdddddcccdc
                        ..c55555bb555bddddddbddc
                        ...cccbb5555bddddddddddc
                        .....cbc55bb55dbddddddcc
                        .....cdbcc55ddbbbddddcc.
                        ....cdddccddddbcbbbcc...
                        ....cccccd555ddcccc.....
                        ........cccccccc........
            """)],
        200,
        True)

def on_right_pressed():
    animation.run_image_animation(Playa,
        [img("""
                . . . . . . . c c . . . . . . . 
                        . . . . . . . c 5 c . . . . . . 
                        . . . . c c c 5 5 5 c c . . . . 
                        . . c c b c 5 5 5 5 c c c c . . 
                        . c b b 5 b 5 5 5 5 b 5 b b c . 
                        . c b 5 5 b b 5 5 b b 5 5 b c . 
                        . . f 5 5 5 b b b b 5 5 5 c . . 
                        . . f f 5 5 5 5 5 5 5 5 f . . . 
                        . . f f e e b f e e e f . . . . 
                        . . f f f b 1 f b b e f . . . . 
                        . . . f f b b b b b b f . . . . 
                        . . . e e f e e e e f . . . . . 
                        . . . e b b e b b 5 f . . . . . 
                        . . . e b b e 5 5 5 5 f . . . . 
                        . . . . e e 5 5 5 5 b c . . . . 
                        . . . . . f f f f f f . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . c c . . . . . . . 
                        . . . . . . c 5 c c . . . . . . 
                        . . . . c c c 5 5 5 c c . . . . 
                        . . c c b c 5 5 5 5 c c c c . . 
                        . c b b 5 b 5 5 5 5 b 5 b b c . 
                        . c b 5 5 b b 5 5 b b 5 5 b c . 
                        . . f 5 5 5 b b b b 5 5 5 c . . 
                        . . f f 5 5 5 5 5 5 5 5 f . . . 
                        . . f f e e b f e e e f . . . . 
                        . . f f f b 1 f b b e f . . . . 
                        . . . f f e e b b b b f . . . . 
                        . . . f e b b e e e f . . . . . 
                        . . . . e b b e b b 5 f . . . . 
                        . . . . f e e 5 5 5 5 c . . . . 
                        . . . . . f f f f f f . . . . .
            """),
            img("""
                . . . . . . . c c . . . . . . . 
                        . . . . . . . c 5 c . . . . . . 
                        . . . . c c c 5 5 5 c c . . . . 
                        . . c c b c 5 5 5 5 c c c c . . 
                        . c b b 5 b 5 5 5 5 b 5 b b c . 
                        . c b 5 5 b b 5 5 b b 5 5 b c . 
                        . . f 5 5 5 b b b b 5 5 5 c . . 
                        . . f f 5 5 5 5 5 5 5 5 f . . . 
                        . . f f e e b f e e e f . . . . 
                        . . f f f b 1 f b b e f . . . . 
                        . . . f f b b b b b b f . . . . 
                        . . . e e f e e e e f . . . . . 
                        . . . e b b e b b 5 f . . . . . 
                        . . . e b b e 5 5 5 5 f . . . . 
                        . . . . e e 5 5 5 5 b c . . . . 
                        . . . . . f f f f f f . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . c c . . . . . . . 
                        . . . . . . c 5 c c . . . . . . 
                        . . . . c c c 5 5 5 c c . . . . 
                        . . c c b c 5 5 5 5 c c c c . . 
                        . c b b 5 b 5 5 5 5 b 5 b b c . 
                        . c b 5 5 b b 5 5 b b 5 5 b c . 
                        . . f 5 5 5 b b b b 5 5 5 c . . 
                        . . f f 5 5 5 5 5 5 5 5 f . . . 
                        . . f f e e b f e e e f . . . . 
                        . . f f f b 1 f b b e f . . . . 
                        . . . f f b b b b b b f . . . . 
                        . . e b b e e e e e f . . . . . 
                        . . e b b e b b b 5 5 f . . . . 
                        . . . e e e 5 5 5 5 5 c . . . . 
                        . . . . . f f f f f f . . . . .
            """)],
        200,
        True)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_down_pressed():
    animation.run_image_animation(Playa,
        [img("""
                . . . . . . . c c c . . . . . . 
                        . . . . . . c b 5 c . . . . . . 
                        . . . . c c c 5 5 c c c . . . . 
                        . . c c b c 5 5 5 5 c c c c . . 
                        . c b b 5 b 5 5 5 5 b 5 b b c . 
                        . c b 5 5 b b 5 5 b b 5 5 b c . 
                        . . f 5 5 5 b b b b 5 5 5 c . . 
                        . . f f 5 5 5 5 5 5 5 5 f f . . 
                        . . f f f b f e e f b f f f . . 
                        . . f f f 1 f b b f 1 f f f . . 
                        . . . f f b b b b b b f f . . . 
                        . . . e e f e e e e f e e . . . 
                        . . e b c b 5 b b 5 b f b e . . 
                        . . e e f 5 5 5 5 5 5 f e e . . 
                        . . . . c b 5 5 5 5 b c . . . . 
                        . . . . . f f f f f f . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . c c . . . . . . . . 
                        . . . . . . c 5 c . . . . . . . 
                        . . . . c c c 5 5 c c c . . . . 
                        . . c c c c 5 5 5 5 c b c c . . 
                        . c b b 5 b 5 5 5 5 b 5 b b c . 
                        . c b 5 5 b b 5 5 b b 5 5 b c . 
                        . . c 5 5 5 b b b b 5 5 5 f . . 
                        . . f f 5 5 5 5 5 5 5 5 f f . . 
                        . . f f f b f e e f b f f f . . 
                        . . f f f 1 f b b f 1 f f f . . 
                        . . . f f b b b b e e e f . . . 
                        . . e b b f e e e e b b e . . . 
                        . . e e f 5 5 b b e b b e . . . 
                        . . . f 5 5 5 5 5 e e c . . . . 
                        . . . . f f f f f f f . . . . .
            """),
            img("""
                . . . . . . c c c . . . . . . . 
                        . . . . . . c 5 b c . . . . . . 
                        . . . . c c c 5 5 c c c . . . . 
                        . . c c c c 5 5 5 5 c b c c . . 
                        . c b b 5 b 5 5 5 5 b 5 b b c . 
                        . c b 5 5 b b 5 5 b b 5 5 b c . 
                        . . c 5 5 5 b b b b 5 5 5 f . . 
                        . . f f 5 5 5 5 5 5 5 5 f f . . 
                        . . f f f b f e e f b f f f . . 
                        . . f f f 1 f b b f 1 f f f . . 
                        . . . f f b b b b b b f f . . . 
                        . . . e e f e e e e f e e . . . 
                        . . e b f b 5 b b 5 b c b e . . 
                        . . e e f 5 5 5 5 5 5 f e e . . 
                        . . . . c b 5 5 5 5 b c . . . . 
                        . . . . . f f f f f f . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . c c . . . . . . 
                        . . . . . . . c 5 c . . . . . . 
                        . . . . c c c 5 5 c c c . . . . 
                        . . c c b c 5 5 5 5 c c c c . . 
                        . c b b 5 b 5 5 5 5 b 5 b b c . 
                        . c b 5 5 b b 5 5 b b 5 5 b c . 
                        . . f 5 5 5 b b b b 5 5 5 c . . 
                        . . f f 5 5 5 5 5 5 5 5 f f . . 
                        . . f f f b f e e f b f f f . . 
                        . . f f f 1 f b b f 1 f f f . . 
                        . . . f e e e b b b b f f . . . 
                        . . . e b b e e e e f b b e . . 
                        . . . e b b e b b 5 5 f e e . . 
                        . . . . c e e 5 5 5 5 5 f . . . 
                        . . . . . f f f f f f f . . . .
            """)],
        200,
        True)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

Cool_new_Dino: Sprite = None
Plate: Sprite = None
Playa: Sprite = None
StartConversation()
tiles.set_tilemap(tilemap("""
    level1
"""))
music.spooky.play()
scene.camera_shake(6, 1000)
Bed = sprites.create(img("""
        ...bbccccccbb...
            ..bdddddddd1db..
            .bddbbbbbbbbddb.
            .cdb11111111bdc.
            .cbcdbbbbbbdcbc.
            .fbcc111111ccbf.
            .fbcd111111dcbf.
            f66cdd1111ddc66f
            f66ccbbbbbbcc66f
            fcbb33333333bbcf
            fbb3333333333bbf
            fbb3d111111d3bbf
            fbd1111111111dbf
            fdd1111111111ddf
            fdd1111111111ddf
            fdd1111111111ddf
            fdd1111111111ddf
            fdd11dbbbbd11ddf
            cdbbddddddddbbdf
            cbddddddddddddbc
            cddddddddddddddc
            .cccccccccccccc.
            .fbbfbbbbbbfbbf.
            ..ff........ff..
    """),
    SpriteKind.player)
tiles.place_on_tile(Bed, tiles.get_tile_location(1, 1))
Create_player()
Create_Dino()
Create_Plate()