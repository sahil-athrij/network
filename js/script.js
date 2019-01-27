


//if you are from cusat and you understand this please contact sahil athrij cs s5 or akul santhosh cs s5





sct = $(document).scrollTop();
function scrollVideo() {

            scrollPosition = $(document).scrollTop();


        if(stopped == "no" && sct-scrollPosition<0) {

            if (displayed == "no") {
                video.play();
                if (secc1animate == 0) {
                    removediv("#secc1", "#landscape");
                    secc1animate = 2;

                }

            }


            else if (displayed2 == "no") {
                video.play();
                if (secc2animate == 0) {

                    removediv("#secc2", "#mountains");
                    secc21animate = 2;

                }


            }

            else if (displayed3 == "no") {
                video.play()
                if (secc3animate == 0) {

                    removediv("#secc3", "#clouds");
                    secc3animate = 2;

                }
            }


            else if (displayed4 == "no") {
                video.play()
                if (secc4animate == 0) {

                    removediv("#secc4", "#clouds");
                    secc4animate = 2;

                }
            }
        }
        sct = scrollPosition;


}

$(window).scroll(function(e) {

        scrollVideo();
});


var stopped = "yes";
var displayed2 = "yes";
var displayed3 = "yes";
var displayed4 = "yes";
var displayed = "no";




var secc1animate = 1;
var secc2animate = 1;
var secc3animate = 1;
var secc4animate = 1;

var video = $('video').get(0);
video.addEventListener("timeupdate", function(){
    console.log(this.currentTime);
    if(this.currentTime >= .3 && this.currentTime<=.8){
    }


    else if(this.currentTime >= 1.0 && this.currentTime<=1.4) {
        if(secc2animate){
            secc2animate = 0;
            animatedivs("#secc2","#mountains")

        }


    }



    else if(this.currentTime >= 1.4 && this.currentTime<=1.7) {

        this.pause();
        displayed = "yes";
        displayed2 = "no";
    }



    else if(this.currentTime >= 3.0 && this.currentTime<=3.3){
        if(secc3animate){
            secc3animate = 0;
            animatedivs("#secc3","#clouds")

        }

    }

    else if(this.currentTime >= 3.3 && this.currentTime<=3.6){
        this.pause();
        displayed = "yes";
        displayed2 = "yes";
        displayed3 = "no";
    }

    else if(this.currentTime >= 4.6 && this.currentTime<=4.9){
        if(secc4animate){
            secc4animate = 0;
            animatedivs("#secc4","#clouds")

        }


    }

    else if(this.currentTime >= 5 && this.currentTime<=5.2){
        this.pause();
        displayed = "yes";
        displayed2 = "yes";
        displayed3 = "yes";
        displayed4 = "no";
    }

    else if(this.currentTime >= 7.1){
        this.pause();
        displayed = "yes";
        displayed2 = "yes";
        displayed3 = "yes";
        displayed4 = "yes";
        stopped = "yes";

        $("#navbar").animate({
          opacity:1,
          
        },1000);

        $("#clockdiv").animate({
            top: "60%",

        }, 500);

        $("#box").animate({
            opacity:.8,
            height:'250px',
            width:'250px'

        }, 500);

        $('.scroll').animate({
            opacity:0
        });





    }


});



function deletediv(){

    var del = document.getElementById("begin");
    del.remove();

    $('#logo').animate({
        width:"70%",
        height:"70%",
        opacity:0

    },400,function () {
        del = document.getElementById("logo");
        del.remove();

    });


    $('#hider').animate({

        opacity:0

    },500,function () {
        del = document.getElementById("hider");
        del.remove();

    });


    //del.remove();
    video.pause();
    $(".loading").animate({
        opacity:1,

    },1000);


    if(secc1animate){
        secc1animate = 0;
        animatedivs("#secc1","#landscape")

    }


    $('.emailpng').animate({
        opacity:1
    });

    $('.scroll').animate({
        opacity:.7
    });


    stopped = "no";

}

video.addEventListener('loadeddata', function() {


    video.pause();



});


function animatedivs(divid,imgid){

    if (screen.width >= 600) {
        $(divid).animate({
            top: "40%",
            opacity:1


        }, 800);

        addBlur();

    }
    else {
        $(divid).animate({
            opacity:1


        }, 800);
    }






    $(imgid).animate({
        bottom:"0px",
        opacity:1,


    }, 900)


}


function removediv(divid,imgid) {
    $(divid).animate({
        top: "-20%",
        opacity:0


    }, 500);

    $(imgid).animate({
        bottom:"-400px",
        opacity:0


    }, 500);

    if (screen.width >= 600) {
        removeBlur();
    }

}

function addBlur()
{

    $('video').css("-webkit-filter" ,"blur(5px) brightness(85%)");
    $('video').css("-moz-filter" ,"blur(5px)");
    $('video').css("-ms-filter" ,"blur(5px)");

}

function removeBlur(){
    $('video').css("-webkit-filter" ,"blur(0px) brightness(100%)");
    $('video').css("-moz-filter" ,"blur(0px)");
    $('video').css("-ms-filter" ,"blur(0px)");
}