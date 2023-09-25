$(document).ready(function(){
    // Toggle task details on click
    $(".task-item").click(function(){
        $(this).find(".task-details").slideToggle();
    });
});