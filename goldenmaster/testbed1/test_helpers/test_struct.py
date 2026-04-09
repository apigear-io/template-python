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

def fillTestStructStruct(test_struct_struct):
	test_struct_struct.field_string = fillTestStructString(testbed1.api.StructString());
	return test_struct_struct

def fillTestStructEnum(test_struct_enum):
	test_struct_enum.field_enum = testbed1.api.Enum0.VALUE1;
	return test_struct_enum

def fillTestStructBoolWithArray(test_struct_bool_with_array):
	local_field_bool_array = []
	elementfield_bool = True
	local_field_bool_array.append(elementfield_bool)
	test_struct_bool_with_array.field_bool = local_field_bool_array
	return test_struct_bool_with_array

def fillTestStructIntWithArray(test_struct_int_with_array):
	local_field_int_array = []
	elementfield_int = 1
	local_field_int_array.append(elementfield_int)
	test_struct_int_with_array.field_int = local_field_int_array
	return test_struct_int_with_array

def fillTestStructFloatWithArray(test_struct_float_with_array):
	local_field_float_array = []
	elementfield_float = 1.1
	local_field_float_array.append(elementfield_float)
	test_struct_float_with_array.field_float = local_field_float_array
	return test_struct_float_with_array

def fillTestStructStringWithArray(test_struct_string_with_array):
	local_field_string_array = []
	elementfield_string = "xyz"
	local_field_string_array.append(elementfield_string)
	test_struct_string_with_array.field_string = local_field_string_array
	return test_struct_string_with_array

def fillTestStructStructWithArray(test_struct_struct_with_array):
	local_field_struct_array = []
	elementfield_struct = fillTestStructStringWithArray([] )
	local_field_struct_array.append(elementfield_struct)
	test_struct_struct_with_array.field_struct = local_field_struct_array
	return test_struct_struct_with_array

def fillTestStructEnumWithArray(test_struct_enum_with_array):
	local_field_enum_array = []
	elementfield_enum = testbed1.api.Enum0.VALUE1
	local_field_enum_array.append(elementfield_enum)
	test_struct_enum_with_array.field_enum = local_field_enum_array
	return test_struct_enum_with_array
