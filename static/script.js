$(document).ready(function(){
    $(document).on("click", "#add", function(){
        $(".append").append("<input class=\"ingredient\" list=\"food\"> <input class=\"amount\" name=\"amount\"><br>")
    });
    $(document).on("click", "#remove", function(){
        $(".append").remove("<input class=\"ingredient\" list=\"food\"> <input class=\"amount\" name=\"amount\"><br>")
    });
    $(".ingredient").on("click", function() {
        $("input[name=ingredient]").val("")
    });
});