function load_checks()
{
	var date=new Date();
	date.setUTCHours(13);
	document.getElementById("time").innerHTML=date.getHours()+':'+date.getUTCMinutes()+' Τοπική Ώρα';
}
