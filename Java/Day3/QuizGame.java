import java.util.Scanner;

public class QuizGame{

public static void main(String... args){
String[] question = QuizGameFunction.questions();
String[] answer = QuizGameFunction.answers();
String[] correctAnswer = QuizGameFunction.rightAnswer();
Scanner scanner = new Scanner(System.in);
String main = """
1.Get Quiz Questions
0.End Game
""";
System.out.print(main);
System.out.print("Enter your choice: ");
String choice = scanner.nextLine();
boolean isLoop = true;

while(isLoop){
switch(choice){
	case "1"->{
	System.out.print("Here are some quiz questions to keep your brain sharp");
	int solution = 0;
	int index = 0;
	for(int count = 0; count < 10; count++){
		System.out.println(question[index]);
		System.out.println(answer[index]);
	
		System.out.print("Enter your choice: ");
		String quizAnswer = scanner.nextLine();
		if(quizAnswer.equals(correctAnswer[index])){
		System.out.println("You are correct /(^-^)/!!!");		solution += 1;
		}

		else{
			if(!quizAnswer.equals("1") && !quizAnswer.equals("2") && !quizAnswer.equals("3") && !quizAnswer.equals("4")){
		System.out.println("Option not available , You're Wrong");
		}
		else{
		
		System.out.println("You are wrong (T-T)");
		}
		}
		index += 1;
		}	



	System.out.println("You got " + solution + " out of 10");
	System.out.print("Enter (1) to play again (0) to leave: ");
	choice = scanner.nextLine();

	}
	
	
	case "0"->{isLoop = false;}

	default->{System.out.println("Invalid Input");
		System.out.print("Enter (1) to play again (0) to leave: ");
		choice = scanner.nextLine();

		}

}


	




}









}





}