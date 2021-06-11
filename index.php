<?php
foreach (glob("*.zip") as $filename) { 

//echo "$filename\n";
//echo str_replace("","","$filename\n");

echo str_replace("","","<a href='$filename'>$filename</a>\n");

} 
?>