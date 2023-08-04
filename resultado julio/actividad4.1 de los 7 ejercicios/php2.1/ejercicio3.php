<form action="#"method="post">
    <span> Ingrese su nota: </span> 
    <input type="number" name="nota">
    <button type="submit">Enviar</button>
<form>

<?php
$nota = $_POST['nota'];

if($nota >= 7){
    echo "<br>";
    echo "Aprobo";
} if($nota <7){
    echo "<br>";
    echo "No aprobo";
}
?>