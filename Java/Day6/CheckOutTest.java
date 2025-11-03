import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class CheckOutTest{


	@Test
	public void testThatFuctionGetItemsIsReturningAString(){
	Check check = new Check();

	String result = check.getItems("fruit");

	assertEquals(result , "fruit");



}

	@Test
	public void testThatFunctionGetPricesIsReturningAFloat(){
	Check check = new Check();

	double result = check.getPrices(9.8);

	assertEquals(result , 9.8);







	}








}