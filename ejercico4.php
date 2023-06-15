
<form action="#" method="post" >

<input type="text" name="nombre" placeholder= "digite su nombre">

<input type="number" name="sueldo" placeholder= "digite su sueldo base">
<button type= "submit">Enviar</button>
</form>
<?php
$nombre= $_POST['nombre'];
$sueldo =$_POST['sueldo'];
$opera= $sueldo * 0.15 + $sueldo;


echo $nombre. " el valor a pagar es: ". $opera;