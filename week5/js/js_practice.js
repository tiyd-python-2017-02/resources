let message = "Hello World";
let another = "Hi Mom";
let number = 5;
console.log(message);
console.log(another);
console.log(number);
console.log("I'm " + number + " years old!");
console.log(`I'm ${number} years old!`);
let movies = ["top gun", "super troopers", "star wars", "hidden figures"];
console.log(movies);
movies.push("easy a");
movies.push("rebel without a cause");
movies.push("cool hand luke");
console.log(movies);
//loop over the indices of the array movies and log each one to the screen.
for(index in movies){
    console.log(movies[index]);
}

//find the body of the page, append a new ul element with an id of "list"
$('body').append($('<ol>').attr('id', "list"));
//grab the newly created list element
$list = $('#list')
//append a new list item to the #list element and set the html to be each movie.
for(let i = 0; i < movies.length; i++){
    $list.append($('<li>').html(movies[i]))
}

let sentence = "the quick brown fox jumps over the lazy dog";
console.log(sentence.split(" "));

function isPalindrome(word){
    word = word.replace(/[\s\W]/g, '').toLowerCase();
    if (word.length <= 1) {
        return true;
    }
    return (word[0] === word[word.length-1]) && isPalindrome(word.substring(1, word.length-1));
}
