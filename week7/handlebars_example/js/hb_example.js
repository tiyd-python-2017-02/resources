var source = $('#post-template').html();
var template = Handlebars.compile(source);
var context = [
    {
        title: 'Our First Post',
        content: 'This is some content for our post.',
        author: 'Daniel Yuschick'
    },
    {
        title: 'Our Second Post',
        content: 'There was a basketball game last night.',
        author: 'Vitale'
    },
    {
        title: 'Our Third Post',
        content: 'There were two teams that played...  Gonzaga and UNC',
        author: 'Roy'
    },
    {
        title: 'Our Fourth Post',
        content: '<strike>UNC crushed the souls of John Stockton and Duke fans everywhere.</strike>',
        author: 'Devils'
    },
];
for(var i = 0; i < context.length; i++){
    var html = template(context[i]);
    if(i % 3 == 0){
        var $newRow = $("<div>").addClass("row");
        $('#grid').append($newRow);
    }
    $newRow.append(html);
}
