/*
const operacion = document.getElementById('operacion')

function alertarDivisionPor0(operacion) {
    const pr = document.getElementById('parteReal2').value
    const pi = document.getElementById('parteImaginaria2').value
    console.log(pr)
    console.log(pi)
    if(operacion === 'division' && pr === 0 && pi === 0) {
        alert("ESTAS DIVIDIENDO POR 0")
    }
}

operacion.addEventListener('click', e=> {
    e.preventDefault()
    console.log(operacion)
    alertarDivisionPor0(this.operacion.value)
})

*/

const botonMostrarIntegral = document.getElementById('botonMostrarIntegral')
const botonMostrarResultadoIntegral = document.getElementById('botonEvaluarIntegral')
const integralDiv = document.getElementById('mostrarIntegral')
const resultadoDiv = document.getElementById('mostrarResultado')

function mostrarIntegral(integral) {
    integral.style.display = 'block'
}

botonMostrarIntegral.addEventListener('select', e => {
    e.preventDefault()
    mostrarIntegral(integralDiv)
})

function mostrarResultadoIntegral(resultado) {
    resultado.style.display = 'block'
}

botonMostrarResultadoIntegral.addEventListener('select', e => {
    e.preventDefault()
    mostrarResultadoIntegral(resultadoDiv)
})