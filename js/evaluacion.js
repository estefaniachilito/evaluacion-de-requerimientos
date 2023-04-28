function Porcentaje(){
    let n1, quince, n2
    //guardando datos de HTML de la respectiva variable
    n1= document.getElementById("numero1").value
    n2= document.getElementById("numero2").value

   respuesta=n1*n2
   quince=n1*n2 *15/100
   totalfinal= respuesta-quince

    //enviar al html
    document.getElementById("respuesta").innerHTML="<div>"+totalfinal+"</div>"
}
function porcentajE(){
let n1, cincuenta, n2

//guardando datos de HTML de la respectiva variable
 n1= document.getElementById("numero1").value
    n2= document.getElementById("numero2").value
cincuenta= n1*n2 *50/100

//enviar al html
document.getElementById("Respuesta").innerHTML="<div>"+cincuenta+"</div>"
}
function PorcentajE(){
    let n1, sin , n2
    
    //guardando datos de HTML de la respectiva variable
     n1= document.getElementById("numero1").value
        n2= document.getElementById("numero2").value
    sin= n1*n2 
    
    //enviar al html
    document.getElementById("RespuestA").innerHTML="<div>"+sin+"</div>"
    }
