
function isPalindrome(words){
let new_list = [];
for(let count = 0; count < words.length; count++){
let reverse = "";
	for(let index = 0; index < words[count].length; index++){
	reverse = words[count].charAt(index) +reverse;
	
	if(words[count] == reverse){

	new_list[count] = true;

	}
	
	else{
	new_list[count] = false;
	
	}


}



}



return new_list;

}



let words = ["12321","11211" , "level"];
console.log(isPalindrome(words));










//console.log(new_list);