document.getElementById("title").innerHTML = "Hans Bacca";
document.getElementById("footer").innerHTML = "Copyright Hans Bacca 2018 &copy;";

var navLink = [
"blog1.html",
"blog2.html",
"blog3.html",
"blog4.html",
"blog5.html"
];

var navName = [
"Blog 1",
"Blog 2",
"Blog 3",
"Blog 4",
"Blog 5"
];

var i;
for(var i = 0 ; i < navLink.length ; i++)
{
  var link = document.createElement("a");
  var node = document.createTextNode(navName[i]);
  link.appendChild(node);

  link.href=navLink[i];

  var para = document.createElement("li");
  para.appendChild(link);

  if(navName[i] === titleName)
    para.id="selected";

  var element = document.getElementById("navContainer");
  element.appendChild(para);
}
