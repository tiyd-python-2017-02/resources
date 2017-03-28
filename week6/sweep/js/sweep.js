let mineCount = 0;
let clickCount = 0;
let X = 10;
let Y = 10;
let isGameOver = false;
let isFirst;
function gameOver(won){
    if(won){
        isGameOver = true;
    }
    for(var i = 0; i < Y; i++){
        for(var j = 0; j < X; j++){
            var cell = getCell(j, i);
            if(cell.hasClass('mine')) {
                if(won){
                    cell.addClass('safe');
                } else {
                    cell.addClass('dead');
                }
            } else {
                cell.click();
            }
        }
    }
}

function getCell(x,y){
    return $("#cell_" + x + "_" + y);
}

function getNeighbors(currentCell){
    // x-1,y-1   x,y-1   x+1,y-1
    // x-1,y     x,y     x+1,y
    // x-1,y+1   x,y+1   x+1, y+1
    let y = currentCell.parentNode.rowIndex;
    let x = currentCell.cellIndex;
    let xe = x-1;
    let xw = x+1;
    let yn = y-1;
    let ys = y+1;
    let ne = getCell(xe, yn);
    let n  = getCell(x,  yn);
    let nw = getCell(xw, yn);
    let e  = getCell(xe, y);
    let w  = getCell(xw,  y);
    let se = getCell(xe, ys);
    let s  = getCell(x,  ys);
    let sw = getCell(xw, ys);

    return [ne,n,nw,e,w,se,s,sw];
}

function countNeighboringMines(neighbors) {
    let count = 0;
    for(let i = 0; i < neighbors.length; i++){
        if(neighbors[i].hasClass('mine')){
            count++;
        }
    }
    return count;
}

function cell_clicked(e){
    // console.log(e);
    // console.log(e.target);
    let $src = $(e.target);
    if(isFirst){
        isFirst = false;
        mineCount--;
        $src.removeClass('mine');
    }

    $src.addClass("clicked");
    $src.off('click')
    if($src.hasClass("mine")){
        if(isGameOver){
            $src.addClass('safe');
        } else {
            $src.addClass('dead');
            gameOver(false);
        }
    } else {
        clickCount++;
        let neighbors = getNeighbors(e.target);
        let count = countNeighboringMines(neighbors);
        if(count === 0){
            neighbors.forEach(function(neighbor) { neighbor.click() });
        }
        else{
            let classes = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight']
            $src.addClass(classes[count]);
            $src.html(count);
        }
    }
    if(clickCount+mineCount === X*Y){
        gameOver(true);
    }
}

function cell_right_clicked(e){
    //preventDefault stops default action like opening the context menu.
    e.preventDefault();
    if(!$(e.target).hasClass('clicked')){
        $(e.target).toggleClass('flag');
    }
}


function buildGameBoard(x, y){
    isFirst = true;
    let $board = $('<table>');
    for(var i = 0; i < y; i++){
        let $row = $('<tr>');

        $board.append($row);
        for(var j = 0; j < x; j++){
            let $cell = $('<td>');
            $row.append($cell);
            if(Math.random() < .2) {
                $cell.addClass('mine')
                mineCount++;
            }
            $cell.attr('id', 'cell_' + j + '_' + i);
            $cell.on('click', cell_clicked);
            $cell.on('contextmenu', cell_right_clicked);
        }
    }
    $('#gameBoard').append($board);
    console.log($board);
}

buildGameBoard(X, Y)
