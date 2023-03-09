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
        
        if ($fileSize > 5*1024*1024) { // 3 MB (1 byte * 1024 * 1024 * 3 (for 3 MB))
            die("The file is too large");
        }
        
        $allowedTypes = [
        'image/png' => 'png',
        'image/jpeg' => 'jpg'
        ];
        
        if (!in_array($filetype, array_keys($allowedTypes))) {
            die("File not allowed.");
        }
        
        $filename = "user_".mt_rand(); // I'm using the original name here, but you can also change the name of the file here
        $extension = $allowedTypes[$filetype];
        $targetDirectory = __DIR__ . "/img/user"; // __DIR__ is the directory of the current PHP file
        
        $newFilepath = $targetDirectory . "/" . $filename . "." . $extension;
        
        if (move_uploaded_file($filepath, $newFilepath)) { // Copy the file, returns false if failed
            $conn = connect_to_db();
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
            unlink($filepath); // Delete the temp file
        }
        
        echo "File uploaded successfully :)";

    }
    
?>

<form class="uploadImage" method="post" action="upload.php" enctype="multipart/form-data">
   <input type="file" name="myFile" />
   <input type="submit" value="Upload">
</form>

