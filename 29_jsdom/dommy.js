let thefiblist = [0, 1], current = 0;

const lis = document.getElementsByTagName("li");

const lis2 = document.getElementById("fiblist");

const changeHeading = (e) => {
  document.getElementById("h").innerHTML = e;
};

const removeItem = (e) => {
  e.remove();
};

Array.from(lis).forEach(
  (i) => {
    i.addEventListener("mouseover", () => changeHeading(i.innerHTML));
    i.addEventListener("mouseout", () => changeHeading("Hello World!"));
    i.addEventListener("click", () => removeItem(i));
  }
);

const addItem = (e) => {
  let list = document.getElementById("thelist");
  let item = document.createElement("li");
  item.innerHTML = "WORD";
  item.addEventListener("mouseover", () => changeHeading(item.innerHTML));
  item.addEventListener("mouseout", () => changeHeading("Hello World!"));
  item.addEventListener("click", () => removeItem(item));
  list.appendChild(item);
};

document.getElementById("b").addEventListener("click", () => addItem());

const fib = (n) => {
  if (n < 2)
    return 1;
  return fib(n - 1) + fib(n - 2);
}

const fibonacci = (n, m = thefiblist) => {
  if (n >= m.length)
    m[n] = fibonacci(n - 1) + fibonacci(n - 2);
  return m[n];
};

const addFib = (e) => {
  // console.log(e);
  return fib(e);
};

const addFib2 = (e) => {
  // console.log(e);
  let thethefiblist = document.getElementById("fiblist");
  let item = document.createElement("li");
  item.innerHTML = fibonacci(current++);
  thethefiblist.appendChild(item);
};

document.getElementById("fb").addEventListener("click", () => addFib2());