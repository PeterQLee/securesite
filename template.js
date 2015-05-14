$(document).ready(function() {
    //$("#refresh").hide();
    $(".eventlogs").load("logs/%sLogs.txt");
    $("#refresh").click(function() {
        $(".eventlogs").load("logs/%sLogs.txt");
    });
});
