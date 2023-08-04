function calcular() {
    let c1, v1, c2, v2, c3, v3,total
c1=parseInt(document.getElementById(c1).value)
c2=parseInt(document.getElementById(c2).value)
c3=parseInt(document.getElementById(c3).value)


v1=c1*600000
v2=c2*500000
v3=c3*550000
total= (v1+v2+v3);


mensaje=document.getElementById("mensaje");
mensaje.innerHTML= "la cantidad de samsungs es "+c1+ "<br>"+"su precio total es de "+v1+"<br>"
"la cantidad de motorolas es "+c2+ "<br>"+"su precio total es de "+v2+"<br>"
"la cantidad de huawei es "+c3+ "<br>"+"su precio total es de "+v3+"<br>"
"el valor total es de"+total
}