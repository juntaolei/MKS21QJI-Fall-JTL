let fibsequence = [0, 1], current = 0;

const changeHeading = e => { document.getElementById("h").innerHTML = e; };

const removeItem = e => { e.remove(); };

Array.from(document.getElementsByTagName("li")).forEach(
  i => {
    i.addEventListener("mouseover", () => changeHeading(i.innerHTML));
    i.addEventListener("mouseout", () => changeHeading("Hello World!"));
    i.addEventListener("click", () => removeItem(i));
  }
);

const addItem = () => {
  let item = document.createElement("li");
  item.innerHTML = "WORD";
  item.addEventListener("mouseover", () => changeHeading(item.innerHTML));
  item.addEventListener("mouseout", () => changeHeading("Hello World!"));
  item.addEventListener("click", () => removeItem(item));
  document.getElementById("thelist").appendChild(item);
};

const fib = n => {
  if (n < 2) return 1;
  return fib(n - 1) + fib(n - 2);
}

const fibonacci = (n, m = fibsequence) => {
  if (n >= m.length)
    m[n] = fibonacci(n - 1) + fibonacci(n - 2);
  return m[n];
};

const addFib = current => {
  let item = document.createElement("li");
  item.addEventListener("mouseover", () => changeHeading(item.innerHTML));
  item.addEventListener("mouseout", () => changeHeading("Hello World!"));
  item.addEventListener("click", () => removeItem(item));
  item.innerHTML = fib(current);
  document.getElementById("fiblist").appendChild(item);
};

const addFib2 = current => {
  let item = document.createElement("li");
  item.addEventListener("mouseover", () => changeHeading(item.innerHTML));
  item.addEventListener("mouseout", () => changeHeading("Hello World!"));
  item.addEventListener("click", () => removeItem(item));
  item.innerHTML = fibonacci(current);
  document.getElementById("fiblist").appendChild(item);
};

document.getElementById("b").addEventListener("click", () => addItem());
document.getElementById("fb").addEventListener("click", () => addFib2(current++));