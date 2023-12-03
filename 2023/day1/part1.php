<?php
$input = file('input');
$sum = 0;
foreach($input as $line){
    echo ' ';;
    $firstDigit = NULL;
    $lastDigit = NULL;
    foreach (str_split($line) as $char) {
        if(ctype_digit($char)){
            if(is_null($firstDigit)){
                $firstDigit = $char;
            }
            $lastDigit = $char;
        }
    }
    $sum += $firstDigit.$lastDigit;
}
echo $sum;
?>