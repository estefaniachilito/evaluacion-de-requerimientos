function submit() {
    let seg, di, hr, minu
    seg = (document.getElementById("seg").value)
    di = seg/60/60/24
    hr =seg/60/60
    minu = seg/60

    res = document.getElementById("hola")
    res.innerHTML = "la cantidad de dias son: "+ di +"<br> horas: "+ hr +"<br> minutos: "+ minu + "<br> segundos " + seg
}