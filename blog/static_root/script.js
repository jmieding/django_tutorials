$(document).ready(function() {
	"use strict";
  
  var url = window.location.href;
  $('.navbar-nav a').each(function() {
    if (url == (this.href)) {
      $(this).addClass('tab-nav-button');
    }
  });

  if (url.indexOf('index') > -1) {
    $('article').css('background', 'none');
  };
});