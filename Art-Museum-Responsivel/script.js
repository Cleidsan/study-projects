var button = document.getElementById("mobile-button-menu") /* butao abrir */
var fechar = document.getElementById("fechar")
var menu = document.getElementById("mobile-menu")
var header = document.getElementsByTagName("header")[0]

button.addEventListener("click", MostraMenu)
fechar.addEventListener("click", fecharMenu)

function MostraMenu() {
   menu.style.display = "block"
   menu.style.transition = "5s"
   button.style.display = "none"
}
function fecharMenu() {
   menu.style.display = "none"
   button.style.display = "block"
}