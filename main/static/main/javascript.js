
function zoomin() {
  var GFG = document.getElementById("image1");
  var currWidth = GFG.clientHeightWidth;
  GFG.style.width = (currWidth + 100) + "px";
}

function zoomout() {
  var GFG = document.getElementById("image1");
  var currWidth = GFG.clientWidth;
  GFG.style.width = (currWidth - 100) + "px";
}