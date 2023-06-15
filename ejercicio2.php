
<form action="#" method="post" >

<input type="number" name="num1" placeholder= "primer numero">

<input type="number" name="num2" placeholder= "segundo numero">
<button type= "submit">Enviar</button>
</form>
<?php
$num1= $_POST['num1'];
$num2 =$_POST['num2'];
$opera= $num1+$num2;
echo"la suma de los dos numeros es: ". $opera;

?>