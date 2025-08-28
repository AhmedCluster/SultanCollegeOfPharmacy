window.onload = function() {
    var sliderWrapper = document.getElementById('intro-slider-wrapper');
    var preloader = document.getElementById('preloader');
    
    if (sliderWrapper) {
        sliderWrapper.className = 'onload-class';
    }
    
    if (preloader) {
        preloader.className = 'display-none';
    }
};
