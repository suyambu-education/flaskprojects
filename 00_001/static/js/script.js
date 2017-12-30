$(document).ready(function(){
			$('.menu').click(function(){
				$('ul').toggleClass('active');
			});
			$('nav ul li a').click(function () {
			     $('nav ul li a').removeClass();
			     $($(this).attr('href')).addClass('actives');
            });
		});