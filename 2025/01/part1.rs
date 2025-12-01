use std::{
    fs::File,
    io::{self, BufRead, BufReader},
    path::Path,
};

fn lines_from_file(filename: impl AsRef<Path>) -> io::Result<Vec<String>> {
    BufReader::new(File::open(filename)?).lines().collect()
}

fn main() {
    let lines = lines_from_file("./input.txt").expect("AOC");
    let mut x = 50;
    let mut cnt = 0;
    let m = 100;
    for line in lines {
        let op = line.chars().nth(0);
        let number:i32 = (&line.chars().as_str()[1..]).parse().unwrap();
        if op == Some('R') {
            x += number;
        }
        else {
            x -= number;
        }
        x %= m;
        if x == 0 {
            cnt += 1;
        }
    }
    println!("{cnt}");
}
