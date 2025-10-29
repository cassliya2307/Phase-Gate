import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;
public class StageTwoTest{


	@Test
	public void testThatItReturnCorrectly(){
	
	StageTwo stageTwo = new StageTwo();

	String result = stageTwo.findOccurence("abcdefgh");
	
	
	assertEquals(result, "abcdefgh");



	}


	@Test
	public void testThatTheLengthFuctionReturnsCorrectly(){
	StageTwo stageTwo = new StageTwo();
	int [] store = {1 , 2, 3, 4};

	int result = stageTwo.uniqueSum(store);


	assertEquals(result, 4);


	}















}