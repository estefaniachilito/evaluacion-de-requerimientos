<form action ="#" method = "post">
<input type="number" name= "horas" placeholder ="Ingrese el numero de horas de trabajo semanal">
<button type ="submit">Enviar</button>    
<form>

<?php
$horas = $_POST["horas"];

$extras = ($horas-40);

$total40 = (20*$horas);
$total50 = (20*$horas)+(25*$extras);

if ($horas <= 40){
    echo "Su sueldo semanal es: ", $total40; }
elseif ($horas > 40){
    echo "Su sueldo semanal es: ", $total50; }
?>