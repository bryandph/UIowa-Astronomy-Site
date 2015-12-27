var jumboHeight = $('.homejumbo').outerHeight();
function parallax(){
    var scrolled = $(window).scrollTop();
    $('.homebg').css('height', (jumboHeight-scrolled) + 'px');
}

$(window).scroll(function(e){
    parallax();
});