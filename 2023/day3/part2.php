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
        if($char == "*"){
            array_push($symbols, $row.":".$position);
        }
    }
    $row++;
}

$row = 0;
$currentNumber = "";
$isPart = FALSE;
$parts = [];
foreach($input as $line){
    $line = trim($line);
    $stars = [];
    for ($position = 0; $position <= strlen($line); $position++) {
        $char = substr($line, $position, 1);
        if(ctype_digit($char)){
            $currentNumber = $currentNumber.$char;
            $adjacentPos = array($row.":".($position-1), $row.":".($position+1), ($row-1).":".($position-1), ($row-1).":".($position+1), ($row-1).":".$position, ($row+1).":".($position-1), ($row+1).":".($position+1),($row+1).":".$position);

            foreach($adjacentPos as $pos){
                if(in_array($pos, $symbols)){
                    $isPart = TRUE;
                    if(!in_array($pos, $stars)){
                        array_push($stars, $pos);
                    } 
                }
            }
            
        } else{
            if ($isPart){
                foreach($stars as $star){
                    if(empty($parts[$star])){
                        $parts[$star] = [];
                    }
                    array_push($parts[$star], $currentNumber);
                }
                $stars = [];
                $isPart = FALSE;
            }
            $currentNumber = "";
        }
    }
    $row++;
}
foreach($parts as $part => $val){
    if(count($val) == 2){
        $multiply = 1;
        foreach($val as $number){
            $multiply = $multiply * $number;
        }
        $sum += $multiply;
    }
}
echo $sum;
?>