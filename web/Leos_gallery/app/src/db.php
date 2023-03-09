<?php

function connect_to_db() {
  $url = parse_url(getenv("DATABASE_URL"));

  $host = $url["host"];
  $username = $url["user"];
  $password = $url["pass"];
  $database = substr($url["path"], 1);

  $conn = new PDO("mysql:host=$host;dbname=$database", $username, $password);
  return $conn;
}

?>
