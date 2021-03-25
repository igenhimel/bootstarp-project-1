$(document).ready(function () {
    $(".features-1").owlCarousel({
       
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
               items:3
           },
           1200:{
               items:3
           }
       },
       smartSpeed:400

    });



    $(".apps-ss").owlCarousel({
       
        autoplay:false,
        loop:true,
        items:4,
        margin:0,
        responsiveClass:true,
        responsiveRefreshRate:true,
        responsive:{
            0:{
                items:1,
                autoplay:true
            },
 
            768:{
                items:2,
                autoplay:true
            },
            992:{
                items:3,
                autoplay:true
            },
            1200:{
                items:4
            }
        },
        smartSpeed:400
 
     });

     $(".client-carousel").owlCarousel({
       
        autoplay:false,
        loop:true,
        items:3,
        margin:0,
        responsiveClass:true,
        responsiveRefreshRate:true,
        responsive:{
            0:{
                items:1,
                autoplay:true
            },
 
            768:{
                items:2,
                autoplay:true
            },
            992:{
                items:3,
                autoplay:true
            },
           
        },
        smartSpeed:400
 
     });

   
});