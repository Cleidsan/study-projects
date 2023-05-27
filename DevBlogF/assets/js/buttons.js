var descr1 = document.getElementById("descr1")
var x1 = document.getElementById("X1")
var descr2 = document.getElementById("descr2")
var x2 = document.getElementById("X2")
var descr3 = document.getElementById("descr3")
var x3 = document.getElementById("X3")
var mostraDescr1 = document.getElementById("mostra-descr1")
var mostraDescr2 = document.getElementById("mostra-descr2")
var mostraDescr3 = document.getElementById("mostra-descr3")

descr1.addEventListener("click", abrir1)
descr2.addEventListener("click", abrir2)
descr3.addEventListener("click", abrir3)
x1.addEventListener("click", fechar1)
x2.addEventListener("click", fechar2)
x3.addEventListener("click", fechar3)

function abrir1() {
    mostraDescr1.style.display = "block"
    mostraDescr2.style.display = "none"
    mostraDescr3.style.display = "none"
}

function abrir2() {
    mostraDescr2.style.display = "block"
    mostraDescr1.style.display = "none"
    mostraDescr3.style.display = "none"
}

function abrir3() {
    mostraDescr3.style.display = "block"
    mostraDescr1.style.display = "none"
    mostraDescr2.style.display = "none"
}
function fechar1() {
    mostraDescr1.style.display = "none"
}

function fechar2() {
    mostraDescr2.style.display = "none"
}

function fechar3() {
    mostraDescr3.style.display = "none"
}
