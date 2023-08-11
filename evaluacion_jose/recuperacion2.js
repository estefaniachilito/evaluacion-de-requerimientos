// 2. Tomando como base los resultados obtenidos en un laboratorio de análisis clínicos,
// un médico determina si una persona tiene anemia o no, lo cual depende de su nivel
// de hemoglobina en la sangre, de su edad y de su sexo. Si el nivel de hemoglobina que
// tiene una persona es menor que el rango que le corresponde, se determina su
// resultado como positivo y en caso contrario como negativo. La tabla en la que el
// médico se basa para obtener el resultado es la siguiente
function calcular(){
   let edad, genero, nivel, cantidad
   edad=parseFloat(document.getElementById("edad").value)
   genero=document.getElementById("genero").value
   function init(){
 
    let select = document.createElement("select");
 
    let option1 = document.createElement("option");
    option1.setAttribute("value", "femenino");
    let option1Texto = document.createTextNode("femenino");
    option1.appendChild(option1Texto);
 
    let option2 = document.createElement("option");
    option2.setAttribute("value", "masculino");
    let option2Texto = document.createTextNode("masculino");
    option2.appendChild(option2Texto);
 
    select.appendChild(option1);
    select.appendChild(option2);
 
    document.body.appendChild(select);
     
}
 
   nivel=parseFloat(document.getElementById("nivel").value)
   cantidad=parseFloat(document.getElementById("cantidad").value)

   function init(){
 
    let select = document.createElement("select");
 
    let option1 = document.createElement("option");
    option1.setAttribute("value", "mes");
    let option1Texto = document.createTextNode("mes");
    option1.appendChild(option1Texto);
 
    let option2 = document.createElement("option");
    option2.setAttribute("value", "meses");
    let option2Texto = document.createTextNode("meses");
    option2.appendChild(option2Texto);
 
    let option3 = document.createElement("option");
    option3.setAttribute("value", "años");
    let option3Texto = document.createTextNode("años");
    option3.appendChild(option3Texto);
 
    select.appendChild(option1);
    select.appendChild(option2);
    select.appendChild(option3);
 
    document.body.appendChild(select);
     
}

   if (edad >= 0 && edad - 1 &&
    nivel >= 13 && nivel -27 &&
    cantidad=   &&
    genero >= 0.9  &&){
        mensaje =document.getElementById("mensaje");
        mensaje.innerHTML ="el suelo es apto";
}

}