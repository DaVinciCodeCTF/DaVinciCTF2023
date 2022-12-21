<?php

require_once 'src/db.php';

// Check if the form has been submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
  // Validate the form data
  $username = trim($_POST['username']);
  $password = trim($_POST['password']);

  $errors = [];

  if (empty($username)) {
    $errors[] = 'Username is required';
  }

  if (empty($password)) {
    $errors[] = 'Password is required';
  }

  // If there are no errors, insert the new user into the database
  if (empty($errors)) {
    $conn = connect_to_db();

    $stmt = $conn->prepare('INSERT INTO users (username, password) VALUES (:username, :password)');
    $stmt->bindValue(':username', $username, PDO::PARAM_STR);
    $stmt->bindValue(':password', $password, PDO::PARAM_STR);
    $stmt->execute();

    header('Location: login.php');
    exit;
  }
}

?>
<link rel="stylesheet" href="styles/style.css" type="text/css">
<div class="signup-form">
  <h1>Sign Up</h1>
  <form method="post">
    <label for="username">Username:</label><br>
    <input type="text" id="username" name="username"><br>
    <label for="password">Password:</label><br>
    <input type="password" id="password" name="password"><br>
    <?php if (!empty($errors)): ?>
      <ul>
        <?php foreach ($errors as $error): ?>
          <?= $error ?>
        <?php endforeach; ?>
      </ul>
    <?php endif; ?>
    <br>
    <input type="submit" value="Submit">
  </form> 
</div>



