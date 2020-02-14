/*
 * Jun Tao Lei
 * SoftDev1 pd9
 * K#08 -- Zoomers DVD  
 * 2020-02-13
 */

const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');

const dvd_logo = new Image();
dvd_logo.src = 'logo_dvd.jpg';

let id;
let r = 1, deltaR = 1;
let x = canvas.width / 2, y = canvas.height / 2, dx = 2, dy = 3;

document.getElementById('start').addEventListener(
	'click',
	_ => { 
		draw_circle();
	}
);

document.getElementById('dvd').addEventListener(
	'click',
	_ => {
		x = Math.floor(Math.random() * (canvas.width - 60));
		y = Math.floor(Math.random() * (canvas.height - 40));
		bounce_dvd();
	}

);

document.getElementById('stop').addEventListener(
	'click',
	_ => {
		window.cancelAnimationFrame(id);
	}
);

const draw_circle = _ => {
	window.cancelAnimationFrame(id);
	ctx.clearRect(0, 0, canvas.width, canvas.height);	
	if (r >= canvas.width / 2 || r <= 0) {
		deltaR *= -1;
	}
	ctx.beginPath();
	ctx.arc(canvas.width / 2, canvas.height / 2, r += deltaR, 0, 2 * Math.PI);
	ctx.closePath();
	ctx.fill();
	id = window.requestAnimationFrame(draw_circle);
};

const bounce_dvd = _ => {
	window.cancelAnimationFrame(id);
	ctx.clearRect(0, 0, canvas.width, canvas.height);
	if (y + dy >= canvas.height - 40 || y + dy <= 0) {
		dy *= -1;
	} else if (x + dx >= canvas.width - 60 || x + dx <= 0) {
		dx *= -1;
	}
	ctx.drawImage(dvd_logo, x, y, 60, 40);
	x += dx;
	y += dy;
	id = window.requestAnimationFrame(bounce_dvd);
}
