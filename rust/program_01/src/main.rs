use std::io;

/* 1. Write a program that prompts the user for two numbers and 
displays the addition, subtraction, multiplication, and division between them. */

fn main() {
    // Prompt the user to enter the first number
    println!("Enter the first number: ");
    let mut input1 = String::new();
    io::stdin().read_line(&mut input1).expect("Failed to read input.");
    let num1: f64 = input1.trim().parse().expect("Please enter a valid number.");

    // Prompt the user to enter the second number
    println!("Enter the second number: ");
    let mut input2 = String::new();
    io::stdin().read_line(&mut input2).expect("Failed to read input.");
    let num2: f64 = input2.trim().parse().expect("Please enter a valid number.");

    // Perform arithmetic calculations
    let sum = num1 + num2;
    let difference = num1 - num2;
    let product = num1 * num2;
    let quotient = num1 / num2;

    // Display the results
    println!("Addition : {}", sum);
    println!("Subtraction : {}", difference);
    println!("Multiplication : {}", product);
    println!("Division : {:.3}", quotient);
}
