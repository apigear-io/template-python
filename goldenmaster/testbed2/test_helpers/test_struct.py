import testbed2.api

def fillTestStruct1(test_struct1):
	test_struct1.field1 = 1;
	return test_struct1

def fillTestStruct2(test_struct2):
	test_struct2.field1 = 1;
	test_struct2.field2 = 1;
	return test_struct2

def fillTestStruct3(test_struct3):
	test_struct3.field1 = 1;
	test_struct3.field2 = 1;
	test_struct3.field3 = 1;
	return test_struct3

def fillTestStruct4(test_struct4):
	test_struct4.field1 = 1;
	test_struct4.field2 = 1;
	test_struct4.field3 = 1;
	test_struct4.field4 = 1;
	return test_struct4

def fillTestNestedStruct1(test_nested_struct1):
	test_nested_struct1.field1 = fillTestStruct1(testbed2.api.Struct1());
	return test_nested_struct1

def fillTestNestedStruct2(test_nested_struct2):
	test_nested_struct2.field1 = fillTestStruct1(testbed2.api.Struct1());
	test_nested_struct2.field2 = fillTestStruct2(testbed2.api.Struct2());
	return test_nested_struct2

def fillTestNestedStruct3(test_nested_struct3):
	test_nested_struct3.field1 = fillTestStruct1(testbed2.api.Struct1());
	test_nested_struct3.field2 = fillTestStruct2(testbed2.api.Struct2());
	test_nested_struct3.field3 = fillTestStruct3(testbed2.api.Struct3());
	return test_nested_struct3
