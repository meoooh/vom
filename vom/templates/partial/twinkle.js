function twinkle(target){
	var opa = $(target).css("opacity");

	//console.log($("g."+target).css("opacity"));

	if(twinkleSwitch){
		$(target).css("opacity", parseFloat(opa) - 0.1);

		if($(target).css("opacity") < 0.1){
			twinkleSwitch = false;
		}
	}
	else{
		$(target).css("opacity", parseFloat(opa) + 0.1);

		if($(target).css("opacity") == 1){
			twinkleSwitch = true;
		}
	}
}