$(document).ready(function(){
    n=1
    $(document).on("click", "#add", function() {
        $("#append").append("<input class=\"ingredient\" list=\"food\" onfocus=\"this.value=''\" id=\"ingredient" + n + "\"> <input type=\"number\" class=\"amount\" onfocus=\"this.value=''\" id=\"amount" + n + "\"></br>")
        n++
    });
    $(document).on("click", "#remove", function() {
        $("#append").remove(".ingredient")
        $("#append").remove(".amount")
    });
    // function add() {
    //     var add = document.getElementById("append")
    //     const node = document.createElement("p");
    //     const textnode = document.createTextNode("Water");
    //     node.appendChild(textnode);
    //     add.appendChild(node);
    // }
});