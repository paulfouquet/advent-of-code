<?php
function isPossible(string $gamesList){
    $nbCubes = ["red" => 12, "green" => 13, "blue" => 14];
    $games = explode("; ", $gamesList);
    foreach($games as $game){
        $cubes = explode(', ', $game);
        foreach($cubes as $cube){
            $numberColor = explode(' ', $cube);
            $number = $numberColor[0];
            $color = $numberColor[1];
            if($number > $nbCubes[trim($color)]){
                return FALSE;
            }
        }
    }
    return TRUE;
}

$input = file('input');
$sum = 0;

foreach($input as $line){
   $splittedLine = explode(': ', str_replace('Game ', '', $line));
   $idGame = $splittedLine[0];
   
   if(isPossible($splittedLine[1])){
    $sum += $idGame;
   }
}

echo $sum;
?>