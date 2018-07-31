$(".more").click(
function (){
$(this).next().toggle("slow", function(){});
}
);

$(".less").click(
function (){
$(this).parent().hide("slow", function(){});
}
);
