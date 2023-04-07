function noEstanDefinidos(tipoFuncion1, tipoFuncion2) {
    return tipoFuncion1 !== null && tipoFuncion2 !== null;
}

const tipoFuncion1 = document.getElementById('tipoFuncion1')
const tipoFuncion2 = document.getElementById('tipoFuncion2')

tipoFuncion1.addEventListener('change', e => {
    e.preventDefault();
    mostrarTipoFuncionSegunRespuesta(tipoFuncion1.value, tipoFuncion2.value)
})

tipoFuncion2.addEventListener('change', e => {
    e.preventDefault();
    mostrarTipoFuncionSegunRespuesta(tipoFuncion1.value, tipoFuncion2.value)
})

function mostrarTipoFuncionSegunRespuesta(tipoFuncion1, tipoFuncion2) {

    if (tipoFuncion1 !== tipoFuncion2 && noEstanDefinidos(tipoFuncion1, tipoFuncion2)) {
        document.getElementById('mostrarResultado').style.display = 'block'
    }
    else {
        document.getElementById('mostrarResultado').style.display = 'none'
    }
}