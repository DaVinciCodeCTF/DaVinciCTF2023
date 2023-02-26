use std::{io, usize};
use rand::Rng;
use rand::thread_rng;
use image::{ImageBuffer, RgbImage};
use std::time::{SystemTime, UNIX_EPOCH};
use aes::Aes128;
use block_modes::{BlockMode, Cbc};
use block_modes::block_padding::Pkcs7;

const WIDTH: u32 = 200;

const MODULE_SIZE: u32 = 8;

const MODULE_WIDTH: u32 = WIDTH / MODULE_SIZE;

const PATTERN_SIZE: u32 = 7;

type Aes128Cbc = Cbc<Aes128, Pkcs7>;

fn main() {

    println!("\n---------------- QR code Generator -----------------");
    println!("Please enter the text for the QR Code (Max 30 char): ");

    let mut text: String = String::new();

    io::stdin().read_line(&mut text).expect("An error occurred while reading input!");

    if text.len() > 30 {
        text = text[..30].to_string();
    }

    generate_qr_code(text);

    println!("Your QR Code was generated!");
    println!("Bye");
}

fn generate_qr_code(text: String) {

    let mut img: RgbImage = ImageBuffer::new(WIDTH, WIDTH);
    for i in 0..img.width() {
        for j in 0..img.height() {
            *img.get_pixel_mut(i, j) = image::Rgb([255, 255, 255])
        }
    }

    draw_finding_pattern(&mut img);
    draw_timing_pattern(&mut img);
    draw_alignment_pattern(&mut img);

    let binary_data:String = build_data(text);

    draw_data(&mut img, binary_data);

    img.save("output.png").unwrap();

}

fn draw_module(img: &mut RgbImage, mut x: u32, mut y: u32) {
    x *= MODULE_SIZE;
    y *= MODULE_SIZE;

    for i in x..(x + MODULE_SIZE) {
        for j in y..(y + MODULE_SIZE) {

            if i >= WIDTH || j >= WIDTH {
                break;
            }
            *img.get_pixel_mut(i, j) = image::Rgb([0, 0, 0]);
        }
    }
}

fn draw_finding_pattern(img: &mut RgbImage) {
    for i in 0..PATTERN_SIZE {
        for j in 0..PATTERN_SIZE {
            if j == 0 || j == PATTERN_SIZE - 1 || i == 0 || i == PATTERN_SIZE - 1 || (i > 1 && i < PATTERN_SIZE - 2 && j > 1 && j < PATTERN_SIZE - 2) {
                draw_module(img, i, j);
            }
        }
    }
}

fn draw_timing_pattern(img: &mut RgbImage) {
    for i in PATTERN_SIZE + 1..=MODULE_WIDTH {
        if i % 2 == 0 {
            draw_module(img, i, 0);
            draw_module(img, 0, i);
        }
    }
}

fn draw_alignment_pattern(img: &mut RgbImage) {
    for i in 0..5 {
        for j in 0..5 {
            if (i == 2 && j == 2) || j == 0 || j == 4 || i == 0 || i == 4 {
                draw_module(img, i + MODULE_WIDTH - 8, j + MODULE_WIDTH - 8);
            }
        }
    }
}

fn is_in_timing_pattern(x: u32, y: u32) -> bool {
    return x == 1 || y == 1;
}

fn is_in_alignment_pattern(x: u32, y: u32) -> bool {
    return (x >= MODULE_WIDTH - 8 && x <= MODULE_WIDTH - 4 && y >= MODULE_WIDTH - 8 && y <= MODULE_WIDTH - 4) || (x <= PATTERN_SIZE && y <= PATTERN_SIZE);
}

fn draw_data(img: &mut RgbImage, binary_data: String) {
    let mut i: usize = 0;
    let mut x: u32 = MODULE_WIDTH - 1;
    let mut y: u32 = MODULE_WIDTH - 1;
    let mut up: bool = true;
    let mut is_left: bool = true;
    let mut c: char;

    while i < binary_data.len() && i < 480 {

        if !is_in_alignment_pattern(x, y) {
            c = binary_data.chars().nth(i).unwrap();
            if (x + y) % 2 == 0 {
                if c == '0' {
                    draw_module(img, x, y);
                }
            } else {
                if c == '1' {
                    draw_module(img, x, y);
                }
            }
            i += 1;
        }

        if up {
            y -= 1;
            up = false;
            continue;
        }

        if !is_left && (x + 1 == MODULE_WIDTH) {
            is_left = true;
            up = true;
            y -= 1;
            continue;
        }

        if is_left && is_in_timing_pattern(x - 1, y) {
            is_left = false;
            up = true;
            y -= 1;
            continue;
        }

        if is_left {
            x -= 1;
            y += 1;
        } else {
            x += 1;
            y += 1;
        }

        up = true;
    }

}

fn build_data(text: String) -> String {
    let mut data: String = String::new();
    let timestamp = get_current_timestamp();
    let iv = get_random_key16();

    data.push_str(format!("{:064b}", timestamp).as_str());
    for i in 0..16 {
        data.push_str(format!("{:08b}", iv[i]).as_str());
    }

    let ciphertext: Vec<u8> = cipher_data(text.as_bytes(), &timestamp.to_ne_bytes(), &iv);
    data.push_str(format!("{:08b}", ciphertext.len()).as_str());
    for i in 0..ciphertext.len() {
        data.push_str(format!("{:08b}", ciphertext[i]).as_str());
    }

    let mut rng = rand::thread_rng();
    while data.len() < 480 {
        data.push_str(&rng.gen_range(0..=1).to_string());
    }

    return data;
}

fn cipher_data(plaintext: &[u8], key: &[u8], iv: &[u8]) -> Vec<u8> {
    let cipher = Aes128Cbc::new_from_slices(&key, &iv).unwrap();

    let pos = plaintext.len();
    let mut buffer = [0u8; 128];
    buffer[..pos].copy_from_slice(plaintext);

    let ciphertext = cipher.encrypt(&mut buffer, pos).unwrap();

    return ciphertext.to_vec();
}

fn get_current_timestamp() -> u128 {
    let now = SystemTime::now();
    let timestamp = now
        .duration_since(UNIX_EPOCH)
        .expect("An error occurred!")
        .as_nanos();
    return timestamp;
}

fn get_random_key16() ->  [u8; 16]{
    let mut arr = [0u8; 16];
    thread_rng().try_fill(&mut arr[..]).expect("An error occurred!");
    return arr;
}