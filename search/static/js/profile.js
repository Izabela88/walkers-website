const imageSlider = document.querySelectorAll(".review-box")

const next = document.querySelector("a.next")
const prev = document.querySelector("a.prev")

let slidCount = 0 

next.addEventListener("click", () => {
    imageSlider[slidCount].style.animationName = "firstNext"

    if (slidCount >= imageSlider.length - 1) {
        slidCount = 0
    } else {
        slidCount++
    }

    imageSlider[slidCount].style.animationName = "secondNext"
    
})

prev.addEventListener("click", () => {
    imageSlider[slidCount].style.animationName = "firstPrev"
    if (slidCount === 0) {
        slidCount =  imageSlider.length - 1
    } else {
        slidCount--
    }
    

    imageSlider[slidCount].style.animationName = "secondPrev"
    
})


// ---------------------------------------------------------
const pricesSlider = document.querySelectorAll(".prices-box")

const pricesNext = document.querySelector("a.prices-next")
const pricesPrev = document.querySelector("a.prices-prev")

let slidPricesCount = 0 

pricesNext.addEventListener("click", () => {
    pricesSlider[slidPricesCount].style.animationName = "firstPricesNext"

    if (slidPricesCount >= pricesSlider.length - 1) {
        slidPricesCount = 0
    } else {
        slidPricesCount++
    }

    pricesSlider[slidPricesCount].style.animationName = "secondPricesNext"
    
})

pricesPrev.addEventListener("click", () => {
    pricesSlider[slidPricesCount].style.animationName = "firstPricesPrev"
    if (slidPricesCount === 0) {
        slidPricesCount =  pricesSlider.length - 1
    } else {
        slidPricesCount--
    }
    

    pricesSlider[slidPricesCount].style.animationName = "secondPricesPrev"
    
})

const openPricesButton = document.querySelector('#open-prices');
const closePrices = document.querySelector('.close-prices');
const formPrices = document.querySelector('#prices-form');
// / Function opens Prices
function openPrices() {
  let showPricesWindow = document.querySelector('.prices-wrapper');
  showPricesWindow.classList.toggle('show-prices');
}

openPricesButton.addEventListener('click', openPrices);
closePrices.addEventListener('click', openPrices);