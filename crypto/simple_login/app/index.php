<?php

require_once 'src/functions.php';
require_once 'src/db.php';
include 'secrets.php';

// Connect to the database
$conn = connect_to_db();

// Check if the user is logged in
$user = get_connected_user($conn);

// Close the database connection
$conn = null;

?>
<link rel="stylesheet" href="styles/style.css" type="text/css">
<div class="center">
  <h1>Welcome to the Site</h1>

  <?php if ($user): ?>
    <p>Well done !</p>
    <p>Here is your flag : <?= $my_flag ?> </p>
  <?php else: ?>
    <p>You are not logged in.</p>
    <div class="buttons">
      <button onclick="location.href='login.php'" class="login-button">Log in</button>
      <button onclick="location.href='register.php'" class="signup-button">Sign Up</button>
    </div>
  <?php endif; ?>
</div>

