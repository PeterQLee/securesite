$(document).ready(function() {
    //$("#refresh").hide();
    $(".eventlogs").load("logs/maccamLogs.txt");
    $("#refresh").click(function() {
        $(".eventlogs").load("logs/maccamLogs.txt");
    });
});
