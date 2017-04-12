Handlebars.registerHelper('prevent-orphan', function(text) {
    var lastSpace = text.lastIndexOf(" ");
    return text.slice(0, lastSpace) + text.slice(lastSpace).replace(' ', "&nbsp;");
});

var context = {
  title: 'Block Helper Post',
  content: 'All the things and stuff!',
  author: 'Daniel Yuschick',
  image: 'dan.jpg',
  sources: ['CSS Weekly', 'Smashing Magazine']
}


var source = $('#post-template').html();
var template = Handlebars.compile(source);
var htmlOutput = template(context);
console.log(htmlOutput);
$('#content').html(htmlOutput);


// $.ajax(url).done(function(result){
//     context = result;
//
//     var source = $('#post-template').html();
//     var template = Handlebars.compile(source);
//     var htmlOutput = template(context);
//     console.log(htmlOutput);
//     $('#content').html(htmlOutput);
// })



var newContext = {
  title: 'Our First Post',
  content: 'This is some content for our post. here is some more text so that we can demonstrate the orphan word functionality',
  author: 'Daniel Yuschick',
  sources: [
    { title: 'CSS Weekly', url: 'http://css-weekly.com/' },
    { title: 'Smashing Magazine', url: 'https://www.smashingmagazine.com/' },
  ]
};


var source = $('#new-post-template').html();
var template = Handlebars.compile(source);
var htmlOutput = template(newContext);
console.log(htmlOutput);
$('#newContent').html(htmlOutput);
