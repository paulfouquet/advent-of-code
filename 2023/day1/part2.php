<?php
$input = file('input');
$sum = 0;

$digitAsLetters = [
    "one" => 1,
    "two" => 2,
    "three" => 3,
    "four" => 4,
    "five" => 5,
    "six" => 6,
    "seven" => 7,
    "eight" => 8,
    "nine" => 9,
];

foreach($input as $line){
    $firstDigit = NULL;
    $lastDigit = NULL;
    for ($position = 0; $position <= strlen($line); $position++) {
        if(ctype_digit(substr($line, $position, 1))){
            $char = substr($line, $position, 1);
            if(is_null($firstDigit)){
                $firstDigit = $char;
            }
            $lastDigit = $char;
        } else {
            foreach($digitAsLetters as $current => $val) {
                if ($current == substr($line, $position, strlen($current))){
                    if(is_null($firstDigit)){
                        $firstDigit = $val;
                    }
                    $lastDigit = $val;
                    break;
                }
            }
        }
    }
    $sum += $firstDigit.$lastDigit;
}    
echo $sum;
?>