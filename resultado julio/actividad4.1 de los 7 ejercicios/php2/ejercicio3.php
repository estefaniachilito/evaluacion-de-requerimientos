

<?php
$n1 = floatval(readline(prompt:"primer numero \n"));

if($n1 == 0){
    echo "la nota escrita no existe";
}
if($n1 >= 11){
    echo "la nota sobrepasa la deseada";
}
if($n1 > 7 && $n1 <= 10){
    echo "usted APROBO";
}

if($n1 < 7 && $n1 >= 1){
    echo "usted NO APROBO";
}
?>

<form action="#"method="post">
    <span> Ingrese su nota: </span> 
    <input type="number" name="nota">
    <button type="submit">Enviar</button>
<form>

<?php
$nota = $_POST['nota'];

if($nota >= 7 && $nota <=10){
    echo "<br>";
    echo "Aprobo";
} if($nota <7 && $nota >1){
    echo "<br>";
    echo "No aprobo";
}
if ($nota <= 1){
    echo "El número esta fuera de rango ",$nota;
   }
?>