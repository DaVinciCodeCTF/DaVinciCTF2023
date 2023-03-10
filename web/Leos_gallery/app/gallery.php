<?php
    include_once 'src/header.php';
    require_once 'src/db.php';
    include 'secrets.php';

    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        $images = [];
        $sql_req = trim($_POST['images']);
        $values = explode("|",$sql_req);
        if (isset($values[0]) && !strcmp(md5($my_salt.$values[0]),$values[1])) {
            $conn = connect_to_db(true);
            $conn->exec("SET TRANSACTION ISOLATION LEVEL REPEATABLE READ");
            $stmt = $conn->prepare(base64_decode($values[0]));
            $stmt->execute();

            while ($wallpapers = $stmt->fetch(PDO::FETCH_NUM)){
                $images[$wallpapers[1]] = $wallpapers[2];
            }
        }  
    }
?>

<form method="post">
    <select name="images">
        <option value="|8fc8cee62b7d63c442c0d331346c3ec9"></option>
        <option value="U0VMRUNUICogRlJPTSBsYW5kc2NhcGVzV2FsbHBhcGVyczs=|fadf91bd99bf7474edd040d6aaf3ed06">Landscapes</option>
        <option value="U0VMRUNUICogRlJPTSBhbmltYWxzV2FsbHBhcGVyczs=|2703d13c178ef89d4e614490b6b08c92">Animals</option>
        <option value="U0VMRUNUICogRlJPTSBhYnN0cmFjdFdhbGxwYXBlcnM7|59e6374a0cb4ed5401cd73a0e25cd804">Abstract</option>
        <option value="U0VMRUNUICogRlJPTSB1c2VyV2FsbHBhcGVyczs=|b480e2d69cb41122048c3be17a7adee0">Your wallpapers</option>
    </select>
    <input type="submit" value="Show Me !">
</form>


<div class="images">
    <?php if (!empty($images)): ?>
        <?php foreach ($images as $image_name => $image_path): ?>
            <img src="<?= $image_path ?>" alt="<?= $image_name ?>" title="<?= $image_name ?>" />
        <?php endforeach; ?>
    <?php endif; ?>
</div>