console.log("dfd")
$.ajax({dataType:"json",url:"cameras.json",mimeType:"application/json",success:function(data) {
    
    var st="<ul class='nav navbar-nav'><li ><a href='index.html'>About</a></li><li id='addforum'><a href='forum.html'>Add Email</a></li>";
    for (var i=0;i<data.length;i++) {
	st+="<li id='"+data[i]+"'><a href='"+data[i]+".html'>"+ data[i]+ "</a></li>\n"
	
    }
    st+="</ul>"
    console.log(st)
    //document.write(st)
    document.getElementById("navbar").innerHTML=st;
    
}});
