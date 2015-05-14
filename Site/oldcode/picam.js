$(document).ready(function() {
    //$("#refresh").hide();
    $(".eventlogs").load("logs/PiCamLogs.txt");
    $("#refresh").click(function() {
        $(".eventlogs").load("logs/PiCamLogs.txt");
    });
});