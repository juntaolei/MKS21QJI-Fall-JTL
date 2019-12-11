const foo = () => {
  console.log("diagnostic info here")
}

const factorial = (n) => {
  if (n < 2) return 1;
  return n * factorial(n - 1);
}

const fibonacci = (n, x = 0, y = 1) => {
  if (n == 0) return x;
  return fibonacci(n - 1, y, x + y);
}

const gcd = (a, b) => {
  if (b == 0) return a;
  return gcd(b, a % b);
}

const randomStudent = (n) => {
  return n[Math.floor(Math.random() * n.length)];
}