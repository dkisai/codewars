def camel_case(string):
    return string.title().replace(' ','')
#    all = ''
#    for x in string:
#        all += x.capitalize()
#    return all
#

    #your code here newlist = [x for x in l if type(x) == int]

print(camel_case("diego kisai alba gallart"))
#test.assert_equals(camel_case("test case"), "TestCase")
#test.assert_equals(camel_case("camel case method"), "CamelCaseMethod")
#test.assert_equals(camel_case("say hello "), "SayHello")
#test.assert_equals(camel_case(" camel case word"), "CamelCaseWord")
#test.assert_equals(camel_case(""), "")