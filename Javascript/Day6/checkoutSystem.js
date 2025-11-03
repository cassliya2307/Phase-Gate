function getItems(items){

return items;
}

function getPrices(price){


return price;
}


function calculatePrice(getPrices){
	prices = getPrices
	
	sum = 0
	for(let count = 0; count <= prices.length - 1; count++){
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
	let produce = getItems(itemList);
	let price = getPrices(priceList);
	let VAT = calculateVAT(calculatePrice(getPrices(priceList)));
	let subtotal = calculatePrice(getPrices(priceList));
	let total = finalCost(calculatePrice(getPrices(priceList)) , calculateVAT(calculatePrice(getPrices(priceList))));
	

	console.log("~~~~INVOICE~~~~");
	for(let count = 0; count <= produce.length - 1; count++){
		produce[count];	
		price[count];
		console.log(produce[count] + " : " + price[count]);
		
	}	
		console.log("SubTotal : N" + subtotal);
		console.log("VAT(7.5%): N" + VAT);
		console.log("TOTAL    : N" + total);

		let payment = prompt("Enter your payemt: ");
		
		while(payment < total){
		console.log("The inputted amount is not up to the total");
		payment = prompt("Enter your payemt: ");
		let balance = getBalance(payment , total);
		}
		balance = getBalance(payment , total);

		console.log("~~~PAYMENT~~~");		
		for(let count = 0; count <= produce.length - 1; count++){
		produce[count];	
		price[count];
		console.log(produce[count] + " : " + price[count]);
		
	}
		console.log("Total Paid  : N" + payment);
		console.log("Grand total : N" + total);
		console.log("Balance     : N" + balance);
		//console.log("Payment successful thank you for shopping\(~ 3 ~)\");	


	break;
	}

	else{
	itemList.push(product);
	let price = prompt("Enter price for " + product + " : ");
	while(price < 0){console.log("We don't accept negative prices");
		price = prompt("Enter price for " + product + " : ");
	
}
	price = Number(price);
	priceList.push(price);
	
	}























}
