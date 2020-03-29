let x_, y_;

const btn = document.getElementById('btn');
const svg = document.getElementById('svg-dot');

const clear = _ => svg.innerHTML = '';

const drawCircle = (cx, cy, r) => {
  const circle = document.createElementNS(
    'http://www.w3.org/2000/svg', 'circle'
  );
  circle.setAttributeNS(null, 'cx', cx);
  circle.setAttributeNS(null, 'cy', cy);
  circle.setAttributeNS(null, 'r', r);
  svg.appendChild(circle);
};

const drawLine = (x0, y0, x1, y1) => {
  const line = document.createElementNS(
    'http://www.w3.org/2000/svg', 'line'
  );
  line.setAttributeNS(null, 'x1', x0);
  line.setAttributeNS(null, 'y1', y0);
  line.setAttributeNS(null, 'x2', x1);
  line.setAttributeNS(null, 'y2', y1);
  line.setAttribute('stroke', 'purple');
  svg.appendChild(line);
}

btn.addEventListener(
  'click',
  e => {
    e.preventDefault();
    clear();
  }
)

svg.addEventListener(
  'click',
  e => {
    e.preventDefault();
    drawCircle(e.offsetX, e.offsetY, 10);
    if (x_ !== undefined || y_ !== undefined) {
      drawLine(x_, y_, e.offsetX, e.offsetY);
    }
    x_ = e.offsetX;
    y_ = e.offsetY;
  }
);