function fizz_buzz(n){
    for(var i = 0; i <= n; i++) {
        txt = "";
        if (i % 3 == 0) { txt += "fizz"; }
        if (i % 5 == 0) { txt += "buzz"; }
        if (txt == "") { txt = i; }
        console.log(txt);
    }
}
