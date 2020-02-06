/*
Jun Tao Lei
SoftDev1 pd9
K04 -- Das Canvas
2020-02-05
*/

let mode = 'box';
let xcor, ycor;
let isDrawing = false;

const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
ctx.fillStyle = 'blue';

document.getElementById('clear').addEventListener(
  'click',
  _ => clear()
);
document.getElementById('switch').addEventListener(
  'click',
  e => switchMode(e)
);

canvas.addEventListener(
  'mousedown',
  e => {
    if (!isDrawing) {
      let { x, y } = adjustMousePositions(e);
      xcor = x;
      ycor = y;
      isDrawing = true;
    }
  }
);

canvas.addEventListener(
  'mouseup',
  e => {
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
  let { x, y } = adjustMousePositions(e);
  switch (mode) {
    case 'dot':
      ctx.beginPath();
      ctx.arc(
        xcor,
        ycor,
        Math.sqrt(Math.pow((x - xcor), 2) + Math.pow((y - ycor), 2)) / 2,
        0,
        2 * Math.PI
      );
      ctx.fill();
      ctx.stroke();
      break;
    default:
      ctx.fillRect(xcor, ycor, x - xcor, y - ycor);
      break;
  }
};

const adjustMousePositions = e => {
  let rect = canvas.getBoundingClientRect();
  return {
    x: (e.clientX - rect.left) / (rect.right - rect.left) * canvas.width,
    y: (e.clientY - rect.top) / (rect.bottom - rect.top) * canvas.height
  };
};