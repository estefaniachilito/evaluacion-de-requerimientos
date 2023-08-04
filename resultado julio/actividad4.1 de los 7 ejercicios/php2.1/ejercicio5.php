<form action ="#" method = "post">
    <select name="turno">
        <option value="nocturno">nocturno</option>
        <option value="diurno">diurno</option>
    </select>
<input type="number" name= "horas" placeholder ="Ingrese las horas">
<button type ="submit">Enviar</button>    
<form>

<?php
$turno= $_POST["turno"];
$horas= $_POST["horas"];
if($turno == "diurno"){
 $total = $horas*10;
 echo "<br>";
 echo "el total de dolares son: ". $total;
}
if($turno == "nocturno"){
    $total = $horas*15;
    echo "<br>";
    echo "el total de dolares son: ". $total;
   }
?>