function perfectSquares(numbers){
let new_list = [];
let index = 0;
let divisor = 2;
for(let count = 1; count <= numbers.length; count++){

while(numbers[index] % divisor != 0){divisor += 1;}

let base = numbers[index] / divisor;
if(base * base == numbers[index]){


new_list[index] = true;
}

else{
new_list[index] = false;
}
index += 1;
}

return new_list;


}


numbers = [4, 5, 25, 36, 100];
console.log(perfectSquares(numbers));