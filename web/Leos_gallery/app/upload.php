<?php
    include_once 'src/header.php';
    require_once 'src/db.php';
    include 'secrets.php';
    
    if(!empty($_FILES['myFile']) && $_FILES['myFile']['error'] == 0) {

        $filepath = $_FILES['myFile']['tmp_name'];
        $fileSize = filesize($filepath);
        $fileinfo = finfo_open(FILEINFO_MIME_TYPE);
        $filetype = finfo_file($fileinfo, $filepath);
        
        if ($fileSize === 0) {
            die("The file is empty.");
        }
        
        if ($fileSize > 5*1024*1024) {
            die("The file is too large");
        }
        
        $allowedTypes = [
        'image/png' => 'png',
        'image/jpeg' => 'jpg'
        ];
        
        if (!in_array($filetype, array_keys($allowedTypes))) {
            die("File not allowed.");
        }
        
        $filename = "user_".mt_rand();
        $extension = $allowedTypes[$filetype];
        $targetDirectory = __DIR__ . "/img/user";
        
        $newFilepath = $targetDirectory . "/" . $filename . "." . $extension;
        
        if (move_uploaded_file($filepath, $newFilepath)) {
            $conn = connect_to_db(false);
            $stmt = $conn->prepare("INSERT INTO userWallpapers(image_name,image_path) VALUES(:name,:path)");
            $stmt->bindParam(':name',$_FILES['myFile']['name']);
            $db_path = "img/user/".$filename.".".$extension;
            $stmt->bindParam(':path',$db_path);
            try {
                $stmt->execute();
            }
            catch(PDOException $e){
                die("Error!: " . $e->getMessage());
            }
        }
        else{
            die("Can't move file.");
            unlink($filepath);
        }
        
        echo "File uploaded successfully :)";

    }
    
?>

<form class="uploadImage" method="post" action="upload.php" enctype="multipart/form-data">
   <input type="file" name="myFile" />
   <input type="submit" value="Upload">
</form>

