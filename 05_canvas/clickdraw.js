/*
Jun Tao Lei
SoftDev1 pd9
K05 -- Canvas Again
2020-02-06
*/

let mode = 'box';
let xcor, ycor;
let isDrawing = false;

const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
ctx.fillStyle = 'blue';

document.getElementById('clear').addEventListener(
  'click',
  e => {
    // It signals to the event operation that it needs to be canceled.
    e.preventDefault();
    clear();
  }
);
document.getElementById('switch').addEventListener(
  'click',
  e => {
    // It signals to the event operation that it needs to be canceled.
    e.preventDefault();
    switchMode(e);
  }
);

canvas.addEventListener(
  'mousedown',
  e => {
    // It signals to the event operation that it needs to be canceled.
    e.preventDefault();
    if (!isDrawing) {
      // It provides the offset in the X coordinate of the mouse pointer between that event and the padding edge of the target HTML element.
      xcor = e.offsetX;
      // It provides the offset in the Y coordinate of the mouse pointer between that event and the padding edge of the target HTML element.
      ycor = e.offsetY;
      isDrawing = true;
    }
  }
);

canvas.addEventListener(
  'mouseup',
  e => {
    // It signals to the event operation that it needs to be canceled.
    e.preventDefault();
    if (isDrawing) {
      draw(e);
      isDrawing = false;
    }
  }
);

const clear = _ => {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
};

const switchMode = e => {
  switch (mode) {
    case 'box':
      document.getElementById('switch').innerHTML = 'Switch to Draw-a-Rectangle Mode';
      mode = 'dot';
      break;
    default:
      document.getElementById('switch').innerHTML = 'Switch to Draw-a-Dot Mode';
      mode = 'box';
      break;
  }
};

const draw = e => {
  switch (mode) {
    case 'dot':
      // It discards the old list of sub-paths, and prepares for a new path to allow for drawing.
      ctx.beginPath();
      ctx.arc(
        xcor,
        ycor,
        Math.sqrt(Math.pow((e.offsetX - xcor), 2) + Math.pow((e.offsetY - ycor), 2)),
        0,
        2 * Math.PI
      );
      ctx.fill();
      ctx.stroke();
      break;
    default:
      ctx.fillRect(xcor, ycor, e.offsetX - xcor, e.offsetY - ycor);
      break;
  }
};