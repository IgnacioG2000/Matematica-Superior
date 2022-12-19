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