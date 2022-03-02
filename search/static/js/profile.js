const imageSlider = document.querySelectorAll(".review-box")

const next = document.querySelector("span.next")
const prev = document.querySelector("span.prev")

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