
<form action="#" method="post" >

<input type="number" name="num1" placeholder= "primer numero">

<input type="number" name="num2" placeholder= "segundo numero">
<button type= "submit">Enviar</button>
</form>
<?php
$num1= $_POST['num1'];
$num2 =$_POST['num2'];
$opera= $num1+$num2;
$opera1= $num1-$num2;
$opera2= $num1*$num2;
echo "los numeros elegidos son: ". $num1. " y ".$num2. "<br>", "la suma de los numeros es: ". $opera,
"<br>", "la resta de los numeros es: ". $opera1,"<br>", "la multiplicacion de los numeros es: ". $opera2;

?>