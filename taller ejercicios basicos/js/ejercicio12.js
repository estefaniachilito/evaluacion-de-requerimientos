function validar(){
    let usuario, clave
    usuario = document.getElementById("usuario").value
    clave = document.getElementById("password").value
    if (usuario == 'fund@gmail.com' && clave == '123456'){
        alert("bienvenidos a fundamentos de programacion")
    }else {
        alert("error en los datos de ingreso")
    }
}