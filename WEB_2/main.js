function httpGet(theUrl)
{
    var xmlHttp = XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false ); // false for synchronous request
    xmlHttp.send( null );
    return xmlHttp.responseText;
}
var a=httpGet('https://ap3.ragic.com/haisann/forms2/5?api=true');
console.log(a);
