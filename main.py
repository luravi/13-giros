def on_forever():
    # Giro a la izquierda
    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 50)  # Motor izquierdo adelante
    maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CCW, 50) # Motor derecho atrás
    basic.pause(1000)  # Pausa 1 segundo
    maqueen.motor_stop(maqueen.Motors.ALL)  # Detener ambos motores
    basic.pause(500)  # Pausa 0.5 segundos

    # Giro a la derecha
    maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CCW, 50) # Motor izquierdo atrás
    maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 50)  # Motor derecho adelante
    basic.pause(1000)  # Pausa 1 segundo
    maqueen.motor_stop(maqueen.Motors.ALL)  # Detener ambos motores
    basic.pause(500)  # Pausa 0.5 segundos

# Ejecutar el ciclo indefinidamente
basic.forever(on_forever)
