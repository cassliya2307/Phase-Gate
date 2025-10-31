import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;
public class ParkingLotTest{

	@Test
	public void testThatTheFunctionReturnsAnEmptyArray(){

	ParkingLot parkingLot = new ParkingLot();
	
	int [] space = new int [9]; 

	int [] result = parkingLot.getSpaceToPark();

	assertEquals(space , result);

	

	}	






	}