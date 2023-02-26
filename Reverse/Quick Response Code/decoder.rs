//Only for WU
use image::{GenericImageView};
use aes::Aes128;
use block_modes::{BlockMode, Cbc};
use block_modes::block_padding::Pkcs7;

const WIDTH: u32 = 200;

const MODULE_SIZE: u32 = 8;

const MODULE_WIDTH: u32 = WIDTH / MODULE_SIZE;

const PATTERN_SIZE: u32 = 7;

type Aes128Cbc = Cbc<Aes128, Pkcs7>;

fn main() {

    let path: String = String::from("path_to_png");
    decode_qr_code(path);
}

fn decode_qr_code(path: String) {
    let img = image::open(path).expect("File not found!");
    let black_pixel = image::Rgba([0, 0, 0, 255]);

    let mut i: usize = 0;
    let mut x: u32 = MODULE_WIDTH - 1;
    let mut y: u32 = MODULE_WIDTH - 1;
    let mut up: bool = true;
    let mut is_left: bool = true;

    let mut binary_data: String = String::new();

    while i < 480 {

        if !is_in_alignment_pattern(x, y) {
            if (x + y) % 2 == 0 {
                if img.get_pixel(x * MODULE_SIZE, y * MODULE_SIZE) != black_pixel {
                    binary_data.push_str("1");
                } else {
                    binary_data.push_str("0");
                }
            } else {
                if img.get_pixel(x * MODULE_SIZE, y * MODULE_SIZE) == black_pixel {
                    binary_data.push_str("1");
                } else {
                    binary_data.push_str("0");
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

    let timestamp: u128 = u128::from_str_radix(&binary_data[0..64], 2).unwrap();
    let mut iv: [u8; 16] = [0; 16];
    for i in 0..16 {
        iv[i] = u8::from_str_radix(&binary_data[(64 + (i * 8))..(64 + (i * 8) + 8)], 2).unwrap();
    }
    let length: usize = usize::from_str_radix(&binary_data[192..200], 2).unwrap();
    println!("Recover: Key: {}, IV: {:?}, Data Length: {}", timestamp, iv, length);

    let mut ciphertext = vec![0; length];
    for i in 0..length {
        ciphertext[i] = u8::from_str_radix(&binary_data[(200 + (i * 8)..200 + (i * 8) + 8)], 2).unwrap();
    }

    let plaintext: String = decrypt_data(&ciphertext, &timestamp.to_ne_bytes(), &iv);
    println!("Plaintext: {}", plaintext);

}

fn is_in_timing_pattern(x: u32, y: u32) -> bool {
    return x == 1 || y == 1;
}

fn is_in_alignment_pattern(x: u32, y: u32) -> bool {
    return (x >= MODULE_WIDTH - 8 && x <= MODULE_WIDTH - 4 && y >= MODULE_WIDTH - 8 && y <= MODULE_WIDTH - 4) || (x <= PATTERN_SIZE && y <= PATTERN_SIZE);
}

fn decrypt_data(ciphertext: &Vec<u8>, key: &[u8], iv: &[u8]) -> String {
    let cipher = Aes128Cbc::new_from_slices(&key, &iv).unwrap();

    let mut buffer = ciphertext.to_vec();

    let plaintext = cipher.decrypt(&mut buffer).unwrap();

    return String::from_utf8(plaintext.to_vec()).unwrap();
}