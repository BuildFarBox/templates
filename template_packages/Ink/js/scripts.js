/* search function */
function search() {
    if (document.getElementById('search-bar').value) {
        location.href = 'http://' + location.host + '?s=' + document.getElementById('search-bar').value
    }
    else {
        return false;
    }
}

/* search bar toggle */
$(document).ready(function () {
    $(".sidebar #search").click(function () {
        $(".sidebar .search-bar").slideToggle("250");
        $(".sidebar #search a").toggleClass("selected");
        $("#search-bar").focus();
    });

    if (location.search.indexOf('?s=')==0){
        $(".sidebar #search").click()
    }
});

/* responsive menu */
$(document).ready(function () {
    $("#switch").click(function () {
        $(".nav").slideToggle("250");
        $("#switch").toggleClass("switch_current");
    });
    $(window).resize(function () {
        if ($(window).width() > 768)
            $(".nav").show();
    });
    $(window).resize(function () {
        if ($(window).width() < 768)
            $(".nav").hide();
    });
});


/* smooth scroll */
$(function () {
    $('a[href*=#]:not([href=#])').click(function () {
        if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
            var target = $(this.hash);
            target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
            if (target.length) {
                $('html,body').animate({
                    scrollTop: target.offset().top
                }, 250);
                return false;
            }
        }
    });
});