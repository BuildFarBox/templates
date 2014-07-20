
@search = ->
    if document.getElementById('search_value').value
        location.href='http://'+location.host+'?s='+document.getElementById('search_value').value
    return false


$(document).ready ->
    bt = $('#back_to_top')
    if $(document).width() > 480
        $(window).scroll ->
            st = $(window).scrollTop()
            if st > 30
                bt.css('display', 'block')
            else
                bt.css('display', 'none')
        $('.back-to a').click ->
             $('body,html').animate({scrollTop: 0 }, 800)
             return false