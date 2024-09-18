import testbed1.api

def fillTestStructBool(test_struct_bool):
	test_struct_bool.field_bool = True;
	return test_struct_bool

def fillTestStructInt(test_struct_int):
	test_struct_int.field_int = 1;
	return test_struct_int

def fillTestStructFloat(test_struct_float):
	test_struct_float.field_float = 1.1;
	return test_struct_float

def fillTestStructString(test_struct_string):
	test_struct_string.field_string = "xyz";
	return test_struct_string
