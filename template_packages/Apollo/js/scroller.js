			 
$(function()
{
	var _sTop=0;
	$(window).scroll(function(){
		_sTop=$(this).scrollTop();
		if(_sTop>=1){
			$(".header").css({"max-width":"1080px", "margin": "0 auto", "position":"relative"});
			$("header").css({"position":"fixed", "border-bottom": "1px solid rgba(0, 0, 0, 0.1)", "border-top-right-radius": "3px", "border-top-left-radius": "3px", "opacity": "1","background-color": "#fff", "z-index": "20", "height": "60" });
			
		}else{
			$("header").css({"position":"absolute", "border-color": "none", "border-bottom": "none","background-color": "transparent", "z-index": "1", "height": "60"});
		}	
	});
})