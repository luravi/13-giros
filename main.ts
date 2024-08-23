basic.forever(function () {
    // Primera secuencia de movimiento
    maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 50)
    maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CCW, 50)
    basic.pause(1000)
    // Primera parada de los motores
    maqueen.motorStop(maqueen.Motors.All)
    basic.pause(500)
    // Segunda secuencia de movimiento
    maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CCW, 50)
    maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, 50)
    basic.pause(1000)
    // Segunda parada de los motores
    maqueen.motorStop(maqueen.Motors.All)
    basic.pause(500)
})
