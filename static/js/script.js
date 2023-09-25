$(document).ready(function(){
    // Toggle task details on click
    $(".task-item").click(function(){
        $(this).find(".task-details").slideToggle();
    });
});

function validateForm(){
    var title = document.forms["taskForm"]["title"].value;

    if (title.length < 5){
        alert("Title must be at least 5 characters long.")
        return false
    }

    // Add other validations rules as needed


}