document.getElementById("title").innerHTML = "Hans Bacca";
document.getElementById("footer").innerHTML = "Copyright Hans Bacca 2018 &copy;";

nameList=["Linux Ubuntu",
          "CUDA 9.0",
          "OpenCV 3.4.0",
          "Rpi Setup",
          "PPB Detection",
		  "Invisible Tripwire Alarm"]

addressList=["linux_ubuntu.html",
              "cuda_installation.html",
              "opencv_installation.html",
              "ssh_rpi.html",
              "portable_ppb_detection.html",
			  "invisible-tripwire-alarm.html"]



for(var i = 0 ; i < nameList.length ; i++)
{
  var link = document.createElement("a");
  var node = document.createTextNode(nameList[i]);
  link.appendChild(node);

  link.href=addressList[i];

  var para = document.createElement("li");
  para.appendChild(link);

  var element = document.getElementById("navContainer");
  element.appendChild(para);
}
