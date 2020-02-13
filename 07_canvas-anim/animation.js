/*
 * Jun Tao Lei
 * SoftDev1 pd9
 * K#07 -- Spasmic Black Hole
 * 2020-02-12
 */

const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');

let r = 1, deltaR = 1, id;

document.getElementById('start').addEventListener(
	'click',
	_ => { id = window.requestAnimationFrame(animate); }
);

document.getElementById('stop').addEventListener(
	'click',
	_ => window.cancelAnimationFrame(id)
);

const animate = _ => {
	ctx.clearRect(0, 0, canvas.width, canvas.height);	
	drawCircle();
	id = window.requestAnimationFrame(animate)
};

const drawCircle = _ => {
	if (r >= canvas.width / 2) {
		deltaR = -1;
	} else if (r <= 0) {
		deltaR = 1;
	}
	ctx.beginPath();
	ctx.arc(canvas.width / 2, canvas.height / 2, r += deltaR, 0, 2 * Math.PI);
	ctx.closePath();
	ctx.fill();
};

