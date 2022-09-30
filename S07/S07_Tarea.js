function dia_a_segundos(dias){
    var horas = dias * 24
    var minutos = horas * 60
    var segundos = minutos * 60
    
    return `a ${horas} horas, ${minutos} minutos, ${segundos} segundos.`
}

var x = parseInt (prompt ("Escribe la cantidad de días a transformar a segundos: "))

document.write(`${x} días equivale ${dia_a_segundos(x)}`)
