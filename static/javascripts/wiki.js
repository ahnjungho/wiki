$(document).ready(function(){
  // font awesome external link
  $("a").each(function(index){
    if ($(this).attr('href').substring(0, 4) == 'http'){
      $(this).append('<i class="fa fa-external-link"></i>');
      $(this).attr('target', '_blank');
    }
  });
});
