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

function noSonNulos(tipoFuncion1, tipoFuncion2) {
    return tipoFuncion1 != null && tipoFuncion2 != null;
}

function mostrar() {
    let tipoFuncion1 = document.getElementById('tipoFuncion1').value
    console.log(tipoFuncion1)
    let tipoFuncion2 = document.getElementById('tipoFuncion2').value
    console.log(tipoFuncion2)

    if (tipoFuncion1 !== tipoFuncion2 && noSonNulos(tipoFuncion1, tipoFuncion2)) {
        document.getElementById('mostrarResultado').style.display = 'block'
    }
}

operacion.addEventListener('click', e=> {
    e.preventDefault()
    console.log(operacion)
    alertarDivisionPor0(this.operacion.value)
})

