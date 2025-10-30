public class DayFour{

public static boolean [] perfectSquare(int [] numbers){
boolean [] new_list = new boolean [numbers.length];
int index = 0;
int index2 = 0;
int divisor = 2;
int base = 0;
for(int count = 0; count < numbers.length; count++){

if(numbers[index] == 1){new_list[index] = true;
index += 1;
}

else{
while(numbers[index] % divisor != 0){divisor += 1;}

base = numbers[index] / divisor;
if(base * base == numbers[index]){


new_list[index] = true;
}

else{
new_list[index] = false;
}
index += 1;
//System.out.print(new_list[index2]);
}
}
return new_list;



}

}