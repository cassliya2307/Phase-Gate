function occupySpaces(slot , parking_list = []){
	parking_list.splice(slot - 1, 1, 1)
	return "You've occupied this slot"
}

function leaveSpaces(slot , parking_list = []){
	parking_list.splice(slot - 1, 1, 0)
	return "You've left the space"
}


let available_spots = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 , 0];

const prompt = require('prompt-sync')();
let isLoop = true;


while(isLoop){
console.log("~~Welcome To Mikasa's Parking Lot~~");
console.log("Please Drive Safely/(* - *)/");
console.log("1.Get Parking Space");
console.log("2.Leave Parking Space");
console.log("3.Display Slots");
console.log("0.Leave parking lot");


let choice = prompt("Enter your choice: ");

switch(choice){

case "1":

let slot = prompt("Enter a slot number from (1 - 20): ");

if(slot <= 20){
console.log(occupySpaces(slot , available_spots));

}

else{console.log("No such slot")}
break;
		

case "2":
let slot2 = prompt("Enter a slot number from (1 - 20): ");
if(slot2 <= 20){
if(available_spots[slot2 - 1] == 1){
console.log(leaveSpaces(slot2 , available_spots));
}

else{console.log("Slot originally empty")}
}
else{console.log("No such slot")}


break;

case "3":
console.log(available_spots);
break;


case "0": isLoop = false;
break;

default:
console.log("Invalid input!!!");
break;


}

}