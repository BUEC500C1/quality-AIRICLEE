from ArabToRome import transform_AtoR

def test_transform_AtoR_pass():
	assert transform_AtoR(77) == "LXXVII"
	assert transform_AtoR(66) == "LXVI"
	assert transform_AtoR(55) == "LV"
	assert transform_AtoR(8) == "VIII"
	assert transform_AtoR(1200) == "MCC"
	assert transform_AtoR(34) == "XXXIV"
	assert transform_AtoR(65) == "LXV"
	assert transform_AtoR(3) == "III"
	assert transform_AtoR(21) == "XXI"
	assert transform_AtoR(99) == "XCIX"
	assert transform_AtoR(40) == "XL"
	assert transform_AtoR(3999) == "MMMCMXCIX"
	assert transform_AtoR(4000) == "MMMM"
	assert transform_AtoR(0) == "Negative or Zero, Please input positive number"
	assert transform_AtoR(-1) == "Negative or Zero, Please input positive number"
	assert transform_AtoR(3.5) == "Invalid value, Please input int type"
	assert transform_AtoR("asd") == "Invalid value, Please input int type"

def test_transform_AtoR_failed():
	assert transform_AtoR(999) == "XA"
	assert transform_AtoR("ASD") == "MML"
	assert transform_AtoR(3.5) == "III"
	assert transform_AtoR(-2) == "VIII"
	assert transform_AtoR(0) == "0"
