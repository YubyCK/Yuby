package pl.yuby.kurs;

import java.util.Scanner;

public class test2 {
    public static void main(String[] args) {
        getPESELNumber();
        String pesel = "93111509597";
        System.out.println(validPESELNumber(pesel));
    }

    public static final int ADULT_AGE = 18;

    public static void getPESELNumber() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Welcome! Tell me ur PESEL Number: ");
        String peselNumber = scanner.nextLine();
        if ((peselNumber.length() % 11) != 0) {
            System.out.println("You tried to trick me you cheeky bastard!");
        }
    }

    public static boolean validPESELNumber(String checkPESELNumber) {
        char[] array = new char[11];
        for (int i = 0; i < 11; i++) {
            array[i] = checkPESELNumber.charAt(i);
        }
        int valid = (((array[0] - 48) % 10) + ((array[1] - 48) * 3) % 10 + ((array[2] - 48) * 7) % 10 + ((array[3] - 48) * 9) % 10 + ((array[4] - 48) % 10)
                + ((array[5] - 48) * 3) % 10 + ((array[6] - 48) * 7) % 10 + ((array[7] - 48) * 9) % 10 + (array[8] - 48) % 10 + ((array[9] - 48) * 3) % 10) % 10;
        return ((array[10] - 48) == (10 - valid));
    }
}
