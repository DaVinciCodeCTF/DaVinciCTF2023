<?php

function connect_to_db($ro_query) {
  $url = parse_url(getenv("DATABASE_URL"));

  $host = $url["host"];
  if ($ro_query){
    $username = "query_galleries";
    $password = "Y3grV4uErvNU#Z3P55Dg";
  }
  else {
    $username = $url["user"];
    $password = $url["pass"];
  }
  $database = substr($url["path"], 1);

  $conn = new PDO("mysql:host=$host;dbname=$database", $username, $password);
  return $conn;
}

?>