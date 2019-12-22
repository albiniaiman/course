let slideIndex = 0;
let slideIndex1 = 1;
let slideIndex2 = 1;
function dot_slide(n){
	
			
	showDot_slide(slideIndex2=n);	
}
function plusSlides(n){
	
			
  showSlides_1(slideIndex1 += n);
 
}

function showDot_slide(n){
	 let i;
	 let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("dot");
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";  
  } 
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active1", "");
  }
  slides[slideIndex2-1].style.display = "block";  
  dots[slideIndex2-1].className += " active1";
  slideIndex=slideIndex2;
  slideIndex1=slideIndex2;
 }
function showSlides_1(n) {
 let i;
 let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex1= 1}    
  if (n < 1) {slideIndex1 = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";  	
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active1", "");
  }
  slides[slideIndex1-1].style.display = "block";  
  dots[slideIndex1-1].className += " active1";
  slideIndex=slideIndex1;
}

function showSlides() {
 
	  let i;
    let slides = document.getElementsByClassName("mySlides");
    let dots = document.getElementsByClassName("dot");
	 
     for (i = 0; i < slides.length; i++) {
       slides[i].style.display = "none";  
}
    slideIndex++;
    if (slideIndex > slides.length) {slideIndex = 1}    
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active1", "");
    }
	
    slides[slideIndex-1].style.display = "block";  
    dots[slideIndex-1].className += " active1";
	 	
	  setTimeout(showSlides, 4000); // Change image every 2 seconds
	
}	

	showSlides();
 showDot_slide(slideIndex2);
  showSlides_1(slideIndex1);