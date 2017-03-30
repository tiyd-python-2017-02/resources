function updatePosition(){
    let settings = {
        url: 'http://api.open-notify.org/iss-now.json'
    }
    $.ajax(settings).done( function(result) {
        console.log(result);
        console.log(result.iss_position);
        console.log(result.iss_position.latitude);
        console.log(result.iss_position.longitude);
        let long = result.iss_position.longitude;
        let lat = result.iss_position.latitude;
        $('#longHook').html(long);
        $('#latHook').html(lat);
    });
    console.log("Here I am");
}
setInterval(updatePosition, 5000);
