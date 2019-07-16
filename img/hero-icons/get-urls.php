<?php
exec ('wget https://dota2.gamepedia.com/Category:Hero_minimap_icons');
$file = file('Category:Hero_minimap_icons');

foreach ($file as $line){
    if (strpos($line, 'icon.png" src="')){
        exec('wget ' . get_string_between($line, 'src="', '"'));
    }
}

function get_string_between($string, $start, $end){
    $string = ' ' . $string;
    $ini = strpos($string, $start);
    if ($ini == 0) return '';
    $ini += strlen($start);
    $len = strpos($string, $end, $ini) - $ini;
    return substr($string, $ini, $len);
}