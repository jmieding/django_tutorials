$(document).ready(function() {
	
  var url = window.location.href;
  var articles = document.getElementById('articles');

  if (url.indexOf('articles') !== -1) {
    $(articles).addClass('active');
  } else {
    $('.navbar-nav a').each(function() {
      if (url == (this.href)) {
        $(this).closest('li').addClass('active');
      }
    });
  };
});

  // $(".social-icons").hover(function() {
  //   $(this).animate({width: '2em'});
  // },
  // function(){
  //   $(this).animate({width: '2.25em'});
  // });
