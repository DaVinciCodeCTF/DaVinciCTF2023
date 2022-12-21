<?php

function get_connected_user($conn) {
    session_start();
    if (isset($_SESSION['user_id'])) {
        $user_id = (int)$_SESSION['user_id'];
        $stmt = $conn->prepare('SELECT * FROM users WHERE id = :id');
        $stmt->bindValue(':id', $user_id, PDO::PARAM_INT);
        $stmt->execute();
        return $stmt->fetch();
    }
    return null;
}

?>