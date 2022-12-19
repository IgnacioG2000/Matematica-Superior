const operacion = document.getElementById('operacion')
const parteReal2 = document.getElementById('parteReal2').value
const parteImaginaria2 = document.getElementById('parteImaginaria2').value

function alertarDivisionPor0(operacion, pr, pi) {
    if(operacion.value === 'division' && pr === 0 && pi === 0) {
        alert("ESTAS DIVIDIENDO POR 0")
    }
}

operacion.addEventListener('select', e=> {
    e.preventDefault()
    console.log(operacion)
    alertarDivisionPor0(this.operacion, parteReal2, parteImaginaria2)
})