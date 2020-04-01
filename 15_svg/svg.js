let id, dr = 1, circlev = [];
const svg = document.getElementById('svg-dot');
const colors = ['red', 'green', 'blue', 'lightred', 'lightgreen', 'lightblue', 'yellow', 'lightyellow', 'purple'];

const drawCircle = (cx, cy, r, color) => {
  const circle = document.createElementNS(
    'http://www.w3.org/2000/svg', 'circle'
  );
  circle.setAttribute('cx', cx);
  circle.setAttribute('cy', cy);
  circle.setAttribute('r', r);
  circle.setAttribute('fill', color);
  circle.addEventListener('click', recolor);
  circlev.push([2, 3]);
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

const moveCircles = _ => {
  circles = document.getElementsByTagNameNS(
    'http://www.w3.org/2000/svg', 'circle'
  );
  [...circles].forEach(
    (circle, index) => {
      const cx = parseInt(circle.getAttribute('cx'));
      const cy = parseInt(circle.getAttribute('cy'));
      if (cy + circlev[index][1] >= 590 || cy + circlev[index][1] <= 0) {
        circlev[index][1] *= -1;
      } else if (cx + circlev[index][0] >= 590 || cx + circlev[index][0] <= 0) {
        circlev[index][0] *= -1;
      }
      circle.setAttribute('cx', cx + circlev[index][0]);
      circle.setAttribute('cy', cy + circlev[index][1]);
    }
  );
}

const move = _ => {
  moveCircles();
  id = window.requestAnimationFrame(move);
}

const xtra = _ => {
  circles = document.getElementsByTagNameNS(
    'http://www.w3.org/2000/svg', 'circle'
  );
  [...circles].forEach(
    circle => {
      let r = parseInt(circle.getAttribute('r'));
      if (r >= 50 || r <= 0) {
        dr *= -1;
      }
      circle.setAttribute('r', r + dr);
      if (r % 10 == 0) {
        circle.setAttribute('fill', colors[Math.floor(Math.random() * colors.length)]);
      }
    }
  );
  moveCircles();
  id = window.requestAnimationFrame(xtra);
}

document.getElementById('clear').addEventListener(
  'click',
  _ => {
    while (svg.hasChildNodes()) {
      svg.removeChild(svg.firstChild);
    }
  }
);

document.getElementById('move').addEventListener(
  'click',
  _ => {
    window.cancelAnimationFrame(id);
    id = window.requestAnimationFrame(move);
  }
)

document.getElementById('stop').addEventListener(
  'click',
  _ => {
    id = window.cancelAnimationFrame(id);
  }
)

document.getElementById('xtra').addEventListener(
  'click',
  _ => {
    window.cancelAnimationFrame(id);
    id = window.requestAnimationFrame(xtra);
  }
)

svg.addEventListener(
  'click',
  e => {
    drawCircle(e.offsetX, e.offsetY, 10, 'purple');
  }
);