let drawn = false;

const btn = document.getElementById('btn');
const svg = document.getElementById('svg-dot');

const clear = _ => {
  let fc = svg.firstChild;
  while (fc) {
    svg.removeChild(fc);
    fc = svg.firstChild;
  }
};

const drawCircle = (cx, cy, r, color) => {
  const circle = document.createElementNS(
    'http://www.w3.org/2000/svg', 'circle'
  );
  circle.setAttribute('cx', cx);
  circle.setAttribute('cy', cy);
  circle.setAttribute('r', r);
  circle.setAttribute('fill', color);
  circle.addEventListener('click', recolor);
  svg.appendChild(circle);
};

const recolor = e => {
  e.preventDefault();
  e.currentTarget.setAttribute('fill', 'lightblue');
  e.currentTarget.removeEventListener('click', recolor);
  e.currentTarget.addEventListener('click', destroy);
  e.stopImmediatePropagation();
};

const destroy = e => {
  e.preventDefault();
  e.currentTarget.removeEventListener('click', recolor);
  svg.removeChild(e.currentTarget);
  drawCircle(Math.random() * 500, Math.random() * 500, 10, 'purple');
  e.stopImmediatePropagation();
};

btn.addEventListener(
  'click',
  _ => {
    while (svg.hasChildNodes()) {
      svg.removeChild(svg.firstChild);
    }
  }
);

svg.addEventListener(
  'click',
  e => {
    drawCircle(e.offsetX, e.offsetY, 10, 'purple');
  }
);