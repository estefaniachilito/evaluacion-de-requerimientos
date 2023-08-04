<form action ="#" method = "post">
<input type="number" name= "hora" placeholder ="Ingrese la hora">
<button type ="submit">Enviar</button>    
<form>

<?php
$hora = $_POST['hora'];
$estaciona = $hora*1500;
 echo "El total es de"." ".$estaciona." y las horas fueron"." ".$hora;
?>