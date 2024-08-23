def on_forever():
    # Primera secuencia de movimiento
    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 50)
    maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CCW, 50)
    basic.pause(1000)
    # Primera parada de los motores
    maqueen.motor_stop(maqueen.Motors.ALL)
    basic.pause(500)
    # Segunda secuencia de movimiento
    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CCW, 50)
    maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 50)
    basic.pause(1000)
    # Segunda parada de los motores
    maqueen.motor_stop(maqueen.Motors.ALL)
    basic.pause(500)
basic.forever(on_forever)
