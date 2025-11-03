function getItems(items = []){


return items;
}

function getPrices(price = []){


return price;
}


function calculatePrice(getPrices){
	prices =getPrices
	sum = 0
	for(let count = 0; count <= prices.length; count++){
		sum += prices[count];}

	return sum
}


function calculateVAT(calculatePrice){
	cost = calculatePrice
	vatPrice = 0.075 * cost
	return vatPrice

}

function finalCost(calculatePrice, calculateVAT){
	price = calculatePrice
	cost = calculateVAT
	totalCost = price + cost
	return totalCost

}

function getBalance(payment , finalCost){
	cost = finalCost
	total = payment - cost
	return total
	
}


let itemList = [];
let priceList = [];

let isLooping = true;
const prompt = require('prompt-sync')();
while(isLooping){

let product = prompt("Enter product name (or stop): ");
	if(product == "stop" || product == "STOP"){
 		break;
	}

	else{
	itemList.push(product);
	let price = prompt("Enter price for " + product + " :");
	priceList.push(price);
	}























}
