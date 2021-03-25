$(document).ready(function () {
    $(".owl-carousel").owlCarousel({
       
       autoplay:true,
       loop:true,
       items:3,
       responsiveClass:true,
       responsiveRefreshRate:true,
       responsive:{
           0:{
               items:1
           },

           768:{
               items:2
           },
           992:{
               items:2
           },
           1200:{
               items:3
           }
       },
       smartSpeed:400

    });
});