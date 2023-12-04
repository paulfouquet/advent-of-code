<?php
$input = file('input');
$sum = 0;
$row = 0;
// [row:position, ...]
$symbols = [];

// Get symbols positions 
foreach($input as $line){
    $line = trim($line);
    for ($position = 0; $position <= strlen($line); $position++) {
        $char = substr($line, $position, 1);
        if(!empty($char) && !ctype_digit($char) && $char != "."){
            array_push($symbols, $row.":".$position);
        }
    }
    $row++;
}

$row = 0;
$currentNumber = "";
$isPart = FALSE;
foreach($input as $line){
    $line = trim($line);
    
    for ($position = 0; $position <= strlen($line); $position++) {
        $char = substr($line, $position, 1);
        if(ctype_digit($char)){
            $currentNumber = $currentNumber.$char;
            $adjacentPos = array($row.":".($position-1), $row.":".($position+1), ($row-1).":".($position-1), ($row-1).":".($position+1), ($row-1).":".$position, ($row+1).":".($position-1), ($row+1).":".($position+1),($row+1).":".$position);
            foreach($adjacentPos as $pos){
                if(in_array($pos, $symbols)){
                    $isPart = TRUE;
                    break;
                }
            }
            
        } else{
            if ($isPart){
                echo $currentNumber." ";
                $sum += $currentNumber;
                $isPart = FALSE;
            }
            $currentNumber = "";
        }
    }
    $row++;
}

echo $sum;
?>