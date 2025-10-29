function getQuestions(){

questionList = ["1.What is the national flower of Japan?" , "2.What is the nickname for New York City?" , "3.What do you get when you boil water?" , "4.What is the hardest natural substance on planet Earth?" , "5.What is the process by which plants convert sunlight to energy?" , "6.What is the largest planet in our solar system?" , "7.What was the name of the famous ocean liner that sank on its first voyage in 1912?" , "8.Which book series is the best-selling of the 21st century?" , "9.What is the longest river in the world? " , "10.What is the capital of Canada?"]

return questionList;

}


function getChoices(){

choiceList = ["1.Roses  2.Tulips  3.Hibiscus 4.Cherry Blossoms" , "1.Miny City  2.The Big Bang  3.The Big Apple  4.Kanji" , "1.Water 2.Sand  3.Vapour  4.More Water" , "1.Rocks  2.Obsidian  3.Orb  4.Diamond" , "1.Mitosis  2.Meiosis  3.Chemosynthesis  4.Photosynthesis" , "1.Pluto  2.Mercury  3.Jupiter  4.Saturn" , "1.Ocean Waves  2.Lovers Boat  3.Titanic  4.Ice berg" , "1.Dork Diaries  2.Harry Potter  3.Half of a yellow sun  4.Diary of a wimpy kid" , "1.River Nile  2.Pacific Ocean  3.Atlantic Ocean 4.Nile Sea" , "1.Ottawa  2.Toronto  3.New York  4.Tokyo"]


return choiceList;

}

function rightAnswers(){

rightList = ["4" , "3" , "3" , "4" , "4" , "3" , "3" , "2" , "1" , "1"]


return rightList;
}




console.log("1.Get Quiz Questions");
console.log("0.End Game");

const prompt = require('prompt-sync')();
let choice = prompt("Enter your choice: ");

let isLoop = true;

while(isLoop){
switch(choice){
	case "1":
		console.log("Here are some quiz questions to keep your brain sharp");
	let solution = 0;
	let index = 0;
	let question = getQuestions();
	let answer = getChoices();
	let correct = rightAnswers();
	for(let count = 0; count < 10; count++){
		console.log(question[index]);
		console.log(answer[index]);
	
		let quizAnswer = prompt("Enter your choice: ");
		
		if(quizAnswer == correct[index]){
		console.log("You are correct /(^-^)/!!!");		solution += 1;
		}
		
		else{
			console.log("You are wrong (T-T)");
		}

		index += 1;
		}

		console.log("You got " + solution + " out of 10");
		choice = prompt("Enter (1) to play again (0) to leave: ");
	break;


	case "0": isLoop = false;
			break;














}



}



























