$(document).ready(function(){
    // Initially hide all task details
    $(".task-details").hide();

    // Toggle task details on click
    $(".task-item").click(function(){
        // Slide up any open task details except the one in the clicked task item
        $(".task-details").not($(this).find(".task-details")).slideUp();

        // Slide toggle the task details in the clicked task item
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