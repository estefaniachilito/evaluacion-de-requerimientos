<form action="#"method="post">
    <input type="number" name="num1">
    <input type="number" name="num2">
    <input type="number" name="num3">
    <button type="submit">Enviar</button>
<form>

<?php
$num1 = $_POST['num1'];
$num2 = $_POST['num2'];
$num3 = $_POST['num3'];

if ($num1 < $num2){
    echo "El número menor es ",$num1;
} elseif ($num1 < $num3){
    echo "El número menor es ",$num2;
}else{
 echo "El número menor es ",$num3;
}
echo "<br>";
if ($num1<$num2 && $num1 == $num3){
    echo "los numeros primero y tercero son el numero: ",$num1;
}
if ($num1<$num3 && $num1 == $num2){
    echo "los numeros primero y segundo son el numero: ",$num1;
}
if ($num3<$num1 && $num3 == $num2){
    echo "los numeros segundo y tercero son el numero: ",$num2;
}

?>