var arr = document.getElementsByClassName("arrow");
var i;

for (i=0; i < arr.length; i++){
arr[i].addEventListener('click', function(event) {
  event.target.classList.toggle('down');
})};