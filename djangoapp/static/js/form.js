$(document).ready(function () {
    
    $("#addButton").click(function () {
        var newDiv = '<div class="form-row mt-3">' +
            '<div class="col"><input type="text" class="form-control" placeholder="Course" name="course"></div>' +
            '<div class="col"><input type="text" class="form-control" placeholder="University" name="university"></div>' +
            '<div class="col"><input type="text" class="form-control" placeholder="Year" name="year"></div>' +
            '<input type="button" value="-" class="remove-btn"></div>';
        $(".loop").append(newDiv);
    });
    $(document).on("click", ".remove-btn", function () {
        $(this).closest(".form-row").remove();
    });
});
