import java.util.Scanner;
public class StageTwo{


public String findOccurence(String word){

	word = "abcdefgh";
	char ch = word.charAt(3);

	char first = word.charAt(0);
	char second = word.charAt(1);
	char third = word.charAt(2);	
	
	char five = word.charAt(4);
	
	char six = word.charAt(5);

	char seven = word.charAt(6);

	char eight = word.charAt(7);

System.out.printf("%c%c%c%c%c%c%c%c",ch ,third ,second ,first, five, six, seven, eight);

return word;
} 




public int uniqueSum(int [] numbers){
int [] store = {2,3,2,2};
int sum = 0;
int index = 0;
for(int count = -1; count <= 2; count++){
//System.out.print(store[index]);

//if(store[index] == store[0] && store[index] == store[1] && //store[index] == store[2] && store[index] == store[3]){


sum += store[index];

//}
index += 1;


}

return index;
}




























}