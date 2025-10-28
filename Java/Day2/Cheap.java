public class Cheap{


public double numberOfYearsTillFree(int numberOfItems){
double count = 0;
double fixedPrice = 50000;


if(numberOfItems > 0 && numberOfItems % 2 == 0){
fixedPrice = fixedPrice * numberOfItems;
while(fixedPrice != 0){
fixedPrice -= 4000;
count += 1;

}
return count;

}

else if(numberOfItems % 2 != 0){
fixedPrice = fixedPrice * numberOfItems;
while(fixedPrice != 2000){
fixedPrice -= 4000;
count += 1;

}

}
return count + 0.5;








}







}