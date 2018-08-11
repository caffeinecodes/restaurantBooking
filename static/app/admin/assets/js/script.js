// window height
var windowHeight = $(window).height();

// page load animation
$(window).on('load', function(){
	$(".se-pre-con").fadeOut("slow");
});



$(document).ready(function(){
	//Add category popup
  $("#selectbox").click(function () {
      if ($(this).val() == "#consumergoods") {	
          $('#consumergoods').modal('show');
        }
  });

  // menu bar collapse
  $("#nav1").hover(
      function() {
        $(this).find('ul').slideDown();
      },
      function() {
        $(this).find('ul').slideUp();
      });
  $("#header-dropdown-nav").hover(
      function() {
        $(this).find('ul').slideDown();
      },
      function() {
        $(this).find('ul').slideUp();
      });
  $(".goBack").click(function () {
        window.history.go(-1); 
        return false;
  });

  

});





