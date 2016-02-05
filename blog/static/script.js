$(document).ready(function() {
	"use strict";
  var url = window.location.href;
  var articles = document.getElementById('articles');

  if (url.indexOf('articles') !== -1) {
    $(articles).addClass('tab-nav-button');
  } else {
    $('.navbar-nav a').each(function() {
      if (url == (this.href)) {
        $(this).addClass('tab-nav-button');
      }
    });
  };
});