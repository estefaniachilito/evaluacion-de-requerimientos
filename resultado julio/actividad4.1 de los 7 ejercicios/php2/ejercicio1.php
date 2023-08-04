<form action="#"method="post">
    <input type="number" name="num1" placeholder="Ingrese un número">
    <input type="number" name="num2" placeholder="Ingrese un número">
    <button type="submit">Enviar</button>
</form>

<?php
$num1 = $_POST ['num1'];
$num2 = $_POST ['num2'];

if ($num1 > $num2) {
    echo "El número mayor es ",$num1;
} elseif ($num1 < $num2) {
    echo "El número mayor es ",$num2;
}

?>