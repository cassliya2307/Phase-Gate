import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;
public class CheapTest{
	@Test
	public void testThatItReturnTheNumberOfYears(){
	
	Cheap cheap = new Cheap();

	int answer = cheap.numberOfYearsTillFree(1);

	assertEquals(answer, 12.5);


	}

	@Test
	public void testThatTheNumberOfYearsHasChanged(){

	Cheap cheap = new Cheap();

	int answer = cheap.numberOfYearsTillFree(2);

	
	assertEquals(answer, 25.0);

	}















}