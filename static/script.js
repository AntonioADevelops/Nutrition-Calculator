$(document).ready(function(){
    n=1
    $(document).on("click", "#add", function() {
        $("#append").append("<input class=\"ingredient\" list=\"food\" onfocus=\"this.value=''\" id=\"ingredient" + n + "\"> <input type=\"number\" step=\".01\" min=0 id=\"amount" + n +"\" name=\"amount\" onfocus=\"this.value=''\"> <br id=\"break" + n + "\">")
        n++
    });
    $("#remove").click(function() {
        n--
        $("#ingredient" + n).remove()
        $("#amount" + n).remove()
        $("#break" + n).remove()
        if (n<=0)
            n=0;
    });
});