// Jun Tao Lei & Derek Leung
// SoftDev1 pd9
// K#28 -- <JSDOM/JavaScript & DOM/Change DOM with Javascript>
// 2019-12-11

const foo = () => {
  console.log("diagnostic info here");
};

const factorial = (n) => {
  if (n < 2) return 1;
  return n * factorial(n - 1);
};

const fibonacci = (n, x = 0, y = 1) => {
  if (n == 0) return x;
  return fibonacci(n - 1, y, x + y);
};

const gcd = (a, b) => {
  if (b == 0) return a;
  return gcd(b, a % b);
};

// 28_jsdom

const randomStudent = (n) => {
  return n[Math.floor(Math.random() * n.length)];
};

const gcdWrapped = (n) => {
  let [a, b] = n.split(",").map(i => i.trim());
  return gcd(a, b);
};

const randStudentWrapped = (n) => { return randomStudent(n.split(",").map(i => i.trim())); };

const attachButton = (ele, req, res, fxn) => {
  document.getElementById(ele).addEventListener(
    "click",
    () => {
      document.getElementById(res).innerHTML =
        `Result: ${fxn(document.getElementById(req).value)}`;
    }
  );
};

attachButton("factgo", "facterm", "factout", factorial);
attachButton("fibgo", "fibterm", "fibout", fibonacci);
attachButton("gcdgo", "gcdterm", "gcdout", gcdWrapped);
attachButton("randgo", "randin", "randout", randStudentWrapped);