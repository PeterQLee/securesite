console.log("dfd")
$.ajax({dataType:"json",url:"cameras.json",mimeType:"application/json",success:function(data) {
    
    var st="";
    for (var i=0;i<data.length;i++) {
	st+="<input type='radio' name='camera' value ="+data[i]+">"+data[i]+"<br>";
    }
    if (data.length==0) {
	st+="<br><b>No Cameras are registered!</b>";
    }
    console.log(st)
    //document.write(st)
    document.getElementById("camlist").innerHTML=st;
    document.getElementById("camlist2").innerHTML=st;
    
    
}});
