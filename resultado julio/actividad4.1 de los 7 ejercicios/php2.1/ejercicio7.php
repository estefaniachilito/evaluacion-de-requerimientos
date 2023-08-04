<form action ="#" method = "post">
<input type="number" name= "sueldo" placeholder ="Ingrese su sueldo">
<button type ="submit">Enviar</button>    
<form>

<?php


$sueldo = $_POST["sueldo"];

if ($sueldo <= 500000){
    $descuento = ($sueldo*12)/100; 
    $total1 = $sueldo-$descuento;

    echo "Su sueldo Final es: ".$total1;
}
    if ($sueldo > 500000 && $sueldo <= 1000000){ 
        $sueldoFinal2 = ($sueldo*15)/100; 
        $totaldos = $sueldo-$sueldoFinal2;

        echo "Su sueldo Final es: ".$totaldos;
     }
    if ($sueldo > 1000000){
        $sueldoFinal3 = ($sueldo*18)/100; 
        $totaltres = $sueldo-$sueldoFinal3;

        echo "Su sueldo Final es: ".$totaltres;
    }
    
?>