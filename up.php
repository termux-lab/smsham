<?php
$smsham = file_get_contents("https://raw.githubusercontent.com/termux-lab/smsham/master/smsham.py");
$file = fopen("smsham.py", "w");
fwrite($file, $smsham);
fclose($file);
$smshams = file_get_contents("https://raw.githubusercontent.com/termux-lab/smsham/master/smsham2.py");
$files = fopen("smsham2.py", "w");
fwrite($files, $smshams);
fclose($files);
?>
