import java.util.Scanner;

public class MainCheap{

public static void main(String... args){
Scanner scanner = new Scanner(System.in);
Cheap cheap = new Cheap();

System.out.print("Enter number of items: ");
int items = scanner.nextDouble();

System.out.print(cheap.numberOfYearsTillFree(items) + " Years");











}



}