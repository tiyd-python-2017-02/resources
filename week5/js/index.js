// this is a single line comment.

/*  this is
a multi
line
comment
*/

console.log("Hi mom") //after a statement.


function x()
{
    console.log("yo")
}

x()
function initialize(x){
    console.log("initialize");
    return 0;
}

function test(x){
    console.log("test");
    return x < 10;
}

function update(x){
    console.log("update")
    return ++x;
}

for (var i = initialize(i); test(i); i = update(i)){
    console.log(i)
}

function lhs(){
    console.log("lhs");
    return true
}
function rhs(one, two, three){
    console.log(one, two, three)
    console.log("rhs");
    return true
}

lhs(true, true, true) && rhs(false)

function testScope(){
    if(true){
        let no_colisions = 5;
        if(true){
            console.log(no_colisions);
        }
    }
    //console.log(no_colisions);
}

testScope()

function doStuff(){
    console.log(document);
    console.log(document.getElementById("hi"));

    document.getElementById("hi").innerHTML = "Now we're <h1>getting</h1> to the fun part";
    document.getElementById("hi").style.borderColor = "#123456"
    document.getElementById("hi").style.borderWidth = "10px"
    document.getElementById("hi").style.borderStyle = "solid"
    console.log(document.querySelectorAll("#one, #three"))
}

var $hi_element = $("#hi");
$hi_element.html("Say Hi")
console.log($hi_element.html())
console.log($("#hi"))

$new_list = $("<ul>")

for(var i = 0; i < 10; i++)
{
    console.log(i)
    $new_item = $("<li>")
    $new_item.html(i)
    $new_list.append($new_item)
}
console.log($new_list)

$("body").prepend($new_list)

function doClickStuff(e){
    e.target.hasBeenClicked = true
    console.log(e)
    console.log(e.target)
    alert("I got clicked")
}

function doOut(e){
    if(e.target.hasBeenClicked){
        e.target.style.backgroundColor="green"
    }
    else{
        e.target.style.backgroundColor="blue"
    }
}

function doOver(e){
    e.target.style.backgroundColor="red"
}

$('button').click(doClickStuff)
$('button').on('mouseover', doOver)
$('button').on('mouseout', doOut)
// $('title').html(prompt("new name? "))
$('button').on('contextmenu', function() {
    console.log("I got right clicked")
})
