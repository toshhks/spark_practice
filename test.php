<?php
//1
$str = "Hello";

echo "Исходная строка: $str\n";
echo "Третий символ: " . $str[2] . "\n";

$str[strlen($str) - 1] = "!";
echo "Изменённая строка: $str\n\n";

//2
$first = "PHP";
$second = "php";

echo "Строка 1: $first\n";
echo "Строка 2: $second\n";

if (strcasecmp($first, $second) === 0) {
    echo "Строки равны без учёта регистра\n\n";
} else {
    echo "Строки различаются\n\n";
}

// Задание 3.
$sentence = "Сегодня прекрасный день!";

echo "Задание 3\n";
echo "Исходная строка: $sentence\n";

$word = substr($sentence, 15, 20);
echo "Подстрока: $word\n";

$newSentence = substr($sentence, 0, 15) . "обычный" . substr($sentence, 35);
echo "Новая строка: $newSentence\n";
