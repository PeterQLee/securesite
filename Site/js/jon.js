$(document).ready(function() {
    //$("#refresh").hide();
    $(".eventlogs").load("logs/jonLogs.txt");
    $("#refresh").click(function() {
        $(".eventlogs").load("logs/jonLogs.txt");
    });
});
