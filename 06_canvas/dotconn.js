/*
 * Jun Tao Lei
 * SoftDev1 pd9
 * K06 -- DotCanvas
 * 2020-02-11
 */

let dotDrawn = false;
let originalDotX, originalDotY;

const canvas = document.getElementById('playground');
const ctx = canvas.getContext('2d');
ctx.fillStyle = 'blue';

document.getElementById('clear').addEventListener(
	'click',
	e => {
		e.preventDefault()
		ctx.clearRect(0, 0, canvas.width, canvas.height);
		dotDrawn = false;
	}
);

canvas.addEventListener(
	'click',
	e => {
		e.preventDefault();
		if (!dotDrawn) {
			dotDrawn = true;
			drawDot(e);
		} else {
			drawDot(e);
			ctx.beginPath();
			ctx.moveTo(e.offsetX, e.offsetY);
			ctx.lineTo(originalDotX, originalDotY);
			ctx.stroke();
		}
		originalDotX = e.offsetX;
		originalDotY = e.offsetY;
	}
)

const drawDot = e => {
	ctx.beginPath();
	ctx.arc(e.offsetX, e.offsetY, 10, 0, 2 * Math.PI);
	ctx.fill();
	ctx.stroke();
}
