CREATE USER 'query_galleries'@'%' IDENTIFIED BY 'Y3grV4uErvNU#Z3P55Dg';

GRANT SELECT ON dvc_db.* TO 'query_galleries'@'%';

CREATE TABLE userWallpapers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    image_name VARCHAR(255) NOT NULL,
    image_path VARCHAR(255) NOT NULL
);

CREATE TABLE landscapesWallpapers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    image_name VARCHAR(255) NOT NULL,
    image_path VARCHAR(255) NOT NULL
);

CREATE TABLE animalsWallpapers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    image_name VARCHAR(255) NOT NULL,
    image_path VARCHAR(255) NOT NULL
);

CREATE TABLE abstractWallpapers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    image_name VARCHAR(255) NOT NULL,
    image_path VARCHAR(255) NOT NULL
);

CREATE TABLE sup3r53cretd4t4 (
    id INT AUTO_INCREMENT PRIMARY KEY,
    myb3l0v3dfl4g VARCHAR(255) NOT NULL
);

INSERT INTO landscapesWallpapers(image_name,image_path) VALUES("Beach","img/landscapes/beach.jpg");
INSERT INTO landscapesWallpapers(image_name,image_path) VALUES("Moutain","img/landscapes/moutain.jpg");
INSERT INTO landscapesWallpapers(image_name,image_path) VALUES("River","img/landscapes/river.jpg");
INSERT INTO landscapesWallpapers(image_name,image_path) VALUES("Winter","img/landscapes/winter.jpg");

INSERT INTO animalsWallpapers(image_name,image_path) VALUES("Frog","img/animals/frog.jpg");
INSERT INTO animalsWallpapers(image_name,image_path) VALUES("Kitty","img/animals/kitty.jpg");
INSERT INTO animalsWallpapers(image_name,image_path) VALUES("Squirrel","img/animals/squirrel.jpg");
INSERT INTO animalsWallpapers(image_name,image_path) VALUES("Tiger","img/animals/tiger.jpg");

INSERT INTO abstractWallpapers(image_name,image_path) VALUES("Bubbles","img/abstract/bubbles.jpg");
INSERT INTO abstractWallpapers(image_name,image_path) VALUES("Columns","img/abstract/columns.jpg");
INSERT INTO abstractWallpapers(image_name,image_path) VALUES("Fluids","img/abstract/fluids.jpg");
INSERT INTO abstractWallpapers(image_name,image_path) VALUES("Spirale","img/abstract/spirale.jpg");

INSERT INTO sup3r53cretd4t4(myb3l0v3dfl4g) VALUES("dvCTF{h4sh_l3ngth_3xt3ns1on_1s_funny}");
