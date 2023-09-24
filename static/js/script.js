$(document).ready(function(){
    $(".task-block").click(function(){
        $(this).next(".task-details").slideToggle();
    });
});