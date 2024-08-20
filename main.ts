// Pausa 0.5 segundos
// Ejecutar el ciclo indefinidamente
basic.forever(function () {
    // Giro a la izquierda
    maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 50)
    // Motor izquierdo adelante
    maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CCW, 50)
    // Motor derecho atrás
    basic.pause(1000)
    // Pausa 1 segundo
    maqueen.motorStop(maqueen.Motors.All)
    // Detener ambos motores
    basic.pause(500)
    // Pausa 0.5 segundos
    // Giro a la derecha
    maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CCW, 50)
    // Motor izquierdo atrás
    maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, 50)
    // Motor derecho adelante
    basic.pause(1000)
    // Pausa 1 segundo
    maqueen.motorStop(maqueen.Motors.All)
    // Detener ambos motores
    basic.pause(500)
})
