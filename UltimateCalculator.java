import java.util.Scanner;

public class UltimateCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double previousResult = 0.0;

        while (true) {
            System.out.println("Choose an operation:");
            System.out.println("1. Addition (+)");
            System.out.println("2. Subtraction (-)");
            System.out.println("3. Multiplication (*)");
            System.out.println("4. Division (/)");
            System.out.println("5. Power (^)");
            System.out.println("6. Square Root (√) of the first number");
            System.out.println("7. Absolute Value (|x|) of the first number");
            System.out.println("8. Factorial (!) of the first non-negative integer");
            System.out.println("9. Greatest Common Divisor (GCD) of two non-negative integers");
            System.out.println("10. Least Common Multiple (LCM) of two non-negative integers");
            System.out.println("11. Average of a series of numbers");
            System.out.println("12. Square of the first number");
            System.out.println("13. Clear previous result");
            System.out.println("14. Exit");

            int choice = getValidOperationChoice(scanner);

            double result = 0.0;
            switch (choice) {
                case 1:
                    result = performAddition(scanner);
                    break;
                case 2:
                    result = performSubtraction(scanner);
                    break;
                case 3:
                    result = performMultiplication(scanner);
                    break;
                case 4:
                    result = performDivision(scanner);
                    break;
                case 5:
                    result = performPower(scanner);
                    break;
                case 6:
                    result = performSquareRoot(scanner);
                    break;
                case 7:
                    result = performAbsoluteValue(scanner);
                    break;
                case 8:
                    result = performFactorial(scanner);
                    break;
                case 9:
                    result = performGCD(scanner);
                    break;
                case 10:
                    result = performLCM(scanner);
                    break;
                case 11:
                    result = performAverage(scanner);
                    break;
                case 12:
                    result = performSquare(scanner);
                    break;
                case 13:
                    previousResult = 0.0;
                    System.out.println("Previous result cleared.");
                    continue;
                case 14:
                    System.out.println("Goodbye!");
                    scanner.close();
                    return;
                default:
                    System.out.println("Invalid choice. Please choose a valid operation.");
                    continue;
            }

            previousResult = result;
            System.out.println("Result: " + result);
            System.out.println("Previous result: " + previousResult);

            // Ask if the user wants to perform another operation
            System.out.println("Do you want to perform another calculation? (y/n):");
            String again = scanner.next().trim().toLowerCase();
            if (!again.equals("y")) {
                System.out.println("Goodbye!");
                scanner.close();
                return;
            }
        }
    }

    private static int getValidOperationChoice(Scanner scanner) {
        while (true) {
            if (scanner.hasNextInt()) {
                int choice = scanner.nextInt();
                if (choice >= 1 && choice <= 14) {
                    return choice;
                }
            }
            System.out.println("Invalid choice. Please enter a number between 1 and 14:");
            scanner.nextLine();
        }
    }

    private static double getValidDoubleInput(Scanner scanner) {
        while (!scanner.hasNextDouble()) {
            System.out.println("Invalid input. Please enter a valid number:");
            scanner.next();
        }
        return scanner.nextDouble();
    }

    private static int getValidIntegerInput(Scanner scanner) {
        while (!scanner.hasNextInt()) {
            System.out.println("Invalid input. Please enter a valid integer:");
            scanner.next();
        }
        return scanner.nextInt();
    }

    private static double performAddition(Scanner scanner) {
        System.out.println("Enter the first number:");
        double number1 = getValidDoubleInput(scanner);
        System.out.println("Enter the second number:");
        double number2 = getValidDoubleInput(scanner);
        return number1 + number2;
    }

    private static double performSubtraction(Scanner scanner) {
        System.out.println("Enter the first number:");
        double number1 = getValidDoubleInput(scanner);
        System.out.println("Enter the second number:");
        double number2 = getValidDoubleInput(scanner);
        return number1 - number2;
    }

    private static double performMultiplication(Scanner scanner) {
        System.out.println("Enter the first number:");
        double number1 = getValidDoubleInput(scanner);
        System.out.println("Enter the second number:");
        double number2 = getValidDoubleInput(scanner);
        return number1 * number2;
    }

    private static double performDivision(Scanner scanner) {
        System.out.println("Enter the first number:");
        double number1 = getValidDoubleInput(scanner);
        System.out.println("Enter the second number:");
        double number2 = getValidDoubleInput(scanner);
        if (number2 == 0) {
            System.out.println("Error: Division by zero is not allowed.");
            return 0.0;
        }
        return number1 / number2;
    }

    private static double performPower(Scanner scanner) {
        System.out.println("Enter the base number:");
        double base = getValidDoubleInput(scanner);
        System.out.println("Enter the exponent number:");
        double exponent = getValidDoubleInput(scanner);
        return Math.pow(base, exponent);
    }

    private static double performSquareRoot(Scanner scanner) {
        System.out.println("Enter the number:");
        double number = getValidDoubleInput(scanner);
        if (number < 0) {
            System.out.println("Error: Cannot calculate square root of a negative number.");
            return 0.0;
        }
        return Math.sqrt(number);
    }

    private static double performAbsoluteValue(Scanner scanner) {
        System.out.println("Enter the number:");
        double number = getValidDoubleInput(scanner);
        return Math.abs(number);
    }

    private static double performFactorial(Scanner scanner) {
        System.out.println("Enter a non-negative integer:");
        int n = getValidIntegerInput(scanner);
        return factorial(n);
    }

    private static double performGCD(Scanner scanner) {
        System.out.println("Enter the first non-negative integer:");
        int num1 = getValidIntegerInput(scanner);
        System.out.println("Enter the second non-negative integer:");
        int num2 = getValidIntegerInput(scanner);
        return gcd(num1, num2);
    }

    private static double performLCM(Scanner scanner) {
        System.out.println("Enter the first non-negative integer:");
        int num1 = getValidIntegerInput(scanner);
        System.out.println("Enter the second non-negative integer:");
        int num2 = getValidIntegerInput(scanner);
        return lcm(num1, num2);
    }

    private static double performAverage(Scanner scanner) {
        System.out.println("Enter the number of elements:");
        int n = getValidIntegerInput(scanner);
        if (n <= 0) {
            System.out.println("Error: Number of elements must be greater than zero.");
            return 0.0;
        }
        double sum = 0.0;
        for (int i = 1; i <= n; i++) {
            System.out.println("Enter element " + i + ":");
            sum += getValidDoubleInput(scanner);
        }
        return sum / n;
    }

    private static double performSquare(Scanner scanner) {
        System.out.println("Enter the number:");
        double number = getValidDoubleInput(scanner);
        return Math.pow(number, 2);
    }

    private static double factorial(int n) {
        if (n == 0 || n == 1) {
            return 1;
        } else {
            return n * factorial(n - 1);
        }
    }

    private static int gcd(int a, int b) {
        if (b == 0) {
            return a;
        }
        return gcd(b, a % b);
    }

    private static int lcm(int a, int b) {
        return (a * b) / gcd(a, b);
    }
}
