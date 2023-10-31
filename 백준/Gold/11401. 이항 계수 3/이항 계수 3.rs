// test performance

const P: i64 = 1_000_000_007;

fn main() {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).expect("Failed to read input");
    let mut parts = input.trim().split_whitespace().map(|s| s.parse::<i64>().expect("Invalid input"));
    
    let n = parts.next().unwrap();
    let k = parts.next().unwrap();
    
    let denom = (factorial(k) * factorial(n - k)) % P;
    println!("{}", (factorial(n) * pow(denom, P - 2)) % P);
}

fn factorial(n: i64) -> i64 {
    let mut result = 1;
    for i in 1..=n {
        result *= i;
        result %= P;
    }
    result
}

fn pow(base: i64, exp: i64) -> i64 {
    let mut ret = 1;
    let mut base = base;
    let mut exp = exp;
    
    while exp > 0 {
        if exp % 2 == 1 {
            ret *= base;
            ret %= P;
        }
        base = (base * base) % P;
        exp /= 2;
    }
    ret
}
