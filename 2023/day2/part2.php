<?php
function getPower(string $gamesList){
    $games = explode("; ", $gamesList);
    $maxCube = ["red" => 0, "green" => 0, "blue" => 0];
    
    foreach($games as $game){
        $cubes = explode(', ', $game);
        $powerGame = 1;
        foreach($cubes as $cube){
            $numberColor = explode(' ', $cube);
            $number = $numberColor[0];
            $color = $numberColor[1];
            if($number > $maxCube[trim($color)]){
                $maxCube[trim($color)] = $number;
            }
        }
    }
    foreach($maxCube as $color => $nb){
        $powerGame = $powerGame * $nb;
    }
    return $powerGame;
}

$input = file('input');
$sum = 0;

foreach($input as $line){
   $splittedLine = explode(': ', str_replace('Game ', '', $line));
   $idGame = $splittedLine[0];
   $sum += getPower($splittedLine[1]);
}

echo $sum;
?>