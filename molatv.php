<?php 
date_default_timezone_set("Asia/Jakarta");

$url=$_GET['id'];

if ($url == "690") {
	echo "#EXTM3U";
  echo '<br>';
  echo '<br>';
  echo "#EXT-X-VERSION:3"; 
  echo '<br>';
  echo '<br>';
  echo "#EXT-X-STREAM-INF:PROGRAM-ID=1,CLOSED-CAPTIONS=NONE,BANDWIDTH=1500000,NAME=720p,RESOLUTION=1280x720";
  echo '<br>';
  echo "https://etslive-2-vidio-com.akamaized.net/exp=1622814649~acl=/hls-p/ingest_6840_*/*~hmac=edaa841eefaab544841b9f7be7d7dd08f8d34ea2ba588784b2ca71caf41c51e4/hls-p/ingest_6840_720p/index.m3u8";
  echo '<br>';
  echo '<br>';
  echo "#EXT-X-STREAM-INF:PROGRAM-ID=1,CLOSED-CAPTIONS=NONE,BANDWIDTH=1200000,NAME=480p,RESOLUTION=854x480";
  echo '<br>';
  echo "https://etslive-2-vidio-com.akamaized.net/exp=1622814649~acl=/hls-p/ingest_6840_*/*~hmac=edaa841eefaab544841b9f7be7d7dd08f8d34ea2ba588784b2ca71caf41c51e4/hls-p/ingest_6840_480p/index.m3u8";
  echo '<br>';
  echo '<br>';
  echo "#EXT-X-STREAM-INF:PROGRAM-ID=1,CLOSED-CAPTIONS=NONE,BANDWIDTH=625000,NAME=360p,RESOLUTION=640x360";
  echo '<br>';
  echo "https://etslive-2-vidio-com.akamaized.net/exp=1622814649~acl=/hls-p/ingest_6840_*/*~hmac=edaa841eefaab544841b9f7be7d7dd08f8d34ea2ba588784b2ca71caf41c51e4/hls-p/ingest_6840_360p/index.m3u8";
  echo '<br>';
  echo '<br>';
  echo "#EXT-X-STREAM-INF:PROGRAM-ID=1,CLOSED-CAPTIONS=NONE,BANDWIDTH=375000,NAME=240p,RESOLUTION=426x240";
  echo '<br>';
  echo "https://etslive-2-vidio-com.akamaized.net/exp=1622814649~acl=/hls-p/ingest_6840_*/*~hmac=edaa841eefaab544841b9f7be7d7dd08f8d34ea2ba588784b2ca71caf41c51e4/hls-p/ingest_6840_240p/index.m3u8";


}

else {echo "URL TIDAK BOLEH DIRUBAH";}


 ?>

