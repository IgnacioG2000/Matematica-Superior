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
const orden = document.getElementById('ordenEcuacion')

function mostrarOrdenEcuacionSegunOpcion(ordenEc) {
    if(ordenEc === '3') {
        document.getElementById('mostrarResultadoEcDiferencialOrden3').style.display = 'block'
        document.getElementById('mostrarValoresInicialesEcDiferencialOrden3').style.display = 'block'
        document.getElementById('mostrarResultadoEcDiferencialOrden2').style.display = 'block'
        document.getElementById('mostrarValoresInicialesEcDiferencialOrden2').style.display = 'block'
        document.getElementById('mostrarResultadoEcDiferencialOrden1').style.display = 'block'
        document.getElementById('mostrarValoresInicialesEcDiferencialOrden1').style.display = 'block'
        document.getElementById('mostrarFuncionYTerminoIndependiente').style.display = 'block'
    }
    else {
        if(ordenEc === '2') {
            document.getElementById('mostrarResultadoEcDiferencialOrden3').style.display = 'none'
            document.getElementById('mostrarValoresInicialesEcDiferencialOrden3').style.display = 'none'
            document.getElementById('mostrarResultadoEcDiferencialOrden2').style.display = 'block'
            document.getElementById('mostrarValoresInicialesEcDiferencialOrden2').style.display = 'block'
            document.getElementById('mostrarResultadoEcDiferencialOrden1').style.display = 'block'
            document.getElementById('mostrarValoresInicialesEcDiferencialOrden1').style.display = 'block'
            document.getElementById('mostrarFuncionYTerminoIndependiente').style.display = 'block'
        }
        else {
            if(ordenEc === '1') {
                document.getElementById('mostrarResultadoEcDiferencialOrden1').style.display = 'block'
                document.getElementById('mostrarValoresInicialesEcDiferencialOrden1').style.display = 'block'
                document.getElementById('mostrarFuncionYTerminoIndependiente').style.display = 'block'
                document.getElementById('mostrarResultadoEcDiferencialOrden2').style.display = 'none'
                document.getElementById('mostrarValoresInicialesEcDiferencialOrden2').style.display = 'none'
                document.getElementById('mostrarResultadoEcDiferencialOrden3').style.display = 'none'
                document.getElementById('mostrarValoresInicialesEcDiferencialOrden3').style.display = 'none'
            }
        }
    }

}

orden.addEventListener('change', e => {
    e.preventDefault();
    mostrarOrdenEcuacionSegunOpcion(orden.value)
})