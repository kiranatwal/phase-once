// /* If you're feeling fancy you can add interactivity
//     to your site with Javascript */
//
// // prints "hi" in the browser's dev tools console
// console.log('hi');
//
// const redButton = document.querySelector('#red');
//
// // Use addEventListener to respond to a click event.
// redButton.addEventListener('click', (e) => {
//   console.log("You clicked the red button!");
//   responsebox.style.backgroundColor = "red";
//   responsebox.innerHTML = "red";
//
// });
//
// const greenButton = document.querySelector('#green');
//
// greenButton.addEventListener('click', (e) => {
//   console.log("You clicked the green button!");
//   responsebox.style.backgroundColor = "green";
//   responsebox.innerHTML += ", green";
//
// });

const landfill = document.querySelector('#landfill')
const blue = document.querySelector('#blue')
const green = document.querySelector('#green')
const red = document.querySelector('#red')
let trash = document.querySelector('#trash')

//Make the DIV element dragable:
dragElement(document.getElementById("mydiv"));

function dragElement(elmnt) {
  var pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;
  if (document.getElementById(elmnt.id + "header")) {
    /* if present, the header is where you move the DIV from:*/
    document.getElementById(elmnt.id + "header").onmousedown = dragMouseDown;
  } else {
    /* otherwise, move the DIV from anywhere inside the DIV:*/
    elmnt.onmousedown = dragMouseDown;
  }

  function dragMouseDown(e) {
    e = e || window.event;
    e.preventDefault();
    // get the mouse cursor position at startup:
    pos3 = e.clientX;
    pos4 = e.clientY;
    document.onmouseup = closeDragElement;
    // call a function whenever the cursor moves:
    document.onmousemove = elementDrag;
  }

  function elementDrag(e) {
    e = e || window.event;
    e.preventDefault();
    // calculate the new cursor position:
    pos1 = pos3 - e.clientX;
    pos2 = pos4 - e.clientY;
    pos3 = e.clientX;
    pos4 = e.clientY;
    // set the element's new position:
    elmnt.style.top = (elmnt.offsetTop - pos2) + "px";
    elmnt.style.left = (elmnt.offsetLeft - pos1) + "px";
  }

  function closeDragElement() {
    /* stop moving when mouse button is released:*/
    document.onmouseup = null;
    document.onmousemove = null;
  }
}
