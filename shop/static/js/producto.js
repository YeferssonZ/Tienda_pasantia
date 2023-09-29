document.addEventListener("DOMContentLoaded", function () {
    const carouselContainer = document.querySelector("#productosRelacionadosCarousel");
    const carouselPrevBtn = carouselContainer.querySelector(".carousel-control-prev");
    const carouselNextBtn = carouselContainer.querySelector(".carousel-control-next");

    carouselContainer.addEventListener("mouseenter", function () {
        carouselPrevBtn.style.visibility = "visible";
        carouselNextBtn.style.visibility = "visible";
    });

    carouselContainer.addEventListener("mouseleave", function () {
        carouselPrevBtn.style.visibility = "hidden";
        carouselNextBtn.style.visibility = "hidden";
    });
});