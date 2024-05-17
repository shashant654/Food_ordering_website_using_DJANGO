const container = document.querySelector(".container");
const minus = document.querySelector(".minus-box");
var amount = document.getElementById("amount");
var plus = document.querySelector(".plus-box");
var stock = document.querySelector(".stock");
const checkoutBtn = document.querySelector(".gift");
const promoBox = document.querySelector(".promo-box");
const promoInput = document.getElementById("promo");
const sendPromoBtn = document.querySelector(".send-promo");
const promoApplied = document.querySelector(".applied");
var price = document.getElementById("price");

var vatall = document.querySelectorAll(".VAT");

function totalPrice() {
  var nok = document.querySelector(".NOK");
  tp = 0;
  vatall.forEach((vats) => {
    tp += parseInt(vats.innerHTML);
  });
  console.log(tp);
  nok.innerHTML = tp;
}

let vatValueDefault = 0;
let nokValueDefault = 0;

let free = false;
console.log(price.value);

function plusf(e) {
  console.log(e);
  var cartnumber = e.getAttribute("data");
  console.log(cartnumber);
  var amount = document.querySelector(cartnumber + " #amount");
  var price = document.querySelector(cartnumber + " #price");
  var stock = document.querySelector(cartnumber + " .stock");
  var vat = document.querySelector(cartnumber + " .VAT");
  // var nok = document.querySelector(cartnumber + " .NOK");
  console.log(amount);
  console.log(price);
  if (amount.value < 10) {
    amount.value++;
    if (amount.value !== 0 && free === false) {
      vat.innerHTML = `${price.value * amount.value},-`;
      // nok.innerHTML = `${price.value * amount.value},-`;
    }
  }
  if (amount.value == 10) {
    stock.style.backgroundColor = "#BE3144";
    stock.innerHTML = "out of stock";
  }
  totalPrice();
}
function minusf(e) {
  console.log(e);
  var cartnumber = e.getAttribute("data");
  console.log(cartnumber);
  var amount = document.querySelector(cartnumber + " #amount");
  var price = document.querySelector(cartnumber + " #price");
  var stock = document.querySelector(cartnumber + " .stock");
  var vat = document.querySelector(cartnumber + " .VAT");
  // var nok = document.querySelector(cartnumber + " .NOK");
  if (amount.value > 0) {
    amount.value--;
    if (amount.value !== 0 && free === false) {
      vat.innerHTML = `${price.value * amount.value},-`;
      // nok.innerHTML = `${price.value * amount.value},-`;
    }
  }
  stock.style.backgroundColor = "#83bd46";
  stock.innerHTML = "In stock";
  totalPrice();
}
totalPrice();

// plus.addEventListener("click", () => {

//   if (amount.value < 10) {
//     amount.value++;
//     if (amount.value !== 0 && free === false) {
//       vat.innerHTML = `${price.value * amount.value},-`;
//       nok.innerHTML = `${price.value * amount.value},-`;
//     }
//   }
//   if (amount.value == 10) {
//     stock.style.backgroundColor = "#BE3144";
//     stock.innerHTML = "out of stock";
//   }
// });

// minus.addEventListener("click", () => {
//   if (amount.value > 0) {
//     amount.value--;
//     if (amount.value !== 0 && free === false) {
//       vat.innerHTML = `${price.value * amount.value},-`;
//       nok.innerHTML = `${price.value * amount.value},-`;
//     }
//   }
//   stock.style.backgroundColor = "#83bd46";
//   stock.innerHTML = "In stock";
// });

checkoutBtn.addEventListener("click", () => {
  if (!promoInput.classList.contains("applied")) {
    container.style.opacity = ".5";
    container.style.pointerEvents = "none";
    promoBox.style.opacity = "1";
    promoBox.style.display = "flex";
  }
});
sendPromoBtn.addEventListener("click", () => {
  if (promoInput.value.length >= 1) {
    container.style.opacity = "1";
    container.style.pointerEvents = "auto";
    promoBox.style.opacity = "0";
    promoBox.style.display = "none";
    promoInput.classList.add("applied");
    promoApplied.style.opacity = "1";
    promoApplied.style.display = "block";
    vat.innerHTML = `It's free for you`;
    nok.innerHTML = `It's free for you`;
    free = true;
  }
});
