import java.util.Scanner;
import java.util.regex.Pattern;

public class Sectomin {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		System.out.print("Input time in seconds: ");
		String t = input.nextLine();
		if (! id(t)) {
			System.out.println("No se ha ingresado un número");
			System.exit(1);
		}
		int it = Integer.parseInt(t);
		System.out.println(String.format("%d:%d", it/60, it%60));
	}

	public static boolean id(String str) {
		Pattern p = Pattern.compile("^[-+]?[0-9]+$");
		return p.matcher(str).matches();
	}
}
