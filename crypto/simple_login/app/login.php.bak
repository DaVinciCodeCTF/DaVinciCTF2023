<?php

require_once 'src/db.php';
include 'secrets.php';

assert(strlen($my_salt) == 27);
assert(md5($my_salt) == "46eaafcb93f2c5f8fc215cac38e1eaaf");


// Check if the form has been submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
  // Validate the form data
  $username = trim($_POST['username']);
  $password = trim($_POST['password']);
  $hash = trim($_POST['hash']);
  $errors = [];

  if (empty($username)) {
    $errors[] = 'Username is required';
  }

  if (empty($password)) {
    $errors[] = 'Password is required';
  }

  if (empty($hash)) {
    $errors[] = 'Hash is required';
  }


  // If there are no errors, try to log the user in
  if (empty($errors)) {
    $conn = connect_to_db();

    $stmt = $conn->prepare('SELECT * FROM users WHERE username = :username');
    $stmt->bindValue(':username', $username, PDO::PARAM_STR);
    $stmt->execute();
    $user = $stmt->fetch();
    if ($user && $password === $user['password']) {
      if (md5($my_salt . $username) === $hash){
        // Log the user in
        session_start();
        $_SESSION['user_id'] = $user['id'];
        header('Location: index.php');
        exit;
      }
      else {
        $errors[] = 'Wrong hash !';
      }
    } else {
      $errors[] = 'Invalid username or password';
    }
  }
}

?>
<link rel="stylesheet" href="styles/style.css" type="text/css">
<div class="login-form">
  <h1>Log In</h1>
  <form method="post">
    <label for="username">Username:</label><br>
    <input type="text" id="username" name="username"><br>
    <label for="password">Password:</label><br>
    <input type="password" id="password" name="password"><br>
    <label for="hash">Hash:</label><br>
    <input type="text" id="hash" name="hash"><br>
    <?php if (!empty($errors)): ?>
      <ul>
        <?php foreach ($errors as $error): ?>
          <li><?= $error ?></li>
        <?php endforeach; ?>
      </ul>
    <?php endif; ?>
    <br>
    <input type="submit" value="Submit">
  </form> 
</div>
